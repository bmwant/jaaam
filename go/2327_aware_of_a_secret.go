package main

import "fmt"

func sum(arr []int) (res int) {
	for _, value := range arr {
		res += value
	}
	return
}

func peopleAwareOfSecret(n int, delay int, forget int) int {
	f := make([]int, forget)
	f[0] = 1
	// fmt.Printf("index: %d, start: %d, end: %d\n", i, start, end)
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
	fmt.Println(peopleAwareOfSecret(6, 2, 4)) // 5
	// fmt.Println(peopleAwareOfSecret(4, 1, 3)) // 6
}
