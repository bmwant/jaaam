package main

import (
	"fmt"
	"math"
)

func gcd(a, b int) int {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}

func lcm(a, b int) int {
	return int(a * b / gcd(a, b))
}

type Elem struct {
	Position  int
	Steps     int
	BackJumps int
	//	History   []int
}

func max(arr []int) int {
	max := arr[0]
	for _, val := range arr {
		if val > max {
			max = val
		}
	}
	return max
}

func contains(arr []int, elem int) bool {
	for _, a := range arr {
		if a == elem {
			return true
		}
	}
	return false
}

func minimumJumps(forbidden []int, a int, b int, x int) int {
	boundary := max(append(forbidden, x)) + a + b
	visited := make([]int, boundary+1)
	for i, _ := range visited {
		visited[i] = math.MaxInt
	}
	// queue = append(queue, Elem{0, 0, true})
	minJumps := math.MaxInt
	// history := []int{0}
	queue := []Elem{{0, 0, 0}}
	// BFS
	for len(queue) > 0 {
		elem := queue[len(queue)-1] // take last element
		pos := elem.Position
		back := elem.BackJumps
		// re-slice, equivalent to pop from queue
		queue = queue[:len(queue)-1]
		// we reached a destination, check num of steps
		if pos == x && elem.Steps < minJumps {
			minJumps = elem.Steps
			// history = elem.History
			continue
		}
		// jump forward
		newSteps := elem.Steps + 1
		if pos+a <= boundary && !contains(forbidden, pos+a) && visited[pos+a] > newSteps {
			// hNew := elem.History
			// hNew = append(hNew, pos+a)
			queue = append(queue, Elem{pos + a, newSteps, 0})
			// fmt.Println("Jumping forward to", pos+a)
			visited[pos+a] = newSteps
		}
		// jump backward
		if back == 0 && pos-b > 0 && !contains(forbidden, pos-b) && visited[pos-b] > newSteps {
			queue = append(queue, Elem{pos - b, newSteps, 1})
			// fmt.Println("Jumping backward to", pos-b)
			visited[pos-b] = newSteps
		}
	}
	if minJumps == math.MaxInt {
		return -1
	}
	return minJumps
}

func main() {
	// fmt.Println(minimumJumps([]int{14, 4, 18, 1, 15}, 3, 15, 9))      // 3
	// fmt.Println(minimumJumps([]int{1998}, 1999, 2000, 2000))          // 3998
	// fmt.Println(minimumJumps([]int{8, 3, 16, 6, 12, 20}, 15, 13, 11)) // -1
	// fmt.Println(minimumJumps([]int{1, 6, 2, 14, 5, 17, 4}, 16, 9, 7)) // 2
	// f := []int{8, 3, 16, 6, 12, 20}
	// fmt.Println(minimumJumps(f, 15, 13, 11)) // -1
	// fmt.Println(minimumJumps([]int{162, 118, 178, 152, 167, 100, 40, 74, 199, 186, 26, 73, 200, 127, 30, 124, 193, 84, 184, 36, 103, 149, 153, 9, 54, 154, 133, 95, 45, 198, 79, 157, 64, 122, 59, 71, 48, 177, 82, 35, 14, 176, 16, 108, 111, 6, 168, 31, 134, 164, 136, 72, 98}, 29, 98, 80)) // 121
	fmt.Println(minimumJumps([]int{3}, 14, 5, 90)) // 20
	f1 := []int{1401, 832, 1344, 173, 1529, 1905, 1732, 277, 1490, 650, 1577, 1886, 185, 1728, 1827, 1924, 1723, 1034, 1839, 1722, 1673, 1198, 1667, 538, 911, 1221, 1201, 1313, 251, 752, 40, 1378, 1515, 1789, 1580, 1422, 907, 1536, 294, 1677, 1807, 1419, 1893, 654, 1176, 812, 1094, 1942, 876, 777, 1850, 1382, 760, 347, 112, 1510, 1278, 1607, 1491, 429, 1902, 1891, 647, 1560, 1569, 196, 539, 836, 290, 1348, 479, 90, 1922, 111, 1411, 1286, 1362, 36, 293, 1349, 667, 430, 96, 1038, 793, 1339, 792, 1512, 822, 269, 1535, 1052, 233, 1835, 1603, 577, 936, 1684, 1402, 1739, 865, 1664, 295, 977, 1265, 535, 1803, 713, 1298, 1537, 135, 1370, 748, 448, 254, 1798, 66, 1915, 439, 883, 1606, 796}
	fmt.Println(minimumJumps(f1, 19, 18, 1540)) // 120
}
