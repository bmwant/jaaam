package main

import "fmt"

func longestPalindrome(s string) string {
	maxLen := 1
	start := 0
	expand := func(l, r int) int {
		if s[l] != s[r] {
			return 0
		}
		for l-1 >= 0 && r+1 < len(s) {
			if s[l-1] != s[r+1] {
				break
			}
			l--
			r++
		}
		// fmt.Println("Return", r, l, r-l+1)
		return r - l + 1
	}
	for i := 1; i < len(s); i++ {
		even := expand(i-1, i)
		odd := expand(i, i)
		if even > maxLen {
			maxLen = even
			start = i - even/2
			// fmt.Println("i", i, "even", even, "maxLen", maxLen, "start", start)
		}
		if odd > maxLen {
			maxLen = odd
			start = i - odd/2
			// fmt.Println("i", i, "odd", odd, "maxLen", maxLen, "start", start)
		}

	}
	return s[start : start+maxLen]
}

func main() {
	fmt.Println(longestPalindrome("a"))      // a
	fmt.Println(longestPalindrome("bb"))     // bb
	fmt.Println(longestPalindrome("babad"))  // bab
	fmt.Println(longestPalindrome("cbbd"))   // bb
	fmt.Println(longestPalindrome("ccbd"))   // cc
	fmt.Println(longestPalindrome("dabbac")) // abba
}
