package main

import (
	"fmt"
	"math"
	"sort"
)

type Pair struct {
	Value int
	Count int
}

func min(a, b int) int {
	if a <= b {
		return a
	}
	return b
}

func getMajority(nums []int) []Pair {
	counter := make(map[int]int)
	for _, v := range nums {
		counter[v] += 1
	}
	var pairs []Pair
	for k, v := range counter {
		pairs = append(pairs, Pair{Value: k, Count: v})
	}

	sort.Slice(pairs, func(i, j int) bool {
		return pairs[i].Count > pairs[j].Count
	})

	return pairs
}

func minimumOperations(nums []int) int {
	even, odd := []int{}, []int{}
	for i, v := range nums {
		if i%2 == 0 {
			even = append(even, v)
		} else {
			odd = append(odd, v)
		}
	}
	evenTop := getMajority(even)
	oddTop := getMajority(odd)
	// fmt.Println(evenTop)
	// fmt.Println(oddTop)
	minOperations := math.MaxInt64
	for i := 0; i < min(2, len(evenTop)); i++ {
		for j := 0; j < min(2, len(oddTop)); j++ {
			if evenTop[i].Value != oddTop[j].Value {
				// fmt.Println(evenTop[i].Value, oddTop[j].Value)
				changeEven := len(even) - evenTop[i].Count
				changeOdd := len(odd) - oddTop[j].Count
				// fmt.Printf("change even: %d ", changeEven)
				// fmt.Printf("change odd: %d\n", changeOdd)
				operations := changeEven + changeOdd
				if operations < minOperations {
					minOperations = operations
				}
			}
		}
	}
	if minOperations == math.MaxInt64 {
		return len(odd) //
	}
	return minOperations
}

func main() {
	fmt.Println(minimumOperations([]int{3, 1, 3, 2, 4, 3}))       // 3
	fmt.Println(minimumOperations([]int{1, 2, 2, 2, 2}))          // 2
	fmt.Println(minimumOperations([]int{1, 2, 1, 2, 1, 2, 3, 4})) // 2
	fmt.Println(minimumOperations([]int{1, 1, 1, 1, 1}))          // 3
}
