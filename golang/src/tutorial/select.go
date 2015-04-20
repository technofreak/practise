package main

import "fmt"
import "time"

func main() {
	// make two channels to receive simultanelously
	c1 := make(chan string)
	c2 := make(chan string)

	// execute concurrent goroutines with blocking operation to each channel
	go func() {
		time.Sleep(time.Second * 1)
		c1 <- "one"
	}()
	go func() {
		time.Sleep(time.Second * 2)
		c2 <- "two"
	}()

	// use select to avail both of the values simulataneously
	for i := 0; i < 2; i++ {
		select {
		case msg1 := <-c1:
			fmt.Println("received", msg1)
		case msg2 := <-c2:
			fmt.Println("received", msg2)
		}
	}
}
