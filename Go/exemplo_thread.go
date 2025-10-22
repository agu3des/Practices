package main

import (
	"fmt"
	"sync"
	"time"
)

var (
	counter int
	mutex   sync.Mutex
)

func taskCode(tid, n int, wg *sync.WaitGroup) {
	defer wg.Done()

	fmt.Printf("Goroutine %d iniciada\n", tid)

	for i := 0; i < n; i++ {
		mutex.Lock()
		counter++
		mutex.Unlock()
	}
}

func main() {
	var wg sync.WaitGroup
	var n, qtdT int

	fmt.Print("Digite a quantidade de iterações: ")
	fmt.Scanln(&n)

	fmt.Print("Digite a quantidade de threads: ")
	fmt.Scanln(&qtdT)

	for i := 0; i < qtdT; i++ {
		wg.Add(1)
		go taskCode(i, n, &wg)
	}

	wg.Wait()

	fmt.Println("Valor final do contador:", counter)
}




package main

import (
"fmt"
"sync"
"time"
)

// produtor envia 10 valores inteiros para o canal de saida (out)
func insere(id int, startValue int, out chan<- int, wg *sync.WaitGroup) {
	// Decrementa o contador do WaitGroup quando esta goroutine terminar
	defer wg.Done()

	endValue := startValue + 9 // Garante 10 iteracoes (ex: 1 a 10, ou 11 a 20)

	for i := startValue; i <= endValue; i++ {
		fmt.Printf(" [Produtor %d] Enviando: %d\n", id, i)
		out <- i // Envia o numero para o canal
		time.Sleep(5 * time.Millisecond) // Pequena pausa para visualizacao
	}
}

// consumidor le todos os dados do canal de entrada (in)
func ler(in <-chan int, done chan<- bool) {
	totalLido := 0
	// O for range le todos os valores ate o canal 'in' ser fechado
	for result := range in {
		fmt.Printf(" [Consumidor] Recebido: %d\n", result)
		totalLido++
	}

	fmt.Printf("\n [Consumidor] Fim da leitura. Total lido: %d\n", totalLido)
	// Sinaliza para a goroutine principal que o Consumidor terminou
	done <- true
}

func main() {
	fmt.Println("Iniciando produtores e consumidor.")

	// 1. Canal de comunicacao
	ch1 := make(chan int)

	// 2. WaitGroup para esperar os produtores terminarem
	var wg sync.WaitGroup

	// 3. Canal para sinalizar a Goroutine principal que a leitura terminou
	done := make(chan bool)

	// Inicia a Goroutine Consumidora (a terceira Goroutine)
	go ler(ch1, done)

	// Aumenta o contador do WaitGroup para 2 Goroutines (insere1 e insere2)
	wg.Add(2)

	// Inicia as Goroutines Produtoras (as duas primeiras Goroutines)
	go insere(1, 1, ch1, &wg)    // Produtor 1 envia 1 a 10
	go insere(2, 11, ch1, &wg) // Produtor 2 envia 11 a 20

	// Rotina para fechar o canal
	go func() {
		// Espera que os dois produtores (wg.Add(2)) terminem o trabalho (wg.Done())
		wg.Wait()
		// Depois que os produtores terminarem, e seguro fechar o canal
		close(ch1)
		fmt.Println("\n *** Canal Fechado (Produtores Finalizados) ***")
	}()

	// Aguarda o sinal da goroutine Consumidora (ler) indicando que ele terminou
	<-done

	fmt.Println("\nFim do programa. Todos os 20 dados foram processados.")
}
