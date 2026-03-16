package main

import (
	"fmt"
	"log"
	"math/rand"
	"net/rpc"
	"sync"
	"sync/atomic"
	"time"

	remotelist "GoRPC/pkg"
)

func main() {
	// Configura logs com precisão de microssegundos para análise de performance
	log.SetFlags(log.Ltime | log.Lmicroseconds)
	rand.Seed(time.Now().UnixNano())

	// Conexão principal
	client, err := rpc.Dial("tcp", "localhost:5000")
	if err != nil {
		log.Fatalf("ERRO CRÍTICO: Não foi possível conectar ao servidor: %v", err)
	}
	defer client.Close()

	var reply bool
	var replyInt int

	fmt.Println("=============================================================")
	fmt.Println("       BATERIA DE TESTES UNIFICADA - REMOTELIST RPC          ")
	fmt.Println("=============================================================")

	// =================================================================
	// PARTE 1: TESTES SIMPLES (VALIDAÇÃO FUNCIONAL)
	// =================================================================
	log.Println("\n--- [PARTE 1] TESTES FUNCIONAIS BÁSICOS ---")

	// 1. Inserção Sequencial
	log.Println("1.1 Testando Inserção Sequencial (Lista 1)...")
	for i := 1; i <= 5; i++ {
		args := remotelist.AppendArgs{ListID: 1, Value: i * 10}
		if err := client.Call("RemoteList.Append", args, &reply); err != nil {
			log.Fatalf("Falha no Append(1, %d): %v", i*10, err)
		}
		fmt.Printf("    -> Append(1, %d) [OK]\n", i*10)
	}

	// 2. Múltiplas Listas
	log.Println("1.2 Testando Isolamento de Listas (Lista 2)...")
	args2 := remotelist.AppendArgs{ListID: 2, Value: 999}
	if err := client.Call("RemoteList.Append", args2, &reply); err != nil {
		log.Printf("Erro no Append Lista 2: %v", err)
	} else {
		fmt.Println("    -> Append(2, 999) [OK]")
	}

	// 3. Leitura e Verificação
	log.Println("1.3 Testando Leitura (Get/Size)...")
	getArgs := remotelist.GetArgs{ListID: 1, Index: 2} // Esperado: 30 (índice 0=10, 1=20, 2=30)
	if err := client.Call("RemoteList.Get", getArgs, &replyInt); err != nil {
		log.Printf("Erro no Get(1, 2): %v", err)
	} else {
		fmt.Printf("    -> Get(1, 2) retornou: %d (Esperado: 30) [OK]\n", replyInt)
	}

	sizeArgs := remotelist.ListIDArgs{ListID: 1}
	if err := client.Call("RemoteList.Size", sizeArgs, &replyInt); err != nil {
		log.Printf("Erro no Size(1): %v", err)
	} else {
		fmt.Printf("    -> Size(1) retornou: %d [OK]\n", replyInt)
	}

	// =================================================================
	// PARTE 2: TESTES COMPLEXOS (ESTRESSE E CONCORRÊNCIA)
	// =================================================================
	log.Println("\n--- [PARTE 2] TESTES DE ESTRESSE E CONCORRÊNCIA ---")

	// 4. Chaos Monkey (Carga Mista)
	log.Println("\n2.1 INICIANDO 'CHAOS TEST' (OPERAÇÕES CRUZADAS)")
	log.Println("    -> Simulando 20 clientes acessando 5 listas aleatoriamente.")
	log.Println("    -> Mistura de Append (Escrita), Get (Leitura) e Remove (Escrita).")

	chaosWorkers := 20
	opsPerWorker := 50
	listIDs := []int{10, 11, 12, 13, 14} // Listas alvo
	var wgChaos sync.WaitGroup

	var opsSuccess int64
	var opsFail int64

	startChaos := time.Now()

	for i := 0; i < chaosWorkers; i++ {
		wgChaos.Add(1)
		go func(workerID int) {
			defer wgChaos.Done()

			// Conexão dedicada por worker (simula clientes reais distintos)
			c, err := rpc.Dial("tcp", "localhost:5000")
			if err != nil {
				log.Printf("Worker %d falhou ao conectar: %v", workerID, err)
				atomic.AddInt64(&opsFail, 1)
				return
			}
			defer c.Close()

			for j := 0; j < opsPerWorker; j++ {
				targetList := listIDs[rand.Intn(len(listIDs))]
				action := rand.Intn(3) // 0: Append, 1: Get, 2: Remove

				var errOp error
				switch action {
				case 0: // Append
					val := rand.Intn(1000)
					args := remotelist.AppendArgs{ListID: targetList, Value: val}
					var r bool
					errOp = c.Call("RemoteList.Append", args, &r)
				case 1: // Get
					args := remotelist.GetArgs{ListID: targetList, Index: 0}
					var r int
					errOp = c.Call("RemoteList.Get", args, &r)
					// Ignora erro de lista vazia/índice no teste de chaos
					if errOp != nil && errOp.Error() == "índice fora dos limites ou lista inexistente" {
						errOp = nil
					}
				case 2: // Remove
					args := remotelist.ListIDArgs{ListID: targetList}
					var r int
					errOp = c.Call("RemoteList.Remove", args, &r)
					// Ignora erro de lista vazia
					if errOp != nil && errOp.Error() == "lista vazia ou inexistente" {
						errOp = nil
					}
				}

				if errOp != nil {
					log.Printf("Erro na operação (Worker %d): %v", workerID, errOp)
					atomic.AddInt64(&opsFail, 1)
				} else {
					atomic.AddInt64(&opsSuccess, 1)
				}
				time.Sleep(time.Duration(rand.Intn(5)) * time.Millisecond)
			}
		}(i)
	}

	wgChaos.Wait()
	durationChaos := time.Since(startChaos)
	log.Printf("    -> Chaos Test finalizado em %v", durationChaos)
	log.Printf("    -> Sucessos: %d | Falhas reais: %d", atomic.LoadInt64(&opsSuccess), atomic.LoadInt64(&opsFail))

	// 5. Produtor-Consumidor (Consistência Matemática)
	targetListID := 99
	initialItems := 100
	producers := 50
	consumers := 50

	log.Printf("\n2.2 CONSISTÊNCIA PRODUTOR-CONSUMIDOR (Lista %d)", targetListID)
	log.Println("    -> Passo 1: Populando lista com 100 itens iniciais...")

	for i := 0; i < initialItems; i++ {
		client.Call("RemoteList.Append", remotelist.AppendArgs{ListID: targetListID, Value: 1}, &reply)
	}

	client.Call("RemoteList.Size", remotelist.ListIDArgs{ListID: targetListID}, &replyInt)
	log.Printf("    -> Tamanho Inicial: %d", replyInt)

	log.Printf("    -> Passo 2: Lançando %d Produtores e %d Consumidores simultâneos...", producers, consumers)
	log.Println("    -> Matemática esperada: 100 + 50 - 50 = 100")

	var wgConsist sync.WaitGroup
	startConsist := time.Now()

	// Produtores
	for i := 0; i < producers; i++ {
		wgConsist.Add(1)
		go func() {
			defer wgConsist.Done()
			c, _ := rpc.Dial("tcp", "localhost:5000")
			defer c.Close()
			c.Call("RemoteList.Append", remotelist.AppendArgs{ListID: targetListID, Value: 777}, &reply)
		}()
	}

	// Consumidores
	for i := 0; i < consumers; i++ {
		wgConsist.Add(1)
		go func() {
			defer wgConsist.Done()
			c, _ := rpc.Dial("tcp", "localhost:5000")
			defer c.Close()
			for {
				err := c.Call("RemoteList.Remove", remotelist.ListIDArgs{ListID: targetListID}, &replyInt)
				if err == nil {
					return
				}
				time.Sleep(time.Millisecond)
			}
		}()
	}

	wgConsist.Wait()
	log.Printf("    -> Operações concorrentes finalizadas em %v", time.Since(startConsist))

	// Verificação Final
	client.Call("RemoteList.Size", remotelist.ListIDArgs{ListID: targetListID}, &replyInt)

	if replyInt == initialItems {
		log.Printf("    -> [SUCESSO] Tamanho Final: %d. Consistência mantida!", replyInt)
	} else {
		log.Printf("    -> [FALHA CRÍTICA] Tamanho Final: %d. Esperado: %d.", replyInt, initialItems)
	}

	fmt.Println("\n=============================================================")
	fmt.Println("             BATERIA DE TESTES FINALIZADA                    ")
	fmt.Println("=============================================================")
}
