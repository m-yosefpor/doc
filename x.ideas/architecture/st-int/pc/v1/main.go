package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

var wg sync.WaitGroup

func main() {
	ch := make(chan int, 3)
	for i := 0; i < 10; i++ {
		wg.Add(1)
		go producers(ch)
	}

	for i := 0; i < 3; i++ {
		wg.Add(1)
		go consumers(ch)
	}

	wg.Wait()
}

func producers(ch chan int) {
	random := rand.Intn(2)
	time.Sleep(time.Second * time.Duration(random))
	ch <- random
	wg.Done()
}

func consumers(ch chan int) {
	data := <-ch
	time.Sleep(time.Second * 2)
	fmt.Println(data * 2)
	wg.Done()
}
