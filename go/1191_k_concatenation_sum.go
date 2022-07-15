package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
)

func readFromFile() []int {
	file, err := os.Open("/home/pkovalenko/projects/jaaam/go/1191_test01.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	lines, _ := csv.NewReader(file).ReadAll()
	arr := []int{}
	for _, line := range lines {
		for _, val := range line {
			valInt, err := strconv.Atoi(val)
			if err != nil {
				log.Fatal(err)
			}
			arr = append(arr, valInt)
		}
	}
	return arr
}

func getPrev(i, j int, arr []int) int {
	if i == 0 && j == 0 {
		return 0
	}
	if j == 0 {
		return arr[len(arr)-1]
	}
	return arr[j-1]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func justSum(arr []int) int {
	sum := 0
	for i := 0; i < len(arr); i++ {
		sum += arr[i]
	}
	return max(sum, 0)
}

func maxSub(arr []int) int {
	maxSum := arr[0]
	for i := 1; i < len(arr); i++ {
		curMax := max(arr[i], arr[i]+arr[i-1])
		arr[i] = curMax
		if curMax > maxSum {
			maxSum = curMax
		}
	}
	return max(0, maxSum)
}

func kConcatenationMaxSum(arr []int, k int) int {
	mod := int(math.Pow(10, 9)) + 7
	arr2 := make([]int, 2*len(arr))
	copy(arr2[:len(arr)], arr)
	copy(arr2[len(arr):], arr)
	// fmt.Println(arr2)
	m1 := justSum(arr)
	if k == 1 {
		return maxSub(arr) % mod
	}
	m2 := maxSub(arr2)
	// fmt.Println("m1", m1, "m2", m2)
	return ((k-2)*m1 + m2) % mod
}

func main() {
	fmt.Println(kConcatenationMaxSum([]int{1, 2}, 3))     // 9
	fmt.Println(kConcatenationMaxSum([]int{1, -2, 1}, 5)) // 2
	fmt.Println(kConcatenationMaxSum([]int{-1, -2}, 7))   // 0
	fmt.Println(kConcatenationMaxSum([]int{1, -1}, 1))    // 1
	// fmt.Println(kConcatenationMaxSum([]int{5, 6, 7, -13, -13, 6, 7, 8}, 3)) // 0
	// arr := readFromFile()
	// fmt.Println(kConcatenationMaxSum(arr, 1))
	// fmt.Println(maxSub(arr))
}
