package main

import "time"
import "fmt"

func main() {

	// timeout of 1 sec, task is 2 seconds, will timeout
	c1 := make(chan string)
	go func() {
		time.Sleep(time.Second * 2)
		c1 <- "result 1"
	}()

	select {
	case res := <-c1:
		fmt.Println(res)
	case <-time.After(time.Second * 1):
		fmt.Println("timeout 1")
	}

	// timeout of 3 seconds, task is 1 second, will not timeout
	c2 := make(chan string)
	go func() {
		time.Sleep(time.Second * 1)
		c2 <- "result 2"
	}()

	select {
	case res := <-c2:
		fmt.Println(res)
	case <-time.After(time.Second * 3):
		fmt.Println("timeout 2")
	}
}
