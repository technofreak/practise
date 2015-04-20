package main

import "fmt"

func main() {

	queue := make(chan string, 2)
	queue <- "one"
	queue <- "two"
	// close would terminate the iteration
	close(queue)

	// range iterates each element as it's received from queue
	for elem := range queue {
		fmt.Println(elem)
	}
}
