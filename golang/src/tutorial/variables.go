package main

import "fmt"

func main() {
	// delcaring a variable
	var a string = "initial"
	fmt.Println(a)

	// multiple delcations
	var b, c int = 1, 2
	fmt.Println(b, c)

	// go will infer type of initalized vars
	var d = true
	fmt.Println(d)

	// zero-valued variables
	var e int
	fmt.Println(e)

	// shorthand syntax
	f := "short"
	fmt.Println(f)
}
