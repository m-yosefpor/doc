(output)
fmt.Print(a)
fmt.Println(a)
fmt.Printf("type %T , value %v\n",a,a)


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
fmt.Scanf("%d",&i)
fmt.Scan(&i)
fmt.Scanln(&s)
----------------------------------
//types
bool

string

int  int8  int16  int32  int64
uint uint8 uint16 uint32 uint64 uintptr
byte // alias for uint8

rune // alias for int32
     // represents a Unicode code point

float32 float64

complex64 complex128
---
type a struct{
	var s string
}

type b float32

type c interface{
	M()
}


type c interface{
	MM() float64
}
-------------------------------------
var i int
var s string
var i,j int = 1,2 //asserting type e.g. var i float =2
var i = 2 //type inference  //no use
a := 2 //type inference
a,b := 2 , 3.4


------------------------------------
for i:=1 ; i< 10 ; i++ { //init and post are optional //init only scoped in for
	sth
}


for ; i<10 ; {
	
}


for i<10 { //while
	
}

for {  // while trure

}
------------------------
for i,v := range sth{ // for _,v := range // for i,_ range // for i:= range
	sth
}





------------------------------------------
if sth {
}

if a:=2; a<3{ //scope only within if, and else block
}

if sth{
	sth
} else {
	sthelse
}


switch init:=2; vari{
case 2:
	sth1
	sth2
case 3:
	sth
default:
	sth
	sth2
}


switch { // switch true
case cond1:
	sth
case cond2:
	sth
case cond3:
	sth
default:
	sth
}



switch v := i.(type) { //type switch
case T:
    // here v has type T
case S:
    // here v has type S
default:
    // no match; here v has the same type as i
}
-------------------------
func add(x int, y int) int {
	return x + y
}

func add(x, y int) int {
	return x + y
}

func swap(x, y string) (string, string) {
	return y, x
}

func split(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return
}

var (
	area = func(l int, b int) int {
		return l * b
	}
)
----------------
## no class: struct, an methods
type ss struct{
	a,b int
}

func (b ss) met(a int) string { // reciever argument after func keywor
	if a>0{
		return "hello"
	}else{
		return "hi"
	}
}
-----------------------
defer function(arg1,arg2)//The deferred call's arguments are evaluated immediately, but the function call is not executed until the surrounding function returns.


go f('hi')//goroutine

ch := make(chan int) //channel
ch <- v    // Send v to channel ch.
v := <-ch  // Receive from ch, and
           // assign value to v.
------------------------
var a [5]string
a[0] = "hi"
a[low:high]
a[:20]
a[2:]
a[:]
-------------------------------
var a map[string]int

------------------------------
fmt.Stringer //built-in
type Striner interface {
	String() string
}

error //builtin
type error interface {
	Error() string
}

---------------------------------------
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
