package main

import(
	"fmt"
	"os"
	"bufio"
	"time"
)

func main(){
	read := bufio.NewReader(os.Stdin)
	fmt.Println("Hello World!")
	text ,  _ :=  read.ReadString('\n')
	fmt.Println(text)
	fmt.Println(time.Now())
	var a int
	fmt.Println(a)
}
