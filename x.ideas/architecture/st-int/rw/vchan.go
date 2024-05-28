package main

import (
	"fmt"
	"sync"
	"time"
)

type RWLock struct {
	readRequest   chan bool
	writeRequest  chan struct{}
	readRelease   chan bool
	writeRelease  chan struct{}
	readersCount  int
}

func NewRWLock() *RWLock {
	rwl := &RWLock{
		readRequest:   make(chan bool),
		writeRequest:  make(chan struct{}),
		readRelease:   make(chan bool),
		writeRelease:  make(chan struct{}),
		readersCount:  0,
	}

	go rwl.manageAccess()

	return rwl
}

func (rwl *RWLock) manageAccess() {
	for {
		select {
		case <-rwl.readRequest:
			rwl.readersCount++
			rwl.readRequest <- true // Acknowledge the read request
		case <-rwl.readRelease:
			rwl.readersCount--
			if rwl.readersCount == 0 {
				// If no readers left, signal potential writers
				select {
				case rwl.writeRelease <- struct{}{}:
				default:
				}
			}
		case <-rwl.writeRequest:
			if rwl.readersCount == 0 {
				// If no readers, allow write immediately
				rwl.writeRequest <- struct{}{}
			} else {
				// Wait for all readers to release
				<-rwl.writeRelease
				rwl.writeRequest <- struct{}{}
			}
		case <-rwl.writeRelease:
			// Write completed, check if waiting readers
			if rwl.readersCount > 0 {
				rwl.readRequest <- true // Signal next waiting reader
			}
		}
	}
}

func (rwl *RWLock) RLock() {
	rwl.readRequest <- true
	<-rwl.readRequest // Wait for acknowledgment
}

func (rwl *RWLock) RUnlock() {
	rwl.readRelease <- true
}

func (rwl *RWLock) Lock() {
	rwl.writeRequest <- struct{}{}
	<-rwl.writeRequest // Wait for access
}

func (rwl *RWLock) Unlock() {
	rwl.writeRelease <- struct{}{}
}

func main() {
	rwLock := NewRWLock()

	var wg sync.WaitGroup

	// Simulate read operations
	for i := 0; i < 5; i++ {
		wg.Add(1)
		go func(reader int) {
			defer wg.Done()
			rwLock.RLock()
			fmt.Printf("Reader %d is reading\n", reader)
			time.Sleep(1 * time.Second) // Simulate read duration
			fmt.Printf("Reader %d is done reading\n", reader)
			rwLock.RUnlock()
		}(i)
	}

	// Simulate write operation
	wg.Add(1)
	go func() {
		defer wg.Done()
		rwLock.Lock()
		fmt.Println("Writer is writing")
		time.Sleep(2 * time.Second) // Simulate write duration
		fmt.Println("Writer is done writing")
		rwLock.Unlock()
	}()

	wg.Wait()
}
