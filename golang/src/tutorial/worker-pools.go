package main

import "fmt"
import "time"

// will run concurrent instances of the worker
// worker will receive work on the jobs channel and
// post results on the result channel
func worker(id int, jobs <-chan int, results chan<- int) {
	for j := range jobs {
		fmt.Println("worker", id, "processing job", j)
		time.Sleep(time.Second)
		results <- j * 2
	}
}

func main() {
	// create channels for sending work and getting results
	jobs := make(chan int, 100)
	results := make(chan int, 100)

	// creates 3 workers, blocked until it gets jobs
	for w := 1; w <= 3; w++ {
		go worker(w, jobs, results)
	}

	// send 9 jobs and close the channel indicating all the work is sent
	for j := 1; j <= 9; j++ {
		jobs <- j
	}
	close(jobs)

	// collect the results for all the work
	for a := 1; a <= 9; a++ {
		<-results
	}
}
