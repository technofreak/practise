package main

import "fmt"
import "math"

const s string = "constant"

func main() {
	fmt.Println(s)

	const n = 500000000

	const d = 3e20 / n
	fmt.Println(d)

	// numeric constant has no type until an explicit cast
	fmt.Println(int64(d))

	// number can be given a type based on the context
	// math.Sin expects a float64
	fmt.Println(math.Sin(n))
}
