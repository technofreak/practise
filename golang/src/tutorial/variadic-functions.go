package main

import "fmt"

// Variadic Function is a function that can accept an arbitrary number of args

// takes an arbitrary number of ints as arguments
func sum(nums ...int) {
	fmt.Println("nums: ", nums)
	total := 0
	for _, num := range nums {
		total += num
	}
	fmt.Println("total: ", total)
}

func main() {

	sum(1, 2)
	sum(1, 2, 3)

	// using slice as args
	nums := []int{1, 3, 5, 7, 9}
	sum(nums...)

}
