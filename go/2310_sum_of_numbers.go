package main

import (
	"fmt"
	"math"
)

func solvea(numS, kS, lS int) int {
	cache := map[int]int{}
	var s func(a, b, c int) int
	s = func(num, k, l int) int {
		minSet := math.MaxInt
		if num == 0 {
			return l
		}
		res, ok := cache[num]
		if ok {
			// fmt.Println("Cache hit", num, res)
			return res
		}
		for i := 0; ; i++ {
			currentUnit := 10*i + k
			// fmt.Println("current unit", currentUnit)
			if currentUnit == 0 {
				continue
			}
			if currentUnit > num {
				break
			}
			nextNum := num - currentUnit
			res, ok = cache[nextNum]
			curSet := res
			if !ok {
				curSet = s(nextNum, k, l+1)
				cache[nextNum] = curSet
			}
			if curSet < minSet {
				minSet = curSet

				_, ok = cache[currentUnit]
				if !ok {
					cache[currentUnit] = curSet
				}
			}
		}
		return minSet
	}
	result := s(numS, kS, lS)
	fmt.Println(cache)
	return result
}

func solve(num, k int) int {
	if num == 0 {
		return 0
	}
	if num%10 == k {
		return 1
	}
	minSol := math.MaxInt
	for i := 0; ; i++ {
		cLeft := 10*i + k
		if cLeft == 0 {
			continue
		}
		if cLeft > num {
			break
		}
		cRight := num - cLeft
		solLeft := solve(cLeft, k)
		solRight := solve(cRight, k)
		currentSol := math.MaxInt
		if solLeft != math.MaxInt && solRight != math.MaxInt {
			currentSol = solLeft + solRight
		}
		if currentSol < minSol {
			minSol = currentSol
		}
	}
	return minSol
}

func minimumNumbers(num int, k int) int {
	// cache := make(map[int]int)
	result := solve(num, k)
	if result == math.MaxInt {
		return -1
	}
	return result
}

func main() {
	fmt.Println(minimumNumbers(58, 9))   // 2
	fmt.Println(minimumNumbers(37, 2))   // -1
	fmt.Println(minimumNumbers(0, 7))    // 0
	fmt.Println(minimumNumbers(10, 7))   // -1
	fmt.Println(minimumNumbers(3000, 0)) // 1
	fmt.Println(minimumNumbers(3000, 1)) // 3000
	fmt.Println(minimumNumbers(20, 1))   // 10
}
