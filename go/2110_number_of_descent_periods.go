package main

import "fmt"

func getPerm(n int) int64 {
	return int64((n + 1) * n / 2)
}

func getDescentPeriods(prices []int) int64 {
	var total int64 = 0
	curMax := 1
	for i := 1; i < len(prices); i++ {
		if prices[i] == prices[i-1]-1 {
			curMax++
		} else {
			total += getPerm(curMax)
			curMax = 1
		}
	}

	total += getPerm(curMax)
	return total
}

func main() {
	fmt.Println(getDescentPeriods([]int{3, 2, 1, 4}))    // 7
	fmt.Println(getDescentPeriods([]int{3, 2, 1, 4, 3})) // 9
	fmt.Println(getDescentPeriods([]int{8, 6, 7, 7}))    // 4
	fmt.Println(getDescentPeriods([]int{1}))             // 1
}
