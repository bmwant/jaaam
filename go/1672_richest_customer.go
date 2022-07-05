package main

import "fmt"

func maximumWealth(accounts [][]int) int {
	max := 0
	for i := 0; i < len(accounts); i++ {
		curSum := 0
		for j := 0; j < len(accounts[i]); j++ {
			curSum += accounts[i][j]
		}
		if curSum > max {
			max = curSum
		}
	}
	return max
}

func main() {
	fmt.Println(maximumWealth([][]int{{1, 2, 3}, {3, 2, 1}}))
	fmt.Println(maximumWealth([][]int{{1, 5}, {7, 3}, {3, 5}}))
	fmt.Println(maximumWealth([][]int{{2, 8, 7}, {7, 1, 3}, {1, 9, 5}}))
}
