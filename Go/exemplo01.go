package main

import (
	"fmt"
	"time"
)

// produtor envia dados para o channel de saida (out)
func produtor(out chan<- int) {
	defer close(out) // Garante que o channel sera fechado ao final

	for i := 1; i <= 5; i++ {
		fmt.Printf(" [Produtor] Enviando: %d\n", i)
		out <- i // Envia o numero para o channel
		time.Sleep(100 * time.Millisecond)
	}
}

// intermediario (worker) le do 'in', processa e envia para o 'out'
func intermediario(in <-chan int, out chan<- int) {
	// A rotina intermediaria so deve fechar seu 'out'
	// DEPOIS que ele leu TUDO do 'in'.
	defer close(out)

	// Laco para ler todos os valores ate o channel 'in' ser fechado
	for num := range in {
		resultado := num * 2 // Logica de processamento
		fmt.Printf(" [Intermediario] Processando: %d -> %d\n", num, resultado)
		out <- resultado // Envia o resultado processado
	}
}

// consumidor le dados do channel de entrada (in)
func consumidor(in <-chan int) {
	// Laco para ler todos os valores ate o channel 'in' ser fechado
	for finalResult := range in {
		fmt.Printf(" [Consumidor] Recebido o resultado final: %d\n", finalResult)
	}
}

func main() {
	fmt.Println("Iniciando comunicacao entre Goroutines...")

	// 1. Canais para comunicacao
	// Produtor -> Intermediario
	ch1 := make(chan int)
	// Intermediario -> Consumidor
	ch2 := make(chan int)

	// 2. Inicia as 3 Goroutines
	// a) Produtor envia para ch1
	go produtor(ch1)

	// b) Intermediario le de ch1 e escreve em ch2
	go intermediario(ch1, ch2)

	// c) Consumidor le de ch2 (esta no main Goroutine para bloquear e esperar)
	// Como o consumidor usa 'for range', ele so terminara quando ch2 for fechado.
	consumidor(ch2)

	// Se o consumidor estivesse em outra Goroutine,
	// teriamos que usar um WaitGroup para esperar ele terminar.

	fmt.Println("Fim do programa. Todos os dados foram processados.")
}
