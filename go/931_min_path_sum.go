package main

import "fmt"

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func printMatrix(m [][]int) {
	for i := 0; i < len(m); i++ {
		for j := 0; j < len(m[i]); j++ {
			fmt.Printf("%2d ", m[i][j])
		}
		fmt.Println()
	}
}
func minFallingPathSum(matrix [][]int) int {
	maxVal := 100 * 100
	minPath := maxVal
	for i := 1; i < len(matrix); i++ {
		for j := 0; j < len(matrix[i]); j++ {
			left, top, right := maxVal, matrix[i-1][j], maxVal
			if j-1 >= 0 {
				left = matrix[i-1][j-1]
			}
			if j+1 < len(matrix[i]) {
				right = matrix[i-1][j+1]
			}
			matrix[i][j] += min(left, min(top, right))
		}
	}
	lastRow := matrix[len(matrix)-1]
	for _, v := range lastRow {
		if v < minPath {
			minPath = v
		}
	}
	return minPath
}

func main() {
	m1 := [][]int{
		{2, 1, 3},
		{6, 5, 4},
		{7, 8, 9},
	}
	fmt.Println(minFallingPathSum(m1))
	m2 := [][]int{
		{-19, 57},
		{-40, -5},
	}
	fmt.Println(minFallingPathSum(m2))
}
