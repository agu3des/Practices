package main

import (
	"log"
	"net"
	"net/rpc"
	"os"
	"os/signal"
	"syscall"
	remotelist "GoRPC/pkg"
)

func main() {
	// Configuração de Log para incluir data, hora e arquivo de origem
	log.SetFlags(log.LstdFlags | log.Lshortfile)

	log.Println("Inicializando sistema RemoteList...")

	// Inicializa a lista remota (carrega snapshot/logs se existirem)
	listServer := remotelist.NewRemoteList()

	// Registro do serviço RPC
	rpcs := rpc.NewServer()
	if err := rpcs.Register(listServer); err != nil {
		log.Fatalf("Erro fatal ao registrar serviço RPC: %v", err)
	}

	addr := ":5000"
	l, err := net.Listen("tcp", addr)
	if err != nil {
		log.Fatalf("Erro fatal ao abrir porta %s: %v", addr, err)
	}

	// Canal para capturar sinais do SO (Ctrl+C, Kill)
	// Isso permite um encerramento mais controlado se necessário no futuro
	sigs := make(chan os.Signal, 1)
	signal.Notify(sigs, syscall.SIGINT, syscall.SIGTERM)

	go func() {
		<-sigs
		log.Println("\nRecebido sinal de encerramento. Parando servidor...")
		l.Close()
		os.Exit(0)
	}()

	log.Printf("Servidor RPC OTIMIZADO rodando em %s", addr)
	log.Println("Logs de operações e snapshots serão gerados automaticamente.")

	// Loop de aceitação de conexões
	for {
		conn, err := l.Accept()
		if err != nil {
			// Evita que um erro de conexão derrube o servidor inteiro
			log.Printf("Erro ao aceitar conexão: %v", err)
			continue
		}
		// Goroutine para cada cliente (Concorrência)
		go func(c net.Conn) {
			log.Printf("Nova conexão estabelecida: %s", c.RemoteAddr())
			rpcs.ServeConn(c)
			log.Printf("Conexão encerrada: %s", c.RemoteAddr())
		}(conn)
	}
}
