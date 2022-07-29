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

func numDecodings2(s string) int {
	dec := make([]int, len(s))
	if s[0] == '0' {
		return 0
	}
	last := len(s) - 1
	dec[last] = 1
	if s[last] == '0' {
		dec[last] = 0
	}
	for i := len(s) - 2; i >= 0; i-- {
		num, _ := strconv.Atoi(string(s[i]) + string(s[i+1]))
		rest := 1
		if i+2 < len(s) {
			rest = dec[i+2]
		}
		if num > 26 || s[i] == '0' {
			rest = 0
		}
		dec[i] = dec[i+1] + rest
	}

	return dec[0]
}

func numDecodings(s string) int {
	dec := make([]int, len(s)+1)
	if s[0] == '0' {
		return 0
	}
	dec[0] = 1
	dec[1] = 1
	for i := 2; i < len(s)+1; i++ {
		// one step jump
		num, _ := strconv.Atoi(string(s[i-1]))
		if num > 0 && num <= 9 {
			dec[i] += dec[i-1]
		}
		// two steps jump
		num, _ = strconv.Atoi(string(s[i-2]) + string(s[i-1]))
		if num >= 10 && num <= 26 {
			dec[i] += dec[i-2]
		}
	}
	return dec[len(s)]
}

func numDecodingsRec(s string) int {
	var counter int = 0
	valid(s, &counter)
	return counter
}

func main() {
	// fmt.Println(numDecodings("12"))     // 2
	// fmt.Println(numDecodings("226"))    // 3
	// fmt.Println(numDecodings("227"))    // 2
	// fmt.Println(numDecodings("261217")) // 10
	// fmt.Println(numDecodings("06"))
	fmt.Println(numDecodings("10"))   // 1
	fmt.Println(numDecodings("1010")) // 1
	fmt.Println(numDecodings("2101")) // 1
	// fmt.Println(numDecodings("111111"))                                        // 13
	// fmt.Println(numDecodings("111111111111111111111111111111111111111111111")) // 0
}
