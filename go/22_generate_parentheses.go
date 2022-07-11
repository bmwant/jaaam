package main

import (
	"fmt"
)

func generateParenthesis(n int) []string {
	res := make([]string, 0)
	var bt func(s string, left, right int)
	bt = func(s string, left, right int) {
		if len(s) == 2*n {
			res = append(res, s)
			return
		}
		if left < n {
			bt(s+"(", left+1, right)
		}
		if right < left {
			bt(s+")", left, right+1)
		}
	}
	bt("", 0, 0)
	return res
}

func main() {
	// ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
	// [()(()()) ()()(()) (()(())) ()(())() ((()))() ((())()) ()()()() (()()()) (()())() ()((())) (((()))) (())()() ((()()))]
	// res := generateParenthesis(4)
	fmt.Println(generateParenthesis(3)) // ["((()))","(()())","(())()","()(())","()()()"]
	// fmt.Println(generateParenthesis(2))
	// fmt.Println(generateParenthesis(1)) // ["()"]
}
