package main

import "fmt"

func main() {

	// basic if else
	if 7%2 == 0 {
		fmt.Println("7 is even")
	} else {
		fmt.Println("7 is odd")
	}

	// if without else
	if 8%4 == 0 {
		fmt.Println("8 is divisible by 4")
	}

	// a statement preceeding the conditional
	if num := 9; num < 0 {
		fmt.Println(num, "is negative")
	} else if num < 10 {
		fmt.Println(num, "is of single digit")
	} else {
		fmt.Println(num, "is of multiple digits")
	}

	fmt.Println("There is no terninary if in Go.")
}
