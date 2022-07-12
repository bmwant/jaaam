package main

import "fmt"

func max(a, b int) int {
	if a >= b {
		return a
	}
	return b
}

func rob(nums []int) int {
	for i := 2; i < len(nums); i++ {
		far := 0
		if i-3 >= 0 {
			far = nums[i-3]
		}
		near := nums[i-2]
		nums[i] += max(far, near)
	}
	here := nums[len(nums)-1]
	there := 0
	if len(nums) > 1 {
		there = nums[len(nums)-2]
	}
	// return max(here+rob(nums[2:]), next+rob(nums[1:]))
	fmt.Println(nums)
	return max(here, there)
}

func main() {
	// arr := []int{2, 7, 9, 3, 1}
	fmt.Println(rob([]int{2, 7, 9, 3, 1}))
	fmt.Println(rob([]int{1, 2, 3, 1}))
}
