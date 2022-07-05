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

func middleNode(head *ListNode) *ListNode {
	counter := 1
	var middle *ListNode
	track := head
	middle = head
	for track != nil {
		if counter%2 == 0 {
			middle = middle.Next
		}
		// fmt.Println(track.Val, track.Next)
		track = track.Next
		counter += 1
	}
	return middle
}

func main() {
	var n1, n2, n3, n4, n5 ListNode
	n1.Val = 1
	n2.Val = 2
	n3.Val = 3
	n4.Val = 4
	n5.Val = 5
	n1.Next = &n2
	n2.Next = &n3
	n3.Next = &n4
	n4.Next = &n5
	// fmt.Println(&n1, n1.Next, n1.Next.Next)
	var head *ListNode = &n1
	fmt.Println(middleNode(head))
}
