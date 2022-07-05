package main

import (
	"fmt"
	"sort"
)

func kWeakestRows(mat [][]int, k int) []int {
	// var pw = make(map[int]int)
	var powers = make([]int, len(mat))
	type kv struct {
		Key   int
		Value int
	}

	var ss []kv

	for i, row := range mat {
		rowSum := 0
		for _, a := range row {
			rowSum += a
		}
		ss = append(ss, kv{i, rowSum})
	}
	// fmt.Println(ss)

	sort.Slice(ss, func(i, j int) bool {
		return ss[i].Value < ss[j].Value || (ss[i].Value == ss[j].Value && ss[i].Key < ss[j].Key)
	})

	for i, kv := range ss {
		fmt.Printf("%d, %d\n", kv.Key, kv.Value)
		powers[i] = kv.Key
	}
	return powers[:k]
}

func main() {
	mat := [][]int{
		{1, 1, 0, 0, 0},
		{1, 1, 1, 1, 0},
		{1, 0, 0, 0, 0},
		{1, 1, 0, 0, 0},
		{1, 1, 1, 1, 1},
	}

	mat2 := [][]int{
		{1, 0, 0, 0},
		{1, 1, 1, 1},
		{1, 0, 0, 0},
		{1, 0, 0, 0},
	}

	mat3 := [][]int{
		{1, 1, 0},
		{1, 1, 0},
		{1, 1, 1},
		{1, 1, 1},
		{0, 0, 0},
		{1, 1, 1},
		{1, 0, 0},
	}
	fmt.Println(kWeakestRows(mat, 3))  // [2, 0, 3]
	fmt.Println(kWeakestRows(mat2, 2)) // [0, 2]
	fmt.Println(kWeakestRows(mat3, 6)) // [4,6,0,1,2,3]
}
