package main

import "fmt"

func main() {
	// iterating through a slice/array
	nums := []int{1, 2, 3}
	sum := 0
	for _, num := range nums {
		sum += num
	}
	fmt.Println("sum: ", sum)

	// range provides the index and value
	for i, num := range nums {
		fmt.Println("index: ", i, " value: ", num)
	}

	// iterating on a map provides key and value
	kvs := map[string]string{"a": "apple", "b": "ball", "c": "cat"}
	for k, v := range kvs {
		fmt.Printf("%s -> %s\n", k, v)
	}

	// iterating on a string provides index and rune
	for i, c := range "go" {
		fmt.Println(i, c)
	}
}
