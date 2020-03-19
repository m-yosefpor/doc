(output)
fmt.Print(a)
fmt.Println(a)


-------------------------------------------
(input)

reader := bufio.NewReader(os.Stdin)
text , err = reader.ReadString('\n')
text = strings.Replace(text, "\n", "",-1)
char , _ , err = reader.ReadRune()
---
scanner := bufio.NewScanner(os.Stdin)
scanner.Scan()
text = scanner.Text()
---
var i int
var s string
fmt.Scanf("%d",&i)
fmt.Scan(&i)
fmt.Scanln(&s)
----------------------------------
package main

import (
	"fmt"
	"strings"
	"input"
	"bufio"
	"os"
	"math/rand"
)

func main(){
	fmt.Println("Hello World!")
	read := bufio.NewReader(os.Stdin)
	text , _ := read.ReadString('\n')
	a ,b int // var a,b int
	v := 3
	b map[string]int
	b['hello']=2
	fmt.Println(v,a,b)
	rand.Seed(4)
	a = rand.Intn(10)
}
