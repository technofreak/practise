package main

import "fmt"

func main() {
	// basic for loop
	i := 1
	for i <= 3 {
		fmt.Println(i)
		i = i + 1
	}

	// typical for loop
	for j := 5; j <= 7; j++ {
		fmt.Println(j)
	}

	// infinite loop
	for {
		fmt.Println("looping")
		break
	}
}
