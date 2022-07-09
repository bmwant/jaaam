package main

import "fmt"

type Person struct {
	Start int
}

func (p Person) canTalk(n int, delay int) bool {
	if n-p.Start >= delay {
		return true
	}
	return false
}

func (p Person) forgot(n int, forget int) bool {
	if n-p.Start >= forget {
		return true
	}
	return false
}

func main() {
	days := 20
	delay := 2
	forget := 7
	var people []Person = []Person{Person{Start: 0}}
	p1 := make([]int, 0)
	f1 := make([]int, 0)
	s1 := make([]int, 0)
	w1 := make([]int, 0)

	for d := 0; d < days; d++ {
		forgot := 0
		canTalk := 0
		waiting := 0
		knows := make([]Person, 0)
		for _, p := range people {
			if !p.forgot(d, forget) {
				knows = append(knows, p)
				if p.canTalk(d, delay) {
					knows = append(knows, Person{Start: d})
					canTalk++
				} else {
					waiting++
				}
			} else {
				forgot++
			}
		}
		p1 = append(p1, len(knows))
		f1 = append(f1, forgot)
		s1 = append(s1, canTalk)
		w1 = append(w1, waiting)
		people = knows
		// fmt.Printf("On a day %d: %d people know\n", d, len(people))
		// fmt.Printf("forgot %d: shares: %d, waiting: %d\n\n", forgot, canTalk, waiting)
	}
	fmt.Print("i:")
	for i := 0; i < len(p1); i++ {
		fmt.Printf("%2d ", i)
	}
	fmt.Println()
	pr := func(s string, p []int) {
		fmt.Print(s)
		for _, v := range p {
			fmt.Printf("%2d ", v)
		}
		fmt.Println()
	}
	pr("p:", p1)
	pr("f:", f1)
	pr("s:", s1)
	// pr("w:", w1)
}
