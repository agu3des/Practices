# Diagramas do Sistema RemoteList RPC
Este documento contém diagramas UML (usando sintaxe Mermaid) para ilustrar a arquitetura, fluxo de dados e processos de concorrência do sistema.

## 1. Diagrama de Classes
Mostra a estrutura principal do servidor (RemoteList), seus métodos públicos (RPC), métodos privados (Persistência) e as estruturas de dados auxiliares para comunicação.
[class_diagram](class_diagram.png)

classDiagram
class RemoteList {
-sync.RWMutex mu
-map[int][]int Lists
-os.File logFile
-json.Encoder enc
+NewRemoteList() RemoteList
+Append(args: AppendArgs, reply: *bool) error
+Remove(args: ListIDArgs, reply: *int) error
+Get(args: GetArgs, reply: *int) error
+Size(args: ListIDArgs, reply: *int) error
-backgroundSnapshot()
-takeSnapshotSafe()
-loadSnapshot()
-replayLog()
}

    class AppendArgs {
        +int ListID
        +int Value
    }

    class GetArgs {
        +int ListID
        +int Index
    }

    class ListIDArgs {
        +int ListID
    }

    %% Relações de Dependência (Uso)
    RemoteList ..> AppendArgs : usa
    RemoteList ..> GetArgs : usa
    RemoteList ..> ListIDArgs : usa


## 2. Diagrama de Sequência: Inicialização e Recuperação (Startup)
Fluxo ocorre quando o servidor é iniciado (server.go -> NewRemoteList). Ele mostra como o sistema recupera o estado anterior antes de aceitar novas conexões.
[server_diagram](sequence_server_diagram.png)

sequenceDiagram
participant Main as Server Main
participant RL as RemoteList
participant FS as FileSystem (Disk)

    Main->>RL: NewRemoteList()
    activate RL
    
    Note over RL: 1. Carregar Estado Base
    RL->>FS: Open("snapshot.json")
    alt Snapshot Existe
        FS-->>RL: Conteúdo JSON
        RL->>RL: loadSnapshot() (Decodifica para Memória)
    else Não Existe
        RL->>RL: Inicia vazio
    end

    Note over RL: 2. Reaplicar Logs Recentes
    RL->>FS: Open("operations.log")
    loop Para cada linha no Log
        FS-->>RL: Operação (Append/Remove)
        RL->>RL: replayLog() (Aplica na Memória)
    end

    Note over RL: 3. Preparar para Escrita
    RL->>FS: Open("operations.log", APPEND|CREATE)
    
    Note over RL: 4. Iniciar Background Tasks
    RL->>RL: go backgroundSnapshot()
    
    RL-->>Main: Instância Pronta
    deactivate RL


## 3. Diagrama de Sequência: Operação de Escrita (RPC Append)
Ilustra o fluxo de uma requisição de cliente. Note o uso do Lock para garantir consistência entre memória e disco (Log).
[client_diagram](sequence_client_diagram.png)

sequenceDiagram
participant Client
participant RPC as RPC Handler
participant RL as RemoteList
participant Log as operations.log

    Client->>RPC: Call("RemoteList.Append", args)
    RPC->>RL: Append(args)
    
    activate RL
    Note right of RL: Exclusão Mútua (Escrita)
    RL->>RL: mu.Lock()
    
    Note right of RL: 1. Atualiza Memória (Rápido)
    RL->>RL: Lists[id].append(val)
    
    Note right of RL: 2. Persistência (WAL)
    RL->>Log: Encode(JSON Entry)
    alt Erro de Disco
        RL-->>RPC: Retorna Erro
    else Sucesso
        Note right of RL: 3. Libera Server
        RL->>RL: mu.Unlock()
        RL-->>RPC: reply = true
    end
    deactivate RL
    
    RPC-->>Client: Retorno da Chamada


