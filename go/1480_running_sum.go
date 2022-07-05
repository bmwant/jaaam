package main

import (
	"fmt"
)

func runningSum(nums []int) []int {
	for i := 1; i < len(nums); i++ {
		c := nums[i]
		nums[i] = nums[i-1] + c
	}
	return nums
}

func main() {
	fmt.Println(runningSum([]int{1, 2, 3, 4}))
	fmt.Println(runningSum([]int{1, 1, 1, 1, 1}))
	fmt.Println(runningSum([]int{3, 1, 2, 10, 1}))
}
