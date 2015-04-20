package main

import "fmt"

func plus(a int, b int) int {
	return a + b
}

func plusPlus(a, b, c int) int {
	return a + b + c
}

// multiple return values
// generally used for result and error pair from functions
func vals() (int, int) {
	return 1, 0
}

func main() {
	res := plus(1, 2)
	fmt.Println("1+2 = ", res)

	res = plusPlus(1, 2, 3)
	fmt.Println("1+2+3 = ", res)

	a, b := vals()
	fmt.Println(a)
	fmt.Println(b)

	// _ can be used as blank identifier
	_, c := vals()
	fmt.Println(c)
}
