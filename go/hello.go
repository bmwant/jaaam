package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println("Hello, World!")
	a := 'a'
	b := 'b'
	c := string(a) + string(b)
	fmt.Println("This is c", a, b, c)
	res := 237 % int(10e9+7)
	fmt.Printf("%d\n", res)
	fmt.Println("max int64", math.MaxInt64)
}
