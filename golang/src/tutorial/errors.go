package main

import "errors"
import "fmt"

// by convention error is the last of the return value and have type error
func f1(arg int) (int, error) {
	if arg == 42 {
		// errors.New constructs a basic error value with given message
		return -1, errors.New("can't intake 42")
	}
	// a nil value indicates no error
	return arg + 1, nil
}

// custom error types can be implemented by having Error() method
type argError struct {
	arg  int
	prob string
}

func (e *argError) Error() string {
	return fmt.Sprintf("%d - %s", e.arg, e.prob)
}

func f2(arg int) (int, error) {
	if arg == 42 {
		return -1, &argError{arg, "can't intake 42"}
	}
	return arg + 1, nil
}

// test the functions
func main() {
	for _, i := range []int{7, 42} {
		if r, e := f1(i); e != nil {
			fmt.Println("f1 failed:", e)
		} else {
			fmt.Println("f1 worked:", r)
		}
	}

	for _, i := range []int{7, 42} {
		if r, e := f2(i); e != nil {
			fmt.Println("f2 failed:", e)
		} else {
			fmt.Println("f2 worked:", r)
		}
	}

	// to programatically use data in a custom error, get the error as an instance
	// of the custom error type via assertion
	_, e := f2(42)
	if ae, ok := e.(*argError); ok {
		fmt.Println(ae.arg)
		fmt.Println(ae.prob)
	}
}
