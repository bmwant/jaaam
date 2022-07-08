package ds

import "errors"

// Stack
type stack []*TreeNode

func (s stack) Push(v *TreeNode) stack {
	return append(s, v)
}

func (s stack) Pop() (stack, *TreeNode, error) {
	l := len(s)
	if l == 0 {
		return s, nil, errors.New("Stack is empty")
	}
	return s[:l-1], s[l-1], nil
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// Pair
type Pair struct {
	Value int
	Count int
}

// Deque
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
