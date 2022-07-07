package main

import (
	"fmt"
)

type ErrNegativeSqrt float64

func Sqrt(x ErrNegativeSqrt) (float64, error) {
	if x < 0 {
		return 0, x
	}

	z := ErrNegativeSqrt(1.0)
	for i := 0; i < 10; i++ {
		z -= (z*z - x) / (2 * z)
	}
	return float64(z), nil
}

func (e ErrNegativeSqrt) Error() string {
	return fmt.Sprintf("Cannot sqrt negative number %f", e)
}

func main() {
	r, err := Sqrt(2)
	if err == nil {
		fmt.Println(r)
	} else {
		fmt.Println(err)
	}
	fmt.Println(Sqrt(-2))
}
