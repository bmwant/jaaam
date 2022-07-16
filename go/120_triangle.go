package main

import "fmt"

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func minimumTotal(triangle [][]int) int {
	// for i := 0; i < len(triangle); i++ {
	// for j := 0; j < len(triangle[i]); j++ {
	// fmt.Print(triangle[i][j], " ")
	// }
	// fmt.Println()
	// }
	for i := len(triangle) - 2; i >= 0; i-- {
		for j := 0; j < len(triangle[i]); j++ {
			bottom := triangle[i+1][j]
			right := triangle[i+1][j+1]
			triangle[i][j] += min(bottom, right)
		}
	}
	fmt.Println(triangle)
	return triangle[0][0]
}

func main() {
	fmt.Println(minimumTotal([][]int{{2}, {3, 4}, {6, 5, 7}, {4, 1, 8, 3}}))
	fmt.Println(minimumTotal([][]int{{-10}}))
}
