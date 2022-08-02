package main

import "fmt"

func getMin(arr []int) int {
	for index, value := range arr {
		if value == 0 {
			return index + 1
		}
	}
	return -1
}

func getMax(arr []int) int {
	for i := len(arr) - 1; i >= 0; i-- {
		if arr[i] == 0 {
			return i + 1
		}
	}
	return -1
}

func newState(state string, used int) string {
	ns := ""
	for index, val := range state {
		if index+1 == used {
			ns += "1"
		} else {
			ns += string(val)
		}
	}
	return ns
}

func canIWin2(maxChoosableInteger int, desiredTotal int) bool {
	cache := make(map[string]bool)
	var win func(state string, sum int) bool
	win = func(state string, sum int) bool {
		fmt.Println("Solving", state, "for", sum)
		val, ok := cache[state]
		if ok {
			return val
		}
		for index, val := range state {
			if val == '0' && index+1 >= sum {
				cache[state] = true
				return true
			}
		}
		for index, val := range state {
			if val == '0' {
				ns := newState(state, index+1)
				subsolution := win(ns, sum-index-1)
				// Second player can win from a sub state
				if subsolution == true {
					// if at least one solution is false then we cannot FORCE a win?
					cache[state] = true
					return true
				}
			}
		}
		cache[state] = false
		return false
	}
	initialState := ""
	for i := 0; i < maxChoosableInteger; i++ {
		initialState += "0"
	}
	return win(initialState, desiredTotal)
}

func makeState(choices []int) string {
	return fmt.Sprintf("%v", choices)
}

func makeChoices(choices []int, value int) []int {
	var newChoices = make([]int, len(choices)-1)
	for i, j := 0, 0; j < len(choices); j++ {
		val := choices[j]
		if val != value {
			newChoices[i] = val
			i++
		}
	}
	return newChoices
}

func copyMap(original map[int]bool) map[int]bool {
	result := make(map[int]bool)
	for k, v := range original {
		result[k] = v
	}
	return result
}
func canIWin(maxChoosableInteger int, desiredTotal int) bool {
	seen := make(map[string]bool)
	var choices = map[int]bool{}
	for i := 1; i <= maxChoosableInteger; i++ {
		choices[i] = false
	}
	var f func(choices map[int]bool, remainder int) bool
	f = func(choices map[int]bool, remainder int) bool {
		state := fmt.Sprintf("%v", choices)
		v, ok := seen[state]
		if ok {
			return v
		}
		for k, v := range choices {
			if v == false && k >= remainder {
				return true
			}
		}

		for k, v := range choices {
			if v == false {
				// newChoices := copyMap(choices)
				// newChoices[k] = true
				choices[k] = true
				if !f(choices, remainder-k) {
					seen[state] = true
					return true
				}
				choices[k] = false
			}
		}
		seen[state] = false
		return false
	}
	return f(choices, desiredTotal)

}
func canIWin1(maxChoosableInteger int, desiredTotal int) bool {
	seen := make(map[string]bool)
	var win func([]int, int) bool
	cached := func(choices []int, remainder int) bool {
		state := fmt.Sprintf("%v", choices)
		v, ok := seen[state]
		if ok {
			return v
		}
		result := win(choices, remainder)
		seen[state] = result
		return result
	}
	win = func(choices []int, remainder int) bool {
		if len(choices) == 0 {
			return false
		}
		if choices[len(choices)-1] >= remainder {
			return true
		}

		// we cannot win in this step, so consider all the other options
		for _, v := range choices {
			newChoices := makeChoices(choices, v)
			// fmt.Println("New choices are", newChoices)
			// fmt.Println("New state is", newState)
			if !cached(newChoices, remainder-v) {
				// fmt.Println("We can force win from", newState, "Choosing", v, "Left", remainder-v)
				return true
			}
		}
		return false
	}
	var initialChoices = []int{}
	ss := 0
	for c := 1; c <= maxChoosableInteger; c++ {
		initialChoices = append(initialChoices, c)
		ss += c
		// if ss >= desiredTotal {
		// break
		// }
	}
	sumChoices := (maxChoosableInteger + 1) * maxChoosableInteger / 2
	if sumChoices < desiredTotal {
		return false
	}
	if sumChoices == desiredTotal {
		return maxChoosableInteger%2 != 0
	}
	result := cached(initialChoices, desiredTotal)
	// fmt.Println(seen)
	return result
}

func main() {
	fmt.Println(canIWin(10, 0))  // true
	fmt.Println(canIWin(10, 1))  // true
	fmt.Println(canIWin(10, 11)) // false
	fmt.Println(canIWin(10, 40)) // false
	fmt.Println(canIWin(4, 6))   // true
	// fmt.Println(canIWin(18, 188)) // true
	// fmt.Println(canIWin(5, 50))   // true
	// fmt.Println(canIWin(20, 189)) // true
	// fmt.Println(canIWin(20, 152)) // true
	// fmt.Println(canIWin(4, 5))    // true
}
