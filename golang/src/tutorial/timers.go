package main

import "time"
import "fmt"

func main() {
	// timers represent a single event in future
	// tell timer how long we want to wait
	// timer provides a channel that will be notified after the wait
	timer1 := time.NewTimer(time.Second * 2)
	// timer.C blocks on timer's channel c untils it receives the value
	<-timer1.C
	fmt.Println("timer 1 expired")

	// timer can be cancelled before it expires, using .Stop()
	timer2 := time.NewTimer(time.Second)
	go func() {
		<-timer2.C
		fmt.Println("timer 2 expired")
	}()
	stop2 := timer2.Stop()
	if stop2 {
		fmt.Println("timer 2 stopped")
	}
}
