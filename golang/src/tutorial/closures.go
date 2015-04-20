package main

import "fmt"

func intSeq() func() int {
	i := 0
	return func() int {
		i += 1
		return i
	}
}

func main() {
	// nextInt will receive the closure
	nextInt := intSeq()

	// calling the closure
	fmt.Println(nextInt())
	fmt.Println(nextInt())
	fmt.Println(nextInt())

	// create a new closure and test
	testInt := intSeq()
	fmt.Println(testInt())
}
