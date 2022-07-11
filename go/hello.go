package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println("Hello, World!")
	res := 237 % int(10e9+7)
	fmt.Printf("%d\n", res)
	fmt.Println("max int64", math.MaxInt64)
}
