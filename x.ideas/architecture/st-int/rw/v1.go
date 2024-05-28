package main

import (
	"sync"
	"time"
)



type RWLock struct {
	readersCount int
	mu sync.Mutex
}


func NewRWLock() *RWLock {
	return &RWLock{
	}
}

func (rwl *RWLock) RLock() {
	rwl.mu.Lock()
	defer rwl.mu.Unlock()

	rwl.readersCount++
}

func (rwl *RWLock) RUnlock() {
	rwl.mu.Lock()
	defer rwl.mu.Unlock()

	rwl.readersCount--
}

func (rwl *RWLock) Lock() {

	for rwl.readersCount != 0 {

		time.Sleep(1*time.Millisecond)
	}
	rwl.mu.Lock()
}
func (rwl *RWLock) Unlock() {
	rwl.mu.Unlock()
}



func main() {

	for i:=0;i<10;i++{
		go func(){

		}
	}
}
