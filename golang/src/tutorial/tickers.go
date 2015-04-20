package main

import "time"
import "fmt"

func main() {
	// ticker are used to run things at specific intervals, until we stop
	ticker := time.NewTicker(time.Millisecond * 500)
	go func() {
		for t := range ticker.C {
			fmt.Println("Tick at", t)
		}
	}()

	// wait for 1500 milliseconds before stopping the ticker
	time.Sleep(time.Millisecond * 1500)
	ticker.Stop()
	fmt.Println("ticker stopped")
}
