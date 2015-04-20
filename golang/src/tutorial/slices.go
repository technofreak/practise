package main

import "fmt"

func main() {
	// slices are typed by the elements they contain
	// create empty slice with make
	s := make([]string, 3)
	fmt.Println("Init: ", s)

	s[0] = "a"
	s[1] = "b"
	s[2] = "c"
	fmt.Println("Set: ", s)
	fmt.Println("Get: ", s[2])

	fmt.Println("len: ", len(s))

	// append returns new slice
	s = append(s, "d")
	s = append(s, "e", "f")
	fmt.Println("Append: ", s)

	// slice can be copied using copy
	c := make([]string, len(s))
	copy(c, s)
	fmt.Println("Copy: ", c)

	// slice can be sliced using [low:high]
	l := s[2:5]
	fmt.Println("slice 1: ", l)

	l = s[:5]
	fmt.Println("slice 2: ", l)

	l = s[2:]
	fmt.Println("slice 3: ", l)

	// declare and init slice in a single line
	t := []string{"g", "h", "i"}
	fmt.Println("Declare: ", t)

	// two dimensional slice whose inner length can vary
	twoD := make([][]int, 3)
	for i := 0; i < 3; i++ {
		innerLen := i + 1
		twoD[i] = make([]int, innerLen)
		for j := 0; j < innerLen; j++ {
			twoD[i][j] = i + j
		}
	}
	fmt.Println("2d: ", twoD)
}
