package main

import "fmt"

func f(from string, j int) {
	for i := 0; i < j; i++ {
		fmt.Println(from, " : ", i)
	}
}

func main() {
	f("direct", 3)

	go f("goroutine", 10)

	go func(msg string) {
		fmt.Println(msg)
	}("going")

	var input string
	fmt.Scanln(&input)
	fmt.Println("done")
}
