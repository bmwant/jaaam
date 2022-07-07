package main

import (
	"io"
	"os"
	"strings"
	"unicode"
)

type rot13Reader struct {
	r io.Reader
}

func rot13(b byte) byte {
	var a, z byte = 'a', 'z'
	if !unicode.IsLetter(rune(b)) {
		return b
	}
	if unicode.IsUpper(rune(b)) {
		a, z = 'A', 'Z'
	}
	return (b-a+13)%(z-a+1) + a
}

func (r rot13Reader) Read(arr []byte) (int, error) {
	n, err := r.r.Read(arr)
	for i := 0; i < n; i++ {
		arr[i] = rot13(arr[i])
	}
	return n, err
}

func main() {
	s := strings.NewReader("Lbh penpxrq gur pbqr!")
	r := rot13Reader{s}
	io.Copy(os.Stdout, &r)
}
