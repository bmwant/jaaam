package main

import (
	"fmt"
)

func main() {
	a := []int{1, 5, 3, 0, 7}
	b := a
	b = append(b, 10)
	fmt.Printf(fmt.Sprintf("%v", a))
	fmt.Printf(fmt.Sprintf("%v", b))
	b[0] = 8
	fmt.Printf(fmt.Sprintf("%v", a))
	fmt.Printf(fmt.Sprintf("%v", b))
	a1 := 7
	a2 := 2
	fmt.Println(a1 / a2)
}
