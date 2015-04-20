package main

import "fmt"

func main() {
	// channel of string with buffering upto 2 values
	messages := make(chan string, 2)

	// can send upto 2 values with a corresponding concurrent receiver
	messages <- "buffered"
	messages <- "channel"

	// receive values from channel
	fmt.Println(<-messages)
	fmt.Println(<-messages)
}
