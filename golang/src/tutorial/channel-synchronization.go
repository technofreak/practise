package main

import "fmt"
import "time"

// this func will run in a goroutine
// done channel will be used to notify another goroutine
func worker(done chan bool) {
	fmt.Println("working...")
	time.Sleep(time.Second)
	fmt.Println("done")

	// notify the channel that work is done
	done <- true
}

func main() {
	// channel to notify
	done := make(chan bool, 1)
	// start the worker goroutine passing it the channel to notify
	go worker(done)

	// block until we receive notification from worker on the channel
	<-done
}
