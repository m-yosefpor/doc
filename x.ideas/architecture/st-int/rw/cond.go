type RWLock struct {
	lock           sync.Mutex
	rCond          *sync.Cond
	wCond          *sync.Cond
	readersCount   int
	writersWaiting int
}

func NewRWLock() *RWLock {
	rwl := &RWLock{}
	rwl.rCond = sync.NewCond(&rwl.lock)
	rwl.wCond = sync.NewCond(&rwl.lock)
	return rwl
}

func (rwl *RWLock) RLock() {
	rwl.lock.Lock()
	for rwl.writersWaiting > 0 {
		rwl.rCond.Wait() // This waits for a signal before checking the condition again
	}
	rwl.readersCount++
	rwl.lock.Unlock()
}

func (rwl *RWLock) RUnlock() {
	rwl.lock.Lock()
	rwl.readersCount--
	if rwl.readersCount == 0 && rwl.writersWaiting > 0 {
		rwl.wCond.Signal() // Wake up one goroutine waiting on this condition
	}
	rwl.lock.Unlock()
}

// Adjust Lock and Unlock methods accordingly
func (rwl *RWLock) Lock() {
	rwl.lock.Lock()
	rwl.writersWaiting++
	for rwl.readersCount > 0 {
		rwl.wCond.Wait() // This will atomically unlock rwl.lock and suspend the goroutine.
	}
}

func (rwl *RWLock) Unlock() {
	rwl.writersWaiting--
	if rwl.writersWaiting == 0 {
		rwl.rCond.Broadcast()
	} else {
		rwl.wCond.Signal()
	}
	rwl.lock.Unlock()
}
