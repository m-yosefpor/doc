If you implement both the Stringer and error interfaces for a type in Go, the error interaface is superseded and is used for print!!!!

so in return of Error, you can't use %v, as it is a circular dependency, and you should cast it first to sth else

e.g.


package main

import "fmt"

type Moh float64

func (m Moh) Error() string {
	return fmt.Sprintf("hi %v", float64(m))
}

func main() {
	var m Moh = 2
	fmt.Println(m)
}


and not "return fmt.Sprintf("hi %v", m)"
