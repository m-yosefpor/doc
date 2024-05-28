package main

import (
	"fmt"
	"sync"
)

var wg sync.WaitGroup

type BG struct {
	b            []int
	cap          int
	mu           sync.Mutex
	condNotFull  *sync.Cond
	condNotEmpty *sync.Cond
}

func NewBG(cap int) *BG {
	bg := BG{
		b:   make([]int, 0, cap),
		cap: cap,
	}
	bg.condNotEmpty = sync.NewCond(&bg.mu)
	bg.condNotFull = sync.NewCond(&bg.mu)
	return &bg
}

func (bg *BG) Push(element int) {
	bg.mu.Lock()
	defer bg.mu.Unlock()

	for len(bg.b) == bg.cap {
		bg.condNotFull.Wait()
	}

	bg.b = append(bg.b, element)
	fmt.Println(bg.b)
	bg.condNotEmpty.Signal()
}

func (bg *BG) Pop() int {
	bg.mu.Lock()
	defer bg.mu.Unlock()

	for len(bg.b) == 0 {
		bg.condNotEmpty.Wait()
	}

	value := bg.b[0]
	bg.b = bg.b[1:]
	fmt.Println(bg.b)
	bg.condNotFull.Signal()
	return value
}

func main() {

	bg := NewBG(3)

	for i := 0; i < 50; i++ {
		i := i
		wg.Add(1)
		go func() {
			defer wg.Done()
			produce(bg, i)
		}()
	}

	for i := 0; i < 50; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			consume(bg)
		}()
	}

	wg.Wait()
}

func produce(bg *BG, element int) {
	fmt.Println("push:", element)
	// s.mu.Lock()
	// defer s.mu.Unlock()
	// s.b = append(s.b, element)
	bg.Push(element)
}

func consume(bg *BG) {
	p := bg.Pop()
	// s.mu.Lock()
	// defer s.mu.Unlock()
	// s.b = append(s.b, p)
	fmt.Println("consume:", p)
}
