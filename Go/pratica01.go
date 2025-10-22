package main

import (
	"fmt"
)

func insere1(out chan<- int) {
	for i := 0; i <= 10; i++ {
		out <- i
	}
}

func insere2(out chan<- int) {
	for i := 11; i <= 20; i++ {
		out <- i
	}
	defer close(out)
}

func ler(out <-chan int) {
	for finalResult := range out {
		fmt.Print(finalResult)
	}
}

func main() {

	ch1 := make(chan int)

	go insere1(ch1)
	go insere2(ch1)

	ler(ch1)

	fmt.Println("\nFim programa. Todos os dados foram processados.")
}
