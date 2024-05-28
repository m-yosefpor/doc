package main

import (
	"sync"
)

type RWLock struct {
	lock        sync.Mutex
	writeLock   sync.Mutex
	readersCount int
}

func NewRWLock() *RWLock {
	return &RWLock{}
}

// RLock increments the count of readers and ensures exclusive access for writers is blocked.
func (rwl *RWLock) RLock() {
	rwl.lock.Lock()
	defer rwl.lock.Unlock()
	if rwl.readersCount == 0 {
		rwl.writeLock.Lock()
	}
	rwl.readersCount++
}

// RUnlock decrements the count of readers and if no more readers are present, allows writers to proceed.
func (rwl *RWLock) RUnlock() {
	rwl.lock.Lock()
	defer rwl.lock.Unlock()
	rwl.readersCount--
	if rwl.readersCount == 0 {
		rwl.writeLock.Unlock()
	}
}

// Lock ensures exclusive access for writing.
func (rwl *RWLock) Lock() {
	rwl.writeLock.Lock()
}

// Unlock releases exclusive access for writing.
func (rwl *RWLock) Unlock() {
	rwl.writeLock.Unlock()
}

func main() {
	// Example usage
}
