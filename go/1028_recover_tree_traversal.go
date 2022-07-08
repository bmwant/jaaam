package main

import (
	"fmt"
	"strconv"
	"strings"
)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type deque []*TreeNode

func (d deque) PushBack(v *TreeNode) deque {
	return append(d, v)
}

func (d deque) PushFront(v *TreeNode) deque {
	// todo: reimplement
	return append(d, v)
}

func (d deque) PopBack() (deque, *TreeNode) {
	// todo: length check?
	l := len(d)
	return d[:l-1], d[l-1]
}

func (d deque) PopFront() (deque, *TreeNode) {
	// l := len(d)
	// todo: length check?
	return d[1:], d[0]
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func insert(node *TreeNode, val int, level int, curLevel int) bool {
	if curLevel > level {
		return false
	}
	// fmt.Printf("Loking to insert at %d: %d\n", level, curLevel)
	// find first vacant slot on this level
	if curLevel == level {
		if node.Left == nil {
			node.Left = &TreeNode{Val: val}
			return true
		}
		if node.Right == nil {
			node.Right = &TreeNode{Val: val}
			return true
		}
	}
	inserted := false
	// traverse tree further, this order is important
	if !inserted && node.Right != nil {
		inserted = insert(node.Right, val, level, curLevel+1)
	}

	if !inserted && node.Left != nil {
		inserted = insert(node.Left, val, level, curLevel+1)
	}

	return inserted
}

func runeVal(ch rune) int {
	val, _ := strconv.Atoi(fmt.Sprintf("%c", ch))
	return val
}

type Pair struct {
	Value int
	Level int
}

func extractPairs(t string) []Pair {
	result := make([]Pair, 0)
	isLevel := func(c rune) bool {
		return c != '-'
	}
	isNotLevel := func(c rune) bool {
		return c == '-'
	}
	levels := strings.FieldsFunc(t, isLevel)
	values := strings.FieldsFunc(t, isNotLevel)
	// insert root
	value, _ := strconv.Atoi(values[0])
	result = append(result, Pair{Value: value, Level: 0})
	for i, l := range levels {
		level := len(l)
		value, _ = strconv.Atoi(values[i+1])
		result = append(result, Pair{Value: value, Level: level})
	}

	for _, p := range result {
		fmt.Println(p.Value, p.Level)
	}
	return result
}

func recoverFromPreorder(traversal string) *TreeNode {
	pairs := extractPairs(traversal)
	var root TreeNode = TreeNode{Val: pairs[0].Value}
	for _, p := range pairs[1:] {
		insert(&root, p.Value, p.Level, 1)
	}
	return &root
}

func treeToList(t *TreeNode) (res []int) {
	dq := make(deque, 0)
	dq = dq.PushBack(t)
	var current *TreeNode
	for len(dq) > 0 {
		dq, current = dq.PopFront()
		// fmt.Println(current.Val)
		if current.Left != nil {
			dq = dq.PushBack(current.Left)
		}
		if current.Right != nil {
			dq = dq.PushBack(current.Right)
		}
		res = append(res, current.Val)
	}
	return res
}

func treeToPrint(t *TreeNode) (res []*TreeNode) {
	dq := make(deque, 0)
	dq = dq.PushBack(t)
	var current *TreeNode
	for len(dq) > 0 {
		dq, current = dq.PopFront()
		fmt.Println(current)
		res = append(res, current)
		if current == nil {
			continue
		}

		if current.Left == nil && current.Right == nil {
			continue
		}

		if current.Left != nil {
			dq = dq.PushBack(current.Left)
		} else {
			dq = dq.PushBack(nil)
		}
		if current.Right != nil {
			dq = dq.PushBack(current.Right)
		} else {
			dq = dq.PushBack(nil)
		}

	}
	for _, t := range res {
		if t == nil {
			fmt.Print("null ")
		} else {
			fmt.Printf("%d ", t.Val)
		}
	}
	fmt.Println("")
	return res
}

func main() {
	var t1, t2, t3 TreeNode
	t1.Val = 0
	t2.Val = 1
	t3.Val = 2
	t1.Left = &t2
	t2.Left = &t3
	// root := &t1
	// fmt.Println(treeToList(root))
	// head := recoverFromPreorder("1-2--3--4-5--6--7")
	// fmt.Println(treeToList(head)) // [1,2,5,3,4,6,7]
	// head = recoverFromPreorder("1-2--3---4-5--6---7")
	// fmt.Println(treeToList(head)) // [1,2,5,3,null,6,null,4,null,7]
	// head = recoverFromPreorder("1-401--349---90--88")
	// fmt.Println(treeToList(head)) // [1,401,null,349,88,90]

	head := recoverFromPreorder("1-2--3---4-5--6---7")
	treeToPrint(head) // [1,2,5,3,null,6,null,4,null,7]
}
