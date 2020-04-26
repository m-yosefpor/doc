package main

import (
	"fmt"
	"time"
)

func main(){

	s:= []int{1,1,2,2}
	c:= make(chan int)
	go sum1(s[:len(s)/2],c)
	go sum2(s[len(s)/2:],c)
	x , y := <-c , <-c
	fmt.Println(x,y)
}

func sum1(s []int, c chan int){
	sum:=0
	for _,v := range s{
		sum+=v
	}
	c <- sum
}

func sum2(s []int, c chan int){
	time.Sleep(2*time.Second)
	sum:=0
	for _,v := range s{
		sum+=v
	}
	c <- sum
}
