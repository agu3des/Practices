package main

import (
	"fmt"
)

// worker reads from channel jobs’ and send results to the channel ’results’.
func worker(id int, jobs <-chan int, results chan<- int) {
	for n := range jobs {
		results <- n * n
	}
}

func main() {
	// input channel ( jobs ) and output channel ( results )
	jobs := make(chan int)    // unbuffered
	results := make(chan int) // unbuffered

	// Start worker in a Goroutine and close channel results ’ in the end
	go func() {
		worker(1, jobs, results)
		close(results) // sinaliza que Ã£no Ã¡haver mais resultados
	}()

	// Producer : sends 1..5 and closes jobs ’ in the end
	go func() {
		for i := 1; i <= 5; i++ {
			jobs <- i
		}
		close(jobs)
	}()

	// Consumer : reads all the results until the channel is closed
	for r := range results {
		fmt.Println(" resultado :", r)
	}

	fmt.Println(" fim ")
}
