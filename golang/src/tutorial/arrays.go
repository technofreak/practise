package main

import "fmt"

func main() {

	// an array to hold 5 ints
	// type of element and length are part of array's type
	// by default an array is zero valued
	var a [5]int
	fmt.Println("init: ", a)

	// set a value using array[index] = value
	// get a value using array[index]
	a[4] = 100
	fmt.Println("set: ", a)
	fmt.Println("get: ", a[4])

	// builtin len returns length of an array
	fmt.Println("len: ", len(a))

	// declare and initialize an array in single line
	b := [5]int{1, 2, 3, 4, 5}
	fmt.Println("decl: ", b)

	// array types of one dimensional
	// compose types to build multi-dimensional arrays
	var twoD [2][3]int
	for i := 0; i < 2; i++ {
		for j := 0; j < 3; j++ {
			twoD[i][j] = i + j
		}
	}
	fmt.Println("2D: ", twoD)
}
