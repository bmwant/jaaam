package main

import (
	"fmt"
	"math"
)

func max(arr []int) int {
	max := arr[0]
	for _, val := range arr {
		if val > max {
			max = val
		}
	}
	return max
}

func minimumJumps(forbidden []int, a int, b int, x int) int {
	boundary := max(append(forbidden, x)) + a + b
	jumps := make([]int, boundary)
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
		if loc == x {
			fmt.Println("Reached target", x, "with steps", counter, "using backjumps", backJumps)
			minJumps = counter
			return
		}
		if jumps[loc] == 0 {
			jumps[loc] = counter
			jumpTo(loc+a, counter+1, 0)
			if backJumps == 0 {
				jumpTo(loc-b, counter+1, 1)
			}
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
	// fmt.Println(minimumJumps([]int{14, 4, 18, 1, 15}, 3, 15, 9))      // 3
	// fmt.Println(minimumJumps([]int{8, 3, 16, 6, 12, 20}, 15, 13, 11)) // -1
	// fmt.Println(minimumJumps([]int{1, 6, 2, 14, 5, 17, 4}, 16, 9, 7)) // 2
	// fmt.Println(minimumJumps([]int{8, 3, 16, 6, 12, 20}, 15, 13, 11))
	// fmt.Println(minimumJumps([]int{162, 118, 178, 152, 167, 100, 40, 74, 199, 186, 26, 73, 200, 127, 30, 124, 193, 84, 184, 36, 103, 149, 153, 9, 54, 154, 133, 95, 45, 198, 79, 157, 64, 122, 59, 71, 48, 177, 82, 35, 14, 176, 16, 108, 111, 6, 168, 31, 134, 164, 136, 72, 98}, 29, 98, 80)) // 121
	// f1 := []int{1401, 832, 1344, 173, 1529, 1905, 1732, 277, 1490, 650, 1577, 1886, 185, 1728, 1827, 1924, 1723, 1034, 1839, 1722, 1673, 1198, 1667, 538, 911, 1221, 1201, 1313, 251, 752, 40, 1378, 1515, 1789, 1580, 1422, 907, 1536, 294, 1677, 1807, 1419, 1893, 654, 1176, 812, 1094, 1942, 876, 777, 1850, 1382, 760, 347, 112, 1510, 1278, 1607, 1491, 429, 1902, 1891, 647, 1560, 1569, 196, 539, 836, 290, 1348, 479, 90, 1922, 111, 1411, 1286, 1362, 36, 293, 1349, 667, 430, 96, 1038, 793, 1339, 792, 1512, 822, 269, 1535, 1052, 233, 1835, 1603, 577, 936, 1684, 1402, 1739, 865, 1664, 295, 977, 1265, 535, 1803, 713, 1298, 1537, 135, 1370, 748, 448, 254, 1798, 66, 1915, 439, 883, 1606, 796}
	// fmt.Println(minimumJumps(f1, 19, 18, 1540)) // 120
	f := []int{8, 3, 16, 6, 12, 20}
	fmt.Println(minimumJumps(f, 15, 13, 11)) // -1
}
