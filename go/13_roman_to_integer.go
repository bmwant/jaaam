package main

import "fmt"

func romanToInt(s string) int {
	charMap := map[rune]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}
	values := make([]int, len(s))
	for i, c := range s {
		// fmt.Println(i, c)
		values[i] = charMap[c]
	}
	result := 0
	for i := 0; i < len(values); i++ {
		cur := values[i]
		if i+1 < len(values) && values[i+1] > cur {
			result += values[i+1] - cur
			i++
		} else {
			result += cur
		}
	}
	return result
}

func main() {
	fmt.Println(romanToInt("MCMXCIV")) // 1994
	fmt.Println(romanToInt("LVIII"))   // 58
	fmt.Println(romanToInt("III"))     // 3
}
