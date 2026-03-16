# GoRPC - Sistema Distribuído de Gerenciamento de Listas

Implementação de um sistema distribuído para gerenciamento de listas de inteiros, utilizando **RPC (Remote Procedure Call)** em Go. O projeto prioriza consistência forte, alta disponibilidade de leitura e persistência resiliente a falhas.

> **Referência da Disciplina:** Arquivo de Requisitos do Projeto
https://drive.google.com/file/d/1I1K5_PJrroercm9_ccOrOaEVmYFEgc3S/view
---

## Funcionalidades e Requisitos Atendidos

Atendimento integral aos requisitos propostos, com otimizações de engenharia voltadas para cenários reais:

* **Gerenciamento de Múltiplas Listas:** Suporte a N listas simultâneas, identificadas por IDs únicos (`map[int][]int`).
* **Comunicação RPC Síncrona:** Implementação via pacote `net/rpc` sobre TCP.
* **Operações Disponíveis:**
    * `Append(list_id, v)`: Adição de valor ao final.
    * `Remove(list_id)`: Remoção e retorno do último valor (Pilha/LIFO).
    * `Get(list_id, i)`: Retorno de valor de índice específico.
    * `Size(list_id)`: Retorno do tamanho da lista.
* **Persistência Híbrida (Memória + Disco):**
    * **Baixa Latência:** Dados servidos diretamente da RAM.
    * **Write-Ahead Log (WAL):** Salvamento de cada operação de escrita no log (`operations.log`) antes da confirmação ao cliente.
    * **Snapshot em Background:** Salvamento periódico do estado completo (`snapshot.json`) para aceleração da reinicialização.
* **Exclusão Mútua Otimizada:** Uso de `sync.RWMutex` para permissão de leituras paralelas e escritas exclusivas.

---

## Arquitetura e Decisões de Design

### 1. Concorrência (RWMutex)
Substituição do Mutex simples (que bloqueia todo o servidor) pelo uso de `sync.RWMutex`.

* **Leituras (`Get`, `Size`):** Aquisição de `RLock`. Permite a leitura simultânea por múltiplos clientes, aumentando a vazão (throughput).
* **Escritas (`Append`, `Remove`):** Aquisição de `Lock`. Garantia de consistência estrita e serialização das alterações.

### 2. Persistência Robusta (Atomic Snapshot)
Adoção da estratégia **Copy-on-Write + Atomic Rename** para evitar o bloqueio do servidor durante a gravação em disco:

1.  **Lock:** Bloqueio breve do servidor.
2.  **Clone:** Cópia dos dados da memória para uma variável temporária.
3.  **Reset Log:** Truncamento do arquivo de log (sincronização log/memória).
4.  **Unlock:** Liberação do servidor para atendimento aos clientes.
5.  **Save (I/O):** Gravação do clone no disco em arquivo temporário (`.tmp`) via goroutine.
6.  **Atomic Rename:** Substituição atômica do arquivo oficial (`.json`) pelo temporário, gerenciada pelo SO.

**Resultado:** Preservação do arquivo antigo em caso de falha durante o snapshot, prevenindo perda de dados ou corrupção de estado.

---

## Diagramas da Arquitetura

Ilustração dos fluxos lógicos e da estrutura do sistema.
*(Visualização detalhada disponível na pasta `diagrams/`)*

1.  **Diagrama de Classes**
2.  **Inicialização e Recuperação (Startup)**
3.  **Fluxo de Escrita (RPC Append)**
4.  **Snapshot Seguro em Background**
5.  **Fluxo Geral do Sistema (System Flowchart)**

---

## Cenários de Teste (Client)

O arquivo `├remotelist_rpc_client.go` contém uma bateria de testes automatizada dividida em duas partes:

### Parte 1: Testes Funcionais (Simples)
Validação da lógica básica do sistema.
* Inserção sequencial de dados.
* Isolamento (garantia de não interferência de dados entre listas distintas).
* Verificação de retorno de índices e tamanho.

### Parte 2: Testes de Estresse (Complexos)
Simulação de ambiente de produção hostil.

* **Chaos Monkey:** Execução de 20 goroutines (clientes) simultâneas com operações mistas (`Append`, `Get`, `Remove`) em listas aleatórias para verificação de suporte a carga cruzada sem deadlocks.
* **Produtor-Consumidor (Consistência):**
    * População de uma lista com 100 itens.
    * Lançamento de 50 produtores e 50 consumidores simultâneos.
    * **Validação Matemática:** Verificação da igualdade entre o tamanho final e o inicial. Falhas indicam condição de corrida (race condition).
---

##  Como Executar

### Pré-requisitos
* Go 1.20 ou superior instalado.
### Passo 1: Iniciar o Servidor
Abra um terminal na raiz do projeto:
```bash
go run remotelist_rpc_server.go
```
### Passo 2: Executar o Cliente
Abra outro terminal na raiz do projeto:
```bash
go run remotelist_rpc_client.go
```
### Passo 3: Testar Persistência (Manual)
Deixe o servidor rodar e o cliente popular dados.
Pressione Ctrl+C no terminal do servidor para matá-lo.
Reinicie o servidor.
Observe o log: [Server] Estado recuperado do Snapshot ou [Server] X operações recuperadas do Log.
Os dados anteriores estarão disponíveis novamente.


## Estrutura de Arquivos
```bash
GoRPC/
├── go.mod                # Definição do módulo Go
├── remotelist_rpc_server.go             # Entry point do Servidor
├── remotelist_rpc_client.go             # Bateria de Testes (Simples + Stress)
├── remotelist_rpc_client_delay.go             # Bateria de Testes (Um pouco mais lento para utilização de clientes manualmente)
├── README.md             # Documentação e Diagramas
├── operations.log        # (Gerado) Log de operações (WAL)
├── snapshot.json         # (Gerado) Persistência completa
├── pkg/
│   └── remotelist.go     # Core: Lógica, RPC, Persistência
└── diagrams/
├── diagramas.md      # Documentação original dos diagramas
└── (imagens...)      # Imagens estáticas dos diagramas (se geradas)
```