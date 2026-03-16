package remotelist

import (
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"log"
	"os"
	"sync"
	"time"
)

// Constantes para nomes de arquivo
const (
	SnapshotFile = "snapshot.json"
	TempSnapshot = "snapshot.tmp" // Arquivo temporário para garantir atomicidade
	LogFile      = "operations.log"
)

// Argumentos para as chamadas RPC
type AppendArgs struct {
	ListID int
	Value  int
}

type GetArgs struct {
	ListID int
	Index  int
}

type ListIDArgs struct {
	ListID int
}

// RemoteList gerencia múltiplas listas de inteiros
type RemoteList struct {
	// 1.2 EXCLUSÃO MÚTUA OTIMIZADA: RWMutex
	mu      sync.RWMutex
	Lists   map[int][]int
	logFile *os.File
	enc     *json.Encoder
}

// NewRemoteList cria uma nova instância e inicia o processo de recuperação
func NewRemoteList() *RemoteList {
	rl := &RemoteList{
		Lists: make(map[int][]int),
	}

	// 1. Recupera do Snapshot (Estado Base)
	rl.loadSnapshot()

	// 2. Reaplica operações do Log (Estado Recente)
	rl.replayLog()

	// 3. Abre arquivo de log para escrita (append)
	f, err := os.OpenFile(LogFile, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		log.Fatal("Erro fatal ao abrir arquivo de log:", err)
	}
	rl.logFile = f
	rl.enc = json.NewEncoder(f)

	// 4. Inicia snapshot periódico
	go rl.backgroundSnapshot()

	return rl
}

// --- Métodos RPC ---

func (l *RemoteList) Append(args *AppendArgs, reply *bool) error {
	l.mu.Lock() // Lock Exclusivo (Escrita)
	defer l.mu.Unlock()

	// 1. Memória
	l.Lists[args.ListID] = append(l.Lists[args.ListID], args.Value)

	// 2. Persistência
	entry := map[string]interface{}{
		"Op":     "append",
		"ListID": args.ListID,
		"Value":  args.Value,
	}

	// Validação de erro de disco (Robustez)
	if err := l.enc.Encode(entry); err != nil {
		log.Printf("CRÍTICO: Falha ao escrever no log: %v", err)
		return fmt.Errorf("erro de persistência no servidor")
	}

	*reply = true
	return nil
}

func (l *RemoteList) Remove(args *ListIDArgs, reply *int) error {
	l.mu.Lock() // Lock Exclusivo (Escrita)
	defer l.mu.Unlock()

	list, exists := l.Lists[args.ListID]
	if !exists || len(list) == 0 {
		return errors.New("lista vazia ou inexistente")
	}

	lastIndex := len(list) - 1
	val := list[lastIndex]
	l.Lists[args.ListID] = list[:lastIndex]

	*reply = val

	entry := map[string]interface{}{
		"Op":     "remove",
		"ListID": args.ListID,
	}
	if err := l.enc.Encode(entry); err != nil {
		log.Printf("CRÍTICO: Falha ao escrever no log: %v", err)
		return fmt.Errorf("erro de persistência no servidor")
	}

	return nil
}

func (l *RemoteList) Get(args *GetArgs, reply *int) error {
	l.mu.RLock() // Lock Compartilhado (Leitura Simultânea)
	defer l.mu.RUnlock()

	list, exists := l.Lists[args.ListID]
	if !exists || args.Index < 0 || args.Index >= len(list) {
		return errors.New("índice fora dos limites ou lista inexistente")
	}

	*reply = list[args.Index]
	return nil
}

func (l *RemoteList) Size(args *ListIDArgs, reply *int) error {
	l.mu.RLock() // Lock Compartilhado (Leitura Simultânea)
	defer l.mu.RUnlock()

	if list, exists := l.Lists[args.ListID]; exists {
		*reply = len(list)
	} else {
		*reply = 0
	}
	return nil
}

// --- Persistência Robusta ---

func (l *RemoteList) backgroundSnapshot() {
	for {
		time.Sleep(10 * time.Second)
		l.takeSnapshotSafe()
	}
}

