package main

import (
	"fmt"
	"time"
)

func main() {

	// basic switch
	i := 2
	fmt.Println("write ", i, " as ")
	switch i {
	case 1:
		fmt.Println("one")
	case 2:
		fmt.Println("two")
	case 3:
		fmt.Println("three")
	}

	// multiple expressions in same case statement
	switch time.Now().Weekday() {
	case time.Saturday, time.Sunday:
		fmt.Println("it's the weekend")
	default:
		fmt.Println("it's a weekday")
	}

	// switch without an expression is equivalent to if/else
	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("it's befone noon")
	default:
		fmt.Println("it's after noon")
	}
}
