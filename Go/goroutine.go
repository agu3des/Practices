package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println(" Iniciando o programa ")

	// Cria um slice de strings
	mensagens := []string{"Ola ", "do", "Go", " com ", " goroutines !"}

	// Para cada mensagem , cria uma goroutine usando uma closure function
	for i, msg := range mensagens {
		go func(indice int, texto string) {
			// Essa funcao captura as variaveis passadas
			fmt.Printf(" Goroutine %d: %s\n", indice, texto)
		}(i, msg) // valores passados como argumentos
	}

	// Aguarda um pouco para todas as goroutines terminarem
	time.Sleep(500 * time.Millisecond)
	fmt.Println(" Fim do programa ")

}
