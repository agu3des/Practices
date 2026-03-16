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
	fmt.Println(">>> DICA: Abra outro terminal e execute este cliente novamente.")
	fmt.Println(">>> Pressione ENTER para iniciar os testes neste terminal...")
	fmt.Scanln() // <--- TRAVA PARA SINCRONIZAR DOIS TERMINAIS

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
		time.Sleep(100 * time.Millisecond) // Delay visual
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
	getArgs := remotelist.GetArgs{ListID: 1, Index: 2}
	if err := client.Call("RemoteList.Get", getArgs, &replyInt); err != nil {
		// Não falha crítico aqui pois outros clientes podem ter alterado a lista
		log.Printf("Aviso: Get(1, 2) retornou erro (possível concorrência): %v", err)
	} else {
		fmt.Printf("    -> Get(1, 2) retornou: %d [OK]\n", replyInt)
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
	// AUMENTADO: opsPerWorker de 50 para 200 para durar mais tempo
	log.Println("\n2.1 INICIANDO 'CHAOS TEST' (OPERAÇÕES CRUZADAS)")
	log.Println("    -> Simulando 20 clientes acessando 5 listas aleatoriamente.")

	chaosWorkers := 20
	opsPerWorker := 200 // Aumentado para gerar carga sustentada
	listIDs := []int{10, 11, 12, 13, 14}
	var wgChaos sync.WaitGroup

	var opsSuccess int64
	var opsFail int64

	startChaos := time.Now()

	for i := 0; i < chaosWorkers; i++ {
		wgChaos.Add(1)
		go func(workerID int) {
			defer wgChaos.Done()

			c, err := rpc.Dial("tcp", "localhost:5000")
			if err != nil {
				atomic.AddInt64(&opsFail, 1)
				return
			}
			defer c.Close()

			for j := 0; j < opsPerWorker; j++ {
				targetList := listIDs[rand.Intn(len(listIDs))]
				action := rand.Intn(3)

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
					if errOp != nil {
						errOp = nil
					} // Ignora erros lógicos no Chaos
				case 2: // Remove
					args := remotelist.ListIDArgs{ListID: targetList}
					var r int
					errOp = c.Call("RemoteList.Remove", args, &r)
					if errOp != nil {
						errOp = nil
					}
				}

				if errOp != nil {
					log.Printf("Erro IO (Worker %d): %v", workerID, errOp)
					atomic.AddInt64(&opsFail, 1)
				} else {
					atomic.AddInt64(&opsSuccess, 1)
				}

				// Delay aumentado para 0-30ms por operação para estender a duração do teste
				time.Sleep(time.Duration(rand.Intn(30)) * time.Millisecond)
			}
		}(i)
	}

	wgChaos.Wait()
	durationChaos := time.Since(startChaos)
	log.Printf("    -> Chaos Test finalizado em %v", durationChaos)
	log.Printf("    -> Sucessos: %d | Falhas de IO: %d", atomic.LoadInt64(&opsSuccess), atomic.LoadInt64(&opsFail))

	// 5. Produtor-Consumidor
	targetListID := 99
	initialItems := 100
	producers := 50
	consumers := 50

	log.Printf("\n2.2 CONSISTÊNCIA PRODUTOR-CONSUMIDOR (Lista %d)", targetListID)
	log.Println("    -> Passo 1: Populando lista com 100 itens iniciais...")

	// Reset da lista para garantir teste limpo se rodar múltiplas vezes
	// (Na prática apenas adicionamos, num sistema real teríamos um Clear)
	for i := 0; i < initialItems; i++ {
		client.Call("RemoteList.Append", remotelist.AppendArgs{ListID: targetListID, Value: 1}, &reply)
	}

	var startSize int
	client.Call("RemoteList.Size", remotelist.ListIDArgs{ListID: targetListID}, &startSize)
	log.Printf("    -> Tamanho Inicial Real: %d (Pode variar se houver outro cliente rodando)", startSize)

	log.Printf("    -> Passo 2: Lançando %d Produtores e %d Consumidores simultâneos...", producers, consumers)

	var wgConsist sync.WaitGroup
	startConsist := time.Now()

	for i := 0; i < producers; i++ {
		wgConsist.Add(1)
		go func() {
			defer wgConsist.Done()
			c, _ := rpc.Dial("tcp", "localhost:5000")
			defer c.Close()
			c.Call("RemoteList.Append", remotelist.AppendArgs{ListID: targetListID, Value: 777}, &reply)
			time.Sleep(time.Duration(rand.Intn(50)) * time.Millisecond) // Delay para espalhar a carga
		}()
	}

	for i := 0; i < consumers; i++ {
		wgConsist.Add(1)
		go func() {
			defer wgConsist.Done()
			c, _ := rpc.Dial("tcp", "localhost:5000")
			defer c.Close()
			// Tenta remover até conseguir (pode falhar se a lista esvaziar momentaneamente)
			for {
				err := c.Call("RemoteList.Remove", remotelist.ListIDArgs{ListID: targetListID}, &replyInt)
				if err == nil {
					time.Sleep(time.Duration(rand.Intn(50)) * time.Millisecond)
					return
				}
				time.Sleep(10 * time.Millisecond)
			}
		}()
	}

	wgConsist.Wait()
	log.Printf("    -> Operações concorrentes finalizadas em %v", time.Since(startConsist))

	// Verificação Final
	var endSize int
	client.Call("RemoteList.Size", remotelist.ListIDArgs{ListID: targetListID}, &endSize)

	// Nota: Se dois clientes rodarem isso simultaneamente na mesma lista 99,
	// a matemática ainda deve bater: (Inicio + 50 - 50) do Cliente A + (InicioB + 50 - 50) do Cliente B.
	// O tamanho final deve ser igual ao tamanho inicial.
	if endSize == startSize {
		log.Printf("    -> [SUCESSO] Tamanho Final: %d (Igual ao inicial). Consistência mantida!", endSize)
	} else {
		log.Printf("    -> [ALERTA] Tamanho Final: %d (Inicial: %d). Se outro cliente rodou junto, verifique se o delta é zero.", endSize, startSize)
	}

	fmt.Println("\n=============================================================")
	fmt.Println("             BATERIA DE TESTES FINALIZADA                    ")
	fmt.Println("=============================================================")
	fmt.Println("Pressione ENTER para sair...")
	fmt.Scanln()
}
