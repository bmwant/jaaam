package main

import "fmt"

func sum(arr []int) (res int) {
	for _, value := range arr {
		res += value
	}
	return
}

func peopleAwareOfSecret2(n int, delay int, forget int) int {
	f := make([]int, n)
	mod := int(10e9 + 7)
	f[0] = 1
	for i := delay; i < n; i++ {
		start := i - forget + 1
		if start < 0 {
			start = 0
		}
		end := i - delay + 1
		sharedTo := sum(f[start:end]) % mod
		// fmt.Printf("index: %d, start: %d, end: %d, sum: %d\n", i, start, end, sharedTo)

		f[i] = sharedTo
		// fmt.Println(f, f[start:end]
	}
	return sum(f[n-forget:]) % mod
}

func peopleAwareOfSecret(n int, delay int, forget int) int {
	f := make([]int, forget)
	f[0] = 1
	fmt.Println("day 1", f, "shared", 0)
	for i := 1; i < n; i++ {
		// fmt.Println(i+1, "shared to", sm)
		f = append([]int{0}, f...)
		sharedTo := sum(f[delay:forget])
		f[0] = sharedTo
		fmt.Println("day", i+1, f, "shared", sharedTo)
		// fmt.Println(f)
		// drop those who forgot
		// f = f[:len(f)-1]
	}
	return sum(f[:forget]) % int(10e9+7)
}

func main() {
	// fmt.Println(peopleAwareOfSecret2(6, 2, 4)) // 5
	fmt.Println(peopleAwareOfSecret2(20, 2, 4)) // 5
	// fmt.Println(peopleAwareOfSecret2(4, 1, 3)) // 6
	fmt.Println(peopleAwareOfSecret2(684, 18, 496)) // 653668527
}
