package main

import (
	"fmt"
	"sync"
	"time"
)

var wg sync.WaitGroup

type bufferedChannel struct {
	buffer []int
	cap    int
	signal chan bool
	mu     sync.Mutex
	condEmpty   *sync.Cond
}

func (b *bufferedChannel) Push(entry int) {
	b.cond.L.Lock()
	b.mu.Lock()
	defer b.mu.Unlock()

	if len(b.buffer) == b.cap {
		fmt.Println("waiting:", entry)
		b.cond.Wait()
	}
	fmt.Println("push:", entry)

	b.buffer = append(b.buffer, entry)
	fmt.Println("buff:", b.buffer)

	select {
	case b.signal <- true:
	default:
	}
}

func (b *bufferedChannel) Pop() int {
	b.mu.Lock()
	defer b.mu.Unlock()

	if len(b.buffer) == 0 {
		fmt.Println("waiting:")
		b.mu.Unlock()
		<-b.signal
		b.mu.Lock()
	}

	n := len(b.buffer)
	value := b.buffer[n-1]
	b.buffer = b.buffer[:n-1]
	fmt.Println("pop:", value)
	fmt.Println("buff:", b.buffer)

	select {
	case b.signal <- true:
	default:
	}

	return value
}

func main() {

	ch := &bufferedChannel{
		buffer: make([]int, 0, 2),
		cap:    2,
		signal: make(chan bool),
		cond:   sync.NewCond(&sync.Mutex{}),
	}

	for i := 0; i < 3; i++ {
		wg.Add(1)
		// time.Sleep(time.Second)
		go producers(ch, i)
	}

	for i := 0; i < 3; i++ {
		wg.Add(1)
		go consumers(ch)
	}

	wg.Wait()
}

func producers(ch *bufferedChannel, i int) {
	time.Sleep(time.Second * 1)
	ch.Push(i)
	wg.Done()
}

func consumers(ch *bufferedChannel) {
	data := ch.Pop()
	time.Sleep(time.Second * 2)
	fmt.Println(data)
	wg.Done()
}
