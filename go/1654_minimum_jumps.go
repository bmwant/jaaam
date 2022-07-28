package main

import (
	"fmt"
	"math"
)

func minimumJumps(forbidden []int, a int, b int, x int) int {
	jumps := make([]int, 2001)
	for _, f := range forbidden {
		jumps[f] = -1
	}
	minJumps := math.MaxInt
	var jumpTo func(loc, counter, backJumps int)
	jumpTo = func(loc, counter, backJumps int) {
		// fmt.Println("Jumped to", loc, counter)
		if loc >= len(jumps) || loc < 0 || jumps[loc] == -1 {
			return
		}
		if loc == x && backJumps <= 2 {
			fmt.Println("Reached target", x, "with steps", counter, "using backjumps", backJumps)
			minJumps = counter
			return
		}
		if jumps[loc] == 0 {
			jumps[loc] = counter
			jumpTo(loc+a, counter+1, 0)
			jumpTo(loc-b, counter+1, backJumps+1)
			// if backJumps < 2 {
			// jumpTo(loc-b, counter+1, backJumps+1)
			// }
		}
	}
	jumpTo(0, 0, 0)
	if minJumps == math.MaxInt {
		return -1
	}
	return minJumps
}

func main() {
	fmt.Println(minimumJumps([]int{14, 4, 18, 1, 15}, 3, 15, 9))      // 3
	fmt.Println(minimumJumps([]int{[1998}, 1999, 2000, 2000))      // 3
	fmt.Println(minimumJumps([]int{8, 3, 16, 6, 12, 20}, 15, 13, 11)) // -1
	fmt.Println(minimumJumps([]int{1, 6, 2, 14, 5, 17, 4}, 16, 9, 7)) // 2
	fmt.Println(minimumJumps([]int{8, 3, 16, 6, 12, 20}, 15, 13, 11))
	fmt.Println(minimumJumps([]int{162, 118, 178, 152, 167, 100, 40, 74, 199, 186, 26, 73, 200, 127, 30, 124, 193, 84, 184, 36, 103, 149, 153, 9, 54, 154, 133, 95, 45, 198, 79, 157, 64, 122, 59, 71, 48, 177, 82, 35, 14, 176, 16, 108, 111, 6, 168, 31, 134, 164, 136, 72, 98}, 29, 98, 80)) // 121
}
