package main

import "fmt"

func main() {
	// maps are associative arrays or hashmaps or dictionaries
	// use make(map[key-type]val-type) to create a map
	m := make(map[string]int)

	// set using name[key] = value
	m["k1"] = 1
	m["k2"] = 20

	fmt.Println("map: ", m)

	// get using name[key]
	fmt.Println("get: ", m["k2"])

	// built-in len returns len of key-val pairs
	fmt.Println("len: ", len(m))

	// built-in delete removes key-val pair
	delete(m, "k2")
	fmt.Println("delete: ", m)

	// an optional 2nd return val in get call indicates if key was present in mao
	_, pres := m["k2"]
	fmt.Println("present: ", pres)

	// delcare and initialize map in the same line
	n := map[string]int{"one": 1, "two": 2}
	fmt.Println("decl: ", n)

}
