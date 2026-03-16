package main

import (
	"fmt"
	"math/rand"
	"time"
)

const totalReadings = 15

func sensor(name string, out chan<- float64) {
	source := rand.NewSource(time.Now().UnixNano() + int64(len(name)*100))
	r := rand.New(source)
	
	var baseValue float64
	var variance float64
	
	switch name {
	case "Temperatura":
		baseValue = 25.0
		variance = 5.0
	case "Pressão":
		baseValue = 101.0
		variance = 0.5
	case "Umidade":
		baseValue = 60.0
		variance = 10.0
	}

	for {
		reading := baseValue + r.Float64()*variance - (variance / 2)
		out <- reading 
		time.Sleep(time.Duration(r.Intn(150)+50) * time.Millisecond)
	}
}

func main() {
	fmt.Println("Simulador de Sensores Ativado (3 Goroutines + Select)")
	
	tempCh := make(chan float64)
	pressCh := make(chan float64)
	humidCh := make(chan float64)
	
	count := 0

	go sensor("Temperatura", tempCh)
	go sensor("Pressão", pressCh)
	go sensor("Umidade", humidCh)
	
	timeout := time.After(2 * time.Second) 

	for count < totalReadings {
		select {
		case t := <-tempCh:
			fmt.Printf(" Sensor: Temperatura\t| Leitura: %.2f °C\n", t)
			count++
			
		case p := <-pressCh:
			fmt.Printf(" Sensor: Pressão\t| Leitura: %.2f kPa\n", p)
			count++
			
		case h := <-humidCh:
			fmt.Printf(" Sensor: Umidade\t| Leitura: %.2f %%\n", h)
			count++
			
		case <-timeout:
			fmt.Println("\n *** Tempo limite atingido. Encerrando simulacao. ***")
			goto endLoop 
		}
	}
	
endLoop:
	fmt.Println("\nFim do programa. Total de leituras processadas:", count)
}
