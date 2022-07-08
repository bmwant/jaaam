package main

import "fmt"

func climbStairs(n int) int {
	if n == 1 {
		return 1
	}
	calc := make([]int, n)
	calc[0] = 1
	calc[1] = 2
	for i := 2; i < n; i++ {
		calc[i] = calc[i-1] + calc[i-2]
	}
	// fmt.Println(calc)
	return calc[n-1]
}

func main() {
	fmt.Println(climbStairs(3)) // 3
	fmt.Println(climbStairs(2)) // 2
}