## 4. Diagrama de Sequência: Processo de Snapshot Seguro (Background)
Fluxo mais complexo e crítico. Ele mostra como o servidor salva o estado completo sem bloquear os clientes por muito tempo (estratégia Copy-on-Write + Atomic Rename).
[goroutine_diagram](sequence_goroutine_diagram.png)

sequenceDiagram
participant BG as Goroutine Background
participant RL as RemoteList (Memória)
participant Log as operations.log
participant FS as FileSystem

    loop A cada 10 segundos
        BG->>RL: takeSnapshotSafe()
        activate RL
        
        Note over RL: BLOQUEIO CRÍTICO (Stop-the-world)
        RL->>RL: mu.Lock()
        
        Note over RL: 1. Clonagem
        RL->>RL: Copia Map (Memória -> Clone)
        
        Note over RL: 2. Reset do Log (Sincronização)
        RL->>Log: Truncate(0) & Seek(0)
        
        RL->>RL: mu.Unlock()
        Note over RL: DESBLOQUEIO (Clientes voltam a operar)
        
        Note over RL: 3. I/O Lento (Fora do Lock)
        RL->>FS: Create("snapshot.tmp")
        RL->>FS: Encode(Clone) -> snapshot.tmp
        
        alt Sucesso na Gravação
            Note over RL: 4. Commit Atômico
            RL->>FS: Rename("snapshot.tmp" -> "snapshot.json")
        else Erro
            RL->>BG: Loga Erro (Mantém snapshot anterior)
        end
        
        deactivate RL
    end

## 5. Fluxo Geral do Sistema (System Flowchart)
Unifica a visão de Clientes, Rede, Processamento Concorrente e Persistência em disco.
[flowchart_diagram](flowchart_diagram.png)

flowchart TD
subgraph Clients["Clientes RPC"]
C1[Cliente 1]
C2[Cliente 2]
CN[Cliente N]
end

    subgraph Net["Rede (TCP :5000)"]
        RPC[Handler RPC]
    end

    subgraph Server["Servidor RemoteList"]
        Router{Tipo de Requisição?}
        
        subgraph ReadOps["Leitura (Concurrent)"]
            RLock[RLock: Bloqueio Compartilhado]
            Read[Lê Mapa em Memória]
            RUnlock[RUnlock: Libera]
        end

        subgraph WriteOps["Escrita (Exclusive)"]
            Lock[Lock: Bloqueio Total]
            WriteMem[Atualiza Mapa em Memória]
            WriteLog[Grava no Log]
            Unlock[Unlock: Libera]
        end
    end

    subgraph BG["Background Service"]
        Timer((Timer 10s))
        SnapLock[Lock: Bloqueio Total]
        Clone[Clona Memória & Limpa Log]
        SnapUnlock[Unlock: Libera]
        SaveDisk[Grava Snapshot Temporário]
        Rename[Atomic Rename]
    end

    subgraph Disk["Armazenamento Persistente"]
        LogFile[("operations.log (WAL)")]
        SnapFile[("snapshot.json (Base)")]
    end

    %% Fluxo Clientes
    C1 & C2 & CN --> RPC --> Router
    
    %% Fluxo Leitura
    Router -- "Get / Size" --> RLock --> Read --> RUnlock --> Response1[Retorna Valor]
    
    %% Fluxo Escrita
    Router -- "Append / Remove" --> Lock --> WriteMem --> WriteLog --> Unlock --> Response2[Retorna Sucesso]
    WriteLog -.-> LogFile

    %% Fluxo Snapshot
    Timer --> SnapLock --> Clone --> SnapUnlock --> SaveDisk --> Rename --> SnapFile
    Clone -.->|Truncate| LogFile
    
    %% Recuperação (Inicialização)
    Startup[Startup: NewRemoteList] --> LoadSnap[Carrega Snapshot] --> LoadLog[Reaplica Log]
    SnapFile -.-> LoadSnap
    LogFile -.-> LoadLog