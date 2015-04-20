package main

import "fmt"

// person struct
type person struct {
	name string
	age  int
}

func main() {
	// a new person struct
	fmt.Println(person{"Bob", 30})

	// name fields while initializing a struct
	fmt.Println(person{name: "Alice", age: 18})

	// omitted fields assume zero value
	fmt.Println(person{name: "Fred"})

	// & yields pointer to the struct
	fmt.Println(&person{name: "Aron", age: 40})

	// access struct fields with a dot
	s := person{name: "Sean", age: 21}
	fmt.Println(s.name)

	// dots can also be used on struct pointers (auto deferenced)
	sp := &s
	fmt.Println(sp.age)

	// structs are mutable
	sp.age = 51
	fmt.Println(sp.age)
}
