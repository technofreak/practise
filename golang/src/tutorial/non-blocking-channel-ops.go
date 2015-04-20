package main

import "fmt"

func main() {
	messages := make(chan string)
	signals := make(chan bool)

	// select with a default clause can be used to implement
	// non-blocking sneds, receives and multi-way selects
	select {
	case msg := <-messages:
		fmt.Println("received message", msg)
	default:
		fmt.Println("no message received")
	}

	msg := "hi"
	select {
	case messages <- msg:
		fmt.Println("sent message", msg)
	default:
		fmt.Println("no message sent")
	}

	select {
	case msg := <-messages:
		fmt.Println("received msg", msg)
	case sig := <-signals:
		fmt.Println("received sig", sig)
	default:
		fmt.Println("no activity")
	}
}
