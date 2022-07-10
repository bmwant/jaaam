package main

import "fmt"

func peopleAwareOfSecret(n int, delay int, forget int) int {
	p := make([]int, n)
	f := make([]int, forget)
	for i := 0; i < delay; i++ {
		p[i] = 1
	}
	for i := delay; i < n; i++ {
		start := i - forget
		end := i - delay
		sum := 0
		fmt.Printf("index: %d, start: %d, end: %d\n", i, start, end)
		for j := start; j <= end; j++ {
			sum += p[j]
		}
		p[i] = sum
	}
	fmt.Println(p)
	return p[n-1]
}

func main() {
	// fmt.Println(peopleAwareOfSecret(20, 2, 4)) // 5
	fmt.Println(peopleAwareOfSecret(4, 1, 3)) // 6
}
