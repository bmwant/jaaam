package main

import (
	"fmt"
)

func canConstruct(ransomNote string, magazine string) bool {
	// var substr string = magazine[1:]
	// fmt.Println(substr)

	var charMap = make(map[byte]int)
	for i := 0; i < len(magazine); i++ {
		// fmt.Printf("%c", magazine[i])
		charMap[magazine[i]] += 1
	}

	for i := 0; i < len(ransomNote); i++ {
		val := charMap[ransomNote[i]]
		if val == 0 {
			return false
		}
		charMap[ransomNote[i]] -= 1
	}
	// fmt.Println(charMap)
	return true
}

func main() {
	fmt.Println(canConstruct("a", "b"))
	fmt.Println(canConstruct("aa", "ab"))
	fmt.Println(canConstruct("aa", "aab"))

}
