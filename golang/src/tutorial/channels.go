package main

import "fmt"

func main() {
	// create a new channel with make
	// channels are typed by the values they convey
	messages := make(chan string)

	// send a value into a channel using channel <- syntax
	go func() { messages <- "ping" }()

	// recive a value from channel using <- channel syntax
	msg := <-messages

	fmt.Println(msg)
}
