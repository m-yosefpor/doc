package main

import(
	"fmt"
	"os"
	"bufio"
)

func main(){
	read := bufio.NewReader(os.Stdin)
	fmt.Println("Hello World!")
	text ,  _ :=  read.ReadString('\n')
	fmt.Println(text)
	var a int
	fmt.Println(a)
}