// takeSnapshotSafe implementa a estratégia de consistência forte com baixo bloqueio
func (l *RemoteList) takeSnapshotSafe() {
	l.mu.Lock() // Lock Exclusivo 

	// 1. Clonagem Rápida (Memória)
	dataClone := make(map[int][]int)
	for k, v := range l.Lists {
		tmp := make([]int, len(v))
		copy(tmp, v)
		dataClone[k] = tmp
	}

	// --- CORREÇÃO PARA WINDOWS (Access Denied Fix) ---
	// No Windows, não podemos truncar um arquivo aberto com O_APPEND facilmente.
	// A solução robusta é: Fechar -> Truncar por Path -> Reabrir.

	// A. Fecha o handler atual (libera o lock do SO)
	l.logFile.Close()

	// B. Trunca o arquivo físico para zero bytes
	if err := os.Truncate(LogFile, 0); err != nil {
		l.mu.Unlock()
		log.Printf("Erro ao truncar log (filesystem) durante snapshot: %v", err)
		// Tenta reabrir para não matar o servidor
		f, _ := os.OpenFile(LogFile, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
		l.logFile = f
		l.enc = json.NewEncoder(f)
		return
	}

	// C. Reabre o arquivo limpo
	f, err := os.OpenFile(LogFile, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		l.mu.Unlock()
		log.Fatalf("ERRO FATAL: Não foi possível reabrir o log após truncate: %v", err)
	}
	l.logFile = f

	// D. CRUCIAL: Cria um novo encoder apontando para o novo arquivo
	l.enc = json.NewEncoder(l.logFile)

	l.mu.Unlock() // Libera o servidor. Clientes podem escrever no log vazio agora.

	// 3. Gravação Lenta (I/O) fora da seção crítica
	// O servidor já está livre, então essa gravação pode demorar o quanto for necessário.
	file, err := os.Create(TempSnapshot)
	if err != nil {
		log.Printf("Erro ao criar snapshot temporário: %v", err)
		return
	}

	encoder := json.NewEncoder(file)
	if err := encoder.Encode(dataClone); err != nil {
		file.Close()
		log.Printf("Erro ao gravar dados no snapshot: %v", err)
		return
	}
	file.Close()

	// 4. Commit Atômico (Rename)
	// No Windows, Rename falha se o destino existir. Remove o destino antes.
	if _, err := os.Stat(SnapshotFile); err == nil {
		os.Remove(SnapshotFile)
	}

	if err := os.Rename(TempSnapshot, SnapshotFile); err != nil {
		log.Printf("Erro ao substituir snapshot oficial: %v", err)
		return
	}

	log.Println("[Server] Snapshot seguro salvo e Log rotacionado (Windows-Safe).")
}

func (l *RemoteList) loadSnapshot() {
	file, err := os.Open(SnapshotFile)
	if err != nil {
		if !os.IsNotExist(err) {
			log.Printf("Erro ao ler snapshot: %v", err)
		}
		return
	}
	defer file.Close()

	decoder := json.NewDecoder(file)
	if err := decoder.Decode(&l.Lists); err != nil {
		log.Printf("Erro ao decodificar snapshot: %v", err)
	} else {
		log.Println("[Server] Estado recuperado do Snapshot.")
	}
}

func (l *RemoteList) replayLog() {
	file, err := os.Open(LogFile)
	if err != nil {
		return
	}
	defer file.Close()

	decoder := json.NewDecoder(file)
	count := 0
	for {
		var entry map[string]interface{}
		if err := decoder.Decode(&entry); err == io.EOF {
			break
		} else if err != nil {
			log.Printf("Aviso: Fim do log ou entrada parcial: %v", err)
			break
		}

		op := entry["Op"].(string)
		listID := int(entry["ListID"].(float64))

		if op == "append" {
			val := int(entry["Value"].(float64))
			l.Lists[listID] = append(l.Lists[listID], val)
		} else if op == "remove" {
			if len(l.Lists[listID]) > 0 {
				l.Lists[listID] = l.Lists[listID][:len(l.Lists[listID])-1]
			}
		}
		count++
	}
	if count > 0 {
		log.Printf("[Server] %d operações recuperadas do Log.", count)
	}
}
