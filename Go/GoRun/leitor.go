package main

import (
	"fmt"
	"sync"
	"time"
)


func insere(id int, startValue int, out chan<- int, wg *sync.WaitGroup) {
	defer wg.Done() 
	
	endValue := startValue + 9 

	for i := startValue; i <= endValue; i++ {
		fmt.Printf(" [Produtor %d] Enviando: %d\n", id, i)
		out <- i 
		time.Sleep(5 * time.Millisecond) 
	}
}

func ler(in <-chan int, done chan<- bool) {
	totalLido := 0
	for result := range in {
		fmt.Printf(" [Consumidor] Recebido: %d\n", result)
		totalLido++
	}
	
	fmt.Printf("\n [Consumidor] Fim da leitura. Total lido: %d\n", totalLido)
	done <- true 
}

func main() {
	fmt.Println("Iniciando produtores e consumidor.")

	ch1 := make(chan int)

	var wg sync.WaitGroup

	done := make(chan bool)

	go ler(ch1, done)

	wg.Add(2)

	go insere(1, 1, ch1, &wg)   
	go insere(2, 11, ch1, &wg) 

	go func() {
		wg.Wait()
		close(ch1)
		fmt.Println("\n *** Canal Fechado (Produtores Finalizados) ***")
	}()

	<-done

	fmt.Println("\nFim do programa. Todos os 20 dados foram processados.")
}
