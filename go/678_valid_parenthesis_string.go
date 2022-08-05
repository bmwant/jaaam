package main

import "fmt"

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func checkValidString(s string) bool {
	low, high := 0, 0
	for _, c := range s {
		if c == '(' {
			low += 1
		} else {
			// fmt.Println("Here")
			low -= 1
		}
		if c != ')' {
			high++
		} else {
			high--
		}

		// fmt.Println(c, ":", low, high)
		if high < 0 {
			return false
		}
		low = max(low, 0)
	}
	return low == 0

}

func main() {
	fmt.Println(checkValidString("()"))    // true
	fmt.Println(checkValidString("(*)"))   // true
	fmt.Println(checkValidString("(*))"))  // true
	fmt.Println(checkValidString("(***)")) // false
	fmt.Println(checkValidString(")(*"))   // false
}
