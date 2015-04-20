package main

import "fmt"
import "math"

//interfaces are named collection of method signatures
// basic interface for geometric shapes
type geometry interface {
	area() float64
	perim() float64
}

// square and circle types
type square struct {
	width, height float64
}

type circle struct {
	radius float64
}

// implement all the methods of the interface
func (s square) area() float64 {
	return s.width * s.height
}

func (s square) perim() float64 {
	return 2*s.width + 2*s.height
}

func (c circle) area() float64 {
	return math.Pi * c.radius * c.radius
}

func (c circle) perim() float64 {
	return 2 * math.Pi * c.radius
}

func measure(g geometry) {
	fmt.Println(g)
	fmt.Println(g.area())
	fmt.Println(g.perim())
}

func main() {
	s := square{width: 5, height: 10}
	c := circle{radius: 5}
	measure(s)
	measure(c)
}
