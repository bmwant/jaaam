package main

import "fmt"

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
type ListNode struct {
	Val  int
	Next *ListNode
}

func isPalindrome(head *ListNode) bool {
	// slow, fast := head, head
	// rev := head
	arr := []int{}
	p := head
	for p != nil {
		// fmt.Println(slow.Val, fast.Val)
		arr = append(arr, p.Val)
		p = p.Next
	}

	for i := range arr {
		// fmt.Println(arr[i])
		if arr[i] != arr[len(arr)-i-1] {
			return false
		}
		// rev = rev.Next
	}
	return true
}

func main() {
	var n1, n2, n3, n4 ListNode
	n1.Val = 1
	n2.Val = 2
	n3.Val = 2
	n4.Val = 1
	n1.Next = &n2
	n2.Next = &n3
	n3.Next = &n4
	// fmt.Println(&n1, n1.Next, n1.Next.Next)
	var head *ListNode = &n1
	fmt.Println(isPalindrome(head))
}
