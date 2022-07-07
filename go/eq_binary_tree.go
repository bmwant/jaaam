package main

import (
	"fmt"

	"golang.org/x/tour/tree"
)

// Walk walks the tree t sending all values
// from the tree to the channel ch.
func Walk(t *tree.Tree, ch chan int) {
	ch <- t.Value
	if t.Left != nil {
		Walk(t.Left, ch)
	}
	if t.Right != nil {
		Walk(t.Right, ch)
	}
}

// Same determines whether the trees
// t1 and t2 contain the same values.
func Same(t1, t2 *tree.Tree) bool {
	if t1.Value != t2.Value {
		return false
	}
	leftSame, rightSame := true, true
	if t1.Left != nil && t2.Left != nil {
		leftSame = Same(t1.Left, t2.Left)
	}
	if t1.Right != nil && t2.Right != nil {
		rightSame = Same(t1.Right, t2.Right)
	}
	return leftSame && rightSame
}

func main() {
	ch := make(chan int)
	t1 := tree.New(1)
	t2 := tree.New(1)
	fmt.Println(t1)
	fmt.Println(t2)
	go func() {
		defer close(ch)
		Walk(t1, ch)
	}()
	for i := range ch {
		fmt.Println(i)
	}
	// for i := 0; i < 10; i++ {
	// 	fmt.Println(<-ch)
	// }
	fmt.Println(Same(t1, t2))
	fmt.Println(Same(t1, t1))
	fmt.Println(Same(t2, t2))
}
