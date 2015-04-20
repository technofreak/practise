package main

import "fmt"
import "time"

func main() {
	// pbulish jobs in job channel, publish in done when all jobs are run
	jobs := make(chan int, 5)
	done := make(chan bool)

	// special 2-value form of receive, more will be false if jobs has closed
	go func() {
		for {
			j, more := <-jobs
			if more {
				fmt.Println("recieved job", j)
			} else {
				fmt.Println("received all jobs")
				done <- true
				return
			}
		}
	}()

	for j := 1; j <= 3; j++ {
		jobs <- j
		fmt.Println("sent job", j)
		time.Sleep(time.Second * 1)
	}
	close(jobs)
	fmt.Println("sent all jobs")

	<-done
}
