package main

import (
	"fmt"
	"strconv"
)

func valid(s string, c *int) {
	if s == "" {
		*c += 1
		return
	}
	first := s[0]
	if first == '0' {
		// string is not valid if starts with 0
		return
	}
	valid(s[1:], c)
	if len(s) > 1 {
		second := s[1]
		newDigit, _ := strconv.Atoi(string(first) + string(second))
		// fmt.Println("Checking 2n digit", newDigit)
		if newDigit <= 26 {
			valid(s[2:], c)
		}
	}
}

func numDecodings(s string) int {
	var counter int = 0
	valid(s, &counter)
	return counter
}

func main() {
	fmt.Println(numDecodings("12"))     // 2
	fmt.Println(numDecodings("226"))    // 3
	fmt.Println(numDecodings("227"))    // 2
	fmt.Println(numDecodings("227217")) // 2
	fmt.Println(numDecodings("06"))     // 0
	fmt.Println(numDecodings("111111")) // 0
	// fmt.Println(numDecodings("111111111111111111111111111111111111111111111"))// 0
}
