package main

import "fmt"

// Methods defined on Struct type
type rect struct {
	width, height int
}

// area method has receiver type of *rect (pass by reference / pointer)
func (r *rect) area() int {
	return r.width * r.height
}

// perim method has receiver type of rect (pass by value)
func (r rect) perim() int {
	return 2*r.width + 2*r.height
}

func main() {
	r := rect{width: 10, height: 5}

	fmt.Println("area:", r.area())
	fmt.Println("perim:", r.perim())

	// auto converts between values and pointers
	// use pointer receiver types to avoid copying or mutate receiving struct
	rp := &r
	fmt.Println("area:", rp.area())
	fmt.Println("perim:", rp.perim())
}
