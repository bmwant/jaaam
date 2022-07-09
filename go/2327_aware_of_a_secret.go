package main

import "fmt"

func peopleAwareOfSecret(n int, delay int, forget int) int {
	p := make([]int, n)

	for i := 0; i < delay; i++ {
		p[i] = 1
	}
	fmt.Println(p)
	for i := delay; i < n; i++ {
		window := 0
		start := i - forget + 1
		end := i - delay + 1
		if start < 0 {
			start = 0
		}
		for j := start; j < end; j++ {
			window += p[j]
		}
		p[i] = window
	}
	fmt.Println(p)
	return p[n-1]
}

func main() {
	fmt.Println(peopleAwareOfSecret(9, 2, 4)) // 5
	// fmt.Println(peopleAwareOfSecret(4, 1, 3)) // 6
}
