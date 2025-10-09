# Resumo do Livro: Distributed Systems

**Autores:** Maarten van Steen & Andrew S. Tanenbaum (4ª Edição, Versão 4.03, Janeiro de 2025)

---

### Capítulo 1: Introdução

O Capítulo 1 define os sistemas distribuídos e delineia os objetivos de design e as classificações desses sistemas complexos.

**1.1 De Sistemas em Rede a Sistemas Distribuídos**

* **Definição:** Um sistema distribuído é uma coleção de sistemas de computador em rede, onde processos e recursos estão espalhados por diferentes máquinas.
* **Distinção Fundamental:** Os sistemas distribuídos são primariamente relacionados à visão expansiva de sistemas de computador em rede. A decentralização nunca deve ser um objetivo em si; a distribuição deve ser impulsionada pela necessidade e suficiência de espalhar processos e recursos para melhorar o desempenho, a confiabilidade e a escalabilidade.
* **Exemplos de Distribuição vs. Descentralização:**
    * **Google Mail:** Exemplo de um sistema distribuído implementado por uma vasta coleção de computadores para garantir escalabilidade e tolerância a falhas.
    * **Distributed Ledger (Blockchain):** Exemplo de um sistema descentralizado onde a propagação de processos e recursos é necessária devido à falta de confiança entre as partes participantes.
* **Complexidade Inerente:** Sistemas distribuídos são complexos devido a falhas parciais (componentes podem falhar isoladamente), natureza altamente dinâmica (nós entram e saem da rede) e vulnerabilidade a ataques de segurança.

**1.2 Objetivos de Design (Design Goals)**

O design de sistemas distribuídos visa atingir seis objetivos cruciais:

* **Compartilhamento de Recursos (Resource Sharing):** Permitir que usuários e aplicações em diferentes máquinas compartilhem recursos. Serviços como pastas compartilhadas na Internet tornam os dados acessíveis independentemente da localização ou organização do usuário.
* **Transparência de Distribuição (Distribution Transparency):** O objetivo é ocultar o fato de que processos e recursos estão distribuídos fisicamente, tornando-os invisíveis para usuários finais e aplicações, frequentemente usando middleware. Contudo, a latência geográfica (limitada pela velocidade da luz e atrasos de rede) é difícil de ocultar.
* **Abertura (Openness):** Um sistema aberto pode ser facilmente estendido ou modificado. Isso é alcançado organizando o sistema em componentes pequenos e substituíveis, interfaces bem definidas (frequentemente usando IDL - Interface Definition Language), e separando política e mecanismo.
* **Confiabilidade (Dependability):** Inclui disponibilidade, confiabilidade, segurança e manutenibilidade.
    * As falhas são classificadas como **transientes** (ocorrem uma vez e desaparecem), **intermitentes** (aparecem e desaparecem por conta própria, difíceis de diagnosticar) ou **permanentes**.
    * Métricas comuns incluem **Mean Time To Failure (MTTF)** e **Mean Time To Repair (MTTR)**.
* **Segurança (Security):** Garantir acesso autorizado.
    * Técnicas incluem **Criptografia** (chaves secretas $K_{A,B}$ e públicas $PK_A$).
    * **Assinaturas Digitais** são realizadas criptografando dados com a chave secreta do remetente ($SK_A(data)$), permitindo que qualquer parte verifique sua origem usando a chave pública $PK_A$.
    * **Blockchains** usam hashing para encadear blocos de dados, garantindo que qualquer alteração em um bloco exija a modificação de todos os blocos subsequentes (imutabilidade).
* **Escalabilidade (Scalability):** A capacidade de um sistema crescer.
    * **Dimensões:** Tamanho (adicionar usuários/recursos), Geográfica (distância entre usuários/recursos) e Administrativa (expansão através de múltiplos domínios organizacionais).
    * **Técnicas:** Particionamento e Distribuição (exemplo: o Domain Name System - DNS), Replicação e Ocultar Latências de Comunicação (usando comunicação assíncrona ou enviando código para o cliente, como JavaScript).

**1.3 Classificação Simples de Sistemas Distribuídos**

Os sistemas distribuídos são amplamente classificados em três áreas:

* **Computação Distribuída de Alto Desempenho (High-performance distributed computing):** Focada em melhorar o desempenho de programas intensivos em computação, incluindo **cluster computing** (sistemas com mais de 100.000 CPUs).
* **Sistemas de Informação Distribuída (Distributed information systems):** Concentra-se na integração de aplicações através de transações. O **Processamento de Transações Distribuídas** garante a propriedade **Atômica** (todas ou nenhuma operação são executadas). Um **TP monitor** coordena o commit (confirmação) de subtransações.
* **Sistemas Pervasivos (Pervasive systems):** Caracterizados por dispositivos pequenos, móveis, frequentemente conectados sem fio e alimentados por bateria, como na Internet das Coisas (IoT). Exemplos incluem **Ubiquitous Computing**, **Mobile Edge Computing (MEC)** (importante para baixa latência) e redes de sensores (frequentemente usando processamento in-network para agregar dados).

**1.4 Armadilhas (Pitfalls)**

Desenvolvedores inexperientes frequentemente cometem suposições falsas sobre redes, como assumir que a rede é confiável, que a latência é zero ou que a largura de banda é infinita. A maioria dos princípios em sistemas distribuídos visa resolver problemas decorrentes dessas premissas incorretas.

---

### Capítulo 2: Arquiteturas

O Capítulo 2 explora a organização lógica (estilos arquitetônicos) e a instanciação física (arquiteturas de sistema) de sistemas distribuídos.

**2.1 Estilos Arquitetônicos (Organização Lógica)**

Os estilos arquitetônicos definem a estrutura de componentes de software:

* **Arquiteturas em Camadas (Layered architectures):** Componentes organizados em camadas, onde chamadas (downcalls) são feitas para a camada inferior. Uma aplicação pode ser dividida em três camadas lógicas: Interface do Usuário, Processamento e Dados.
* **Arquiteturas Baseadas em Objetos (Object-based architectures):** Encapsulam dados (estado) e operações (métodos) em uma única entidade. Isso é atraente para ocultar detalhes de implementação e facilitar a substituição de componentes.
* **Arquiteturas Orientadas a Serviços (Service-oriented architectures - SOA):** Sistemas construídos como coleções de serviços.
    * **RESTful Architectures:** Subconjunto da SOA que segue princípios rigorosos, utilizando as mesmas interfaces para todas as operações (PUT, POST, GET, DELETE). A execução é stateless (sem estado).
* **Arquiteturas Publicar-Assinar (Publish-Subscribe):** Baseadas no **desacoplamento temporal** (processos não precisam estar ativos simultaneamente) e **referencial** (não se referenciam diretamente).
* **Espaços de Dados Compartilhados (Shared Data Spaces):** Como o modelo Linda, onde a comunicação ocorre via tuplas e operações de remoção (in(t)) ou cópia (rd(t)) são frequentemente blocking (bloqueadoras).
* Em sistemas Publicar-Assinar, a assinatura pode ser baseada em **tópicos** (pares atributo-valor) ou **conteúdo** (pares atributo-intervalo ou predicados complexos).

**2.3 Arquiteturas de Sistemas em Camadas**

A distribuição física das três camadas lógicas (Interface, Processamento, Dados) leva a arquiteturas em dois ou múltiplos níveis (multitiered).

* **Organização Cliente-Servidor (Client-Server):** Define como as camadas são distribuídas. **Clientes magros (thin clients)** mantêm a maior parte da lógica no servidor, facilitando o gerenciamento. **Clientes gordos (fat clients)** executam mais funcionalidades localmente, como em suites de escritório ou aplicações multimídia.
    * **Servidores:** Podem ser **iterativos** (o servidor trata o pedido) ou **concorrentes** (passa o pedido para um processo ou thread separado). Podem ser stateless (sem estado) ou stateful (mantendo estado, possivelmente usando cookies ou outros mecanismos).
* **Web (Arquitetura Multitiered):** Arquiteturas Web evoluíram de sistemas cliente-servidor simples de dois níveis para sistemas de múltiplos níveis, onde o conteúdo é dinamicamente gerado a partir de bases de dados e scripts (server-side scripts).

**2.4 Arquiteturas de Sistemas Simetricamente Distribuídos**

Caracterizadas por sistemas **Peer-to-Peer (P2P)**, onde todos os processos (servants) são clientes e servidores simultaneamente. São organizados em redes de sobreposição (overlay networks).

* **P2P Estruturados:** Utilizam topologias determinísticas (como hipercubos ou anéis) e funções de hashing (**DHT - Distributed Hash Tables**) para mapear chaves a nós responsáveis, permitindo buscas eficientes (ex: Chord, onde o caminho mais curto é da ordem $O(\log N)$).
* **P2P Não Estruturados:** Dependem de busca, geralmente via flooding ou random walks (caminhos aleatórios).
* **P2P Híbridos (Super Peers):** Utilizam nós especiais (**super peers**) que mantêm índices ou atuam como brokers, com peers regulares (weak peers) conectados a eles.

**2.5 Arquiteturas de Sistemas Híbridos**

Sistemas do mundo real que combinam centralização (Cliente-Servidor), P2P e hierarquia.

* **Cloud Computing:** Baseado em utility computing e caracteriza-se por um pool de recursos virtualizados, acessível através de um modelo pay-per-use. Oferece serviços em camadas: **Infraestrutura como Serviço (IaaS)** (ex: Amazon EC2), **Plataforma como Serviço (PaaS)** e **Software como Serviço (SaaS)**.
* **Edge-Cloud Architecture:** Surge com a IoT, posicionando infraestrutura (**Edge Computing** ou **Fog Computing**) entre os dispositivos finais e a nuvem. O **MEC** é essencial para aplicações sensíveis à latência.
* **Blockchain Architectures:** Sistemas descentralizados onde os participantes validam transações em blocos imutáveis. O consenso (que validador avança) pode ser centralizado, distribuído (grupo pré-selecionado) ou totalmente descentralizado.

---

### Capítulo 3: Processos

O Capítulo 3 trata de como os processos (e suas subunidades, threads) são gerenciados e organizados em sistemas distribuídos, incluindo mecanismos de virtualização, organização de clientes e servidores e migração de código.

**3.1 Threads**

* **Threads vs. Processos:**
    * **Context Switching (Troca de Contexto):** O uso de múltiplos processos, que cooperam através de mecanismos de Comunicação Interprocessual (IPC), exige uma extensa troca de contexto. Esta troca pode perturbar o cache e levar a uma perda de desempenho indireta de aproximadamente 80% em alguns casos.
    * **Paralelismo e Facilidade de Programação:** Threads permitem reter a ideia de processos sequenciais que fazem chamadas de sistema bloqueantes, facilitando a programação, ao mesmo tempo que alcançam paralelismo e melhoria de desempenho.
    * **Proteção:** O uso de múltiplos processos (multiprocess server) pode oferecer mais proteção do sistema operacional contra acesso acidental a dados compartilhados em comparação com threads.
* **Organização do Servidor (Server Architectures):** Existem três modelos principais para a construção de servidores:
    * **Multithreading:** Oferece paralelismo e utiliza chamadas de sistema bloqueantes, facilitando a programação.
    * **Processo Single-threaded:** Retém a simplicidade das chamadas bloqueantes, mas o desempenho pode ser gravemente prejudicado pela falta de paralelismo.
    * **Máquina de Estado Finito (Finite-state machine):** Alcança alto desempenho através do paralelismo, mas usa chamadas não bloqueantes (nonblocking calls), que são geralmente difíceis de programar e manter.

**3.2 Virtualização**

A virtualização permite que programas pareçam ser executados simultaneamente, criando uma ilusão de paralelismo em um único núcleo.

* **Princípio da Virtualização:** A essência é imitar interfaces de sistema, que incluem: **Instruction Set Architecture (ISA)** com instruções privilegiadas, chamadas de sistema e **Application Programming Interface (API)**.
* **Tipos de Máquinas Virtuais (VMs):**
    * **Process Virtual Machine (VM de Processo):** Nível de runtime, fornecendo um conjunto abstrato de instruções para a execução de um único processo (exemplo: ambiente Java).
    * **Native Virtual Machine Monitor (VMM Nativa):** Camada implementada diretamente sobre o hardware, oferecendo o conjunto completo de instruções do hardware.
    * **Hosted Virtual Machine Monitor (VMM Hospedada):** É construída sobre um sistema operacional hospedeiro existente.
* **Containers (Contêineres):**
    * **Isolamento:** Uma forma especial de virtualização que fornece a uma aplicação seu próprio ambiente, isolado de outros, enquanto compartilha o mesmo sistema operacional.
    * **Mecanismos Chave:** O isolamento e controle de recursos são realizados através de **namespaces** (visão isolada do sistema) e **cgroups (control groups)**, que restringem a memória ou a prioridade de CPU que um contêiner pode usar.
    * **Comparação:** O desempenho dos contêineres tende a ser melhor para aplicações ligadas a I/O, embora a diferença de desempenho com VMs esteja diminuindo.

**3.4 Servidores, Clusters e Balanceamento de Carga**

* **Servidores Iterativos vs. Concorrentes:** Um servidor iterativo processa a requisição por conta própria. Um servidor concorrente passa a requisição para uma thread ou processo separado.
* **Arquitetura Multicamadas na Web:** Sites frequentemente usam uma arquitetura de três níveis: **Servidor Web** (entrada), **Servidor de Aplicação** (processamento) e **Servidor de Dados** (banco de dados/arquivos).
* **TCP Handoff:** Em clusters de servidores, um switch de camada 4 ou 7 pode atuar como ponto de entrada. O TCP handoff permite que o switch distribua a carga (ex: política round robin). É particularmente eficaz quando as respostas são muito maiores do que as requisições.

**3.5 Migração de Código (Code Migration)**

A migração de código é o movimento de segmentos de um processo para outro nó da rede, visando otimizar a capacidade de computação ou minimizar a comunicação.

* **Motivações:**
    * **Computação de Borda (Edge Computing):** Enviar código para o servidor onde os dados residem pode ser melhor para minimizar a comunicação.
    * **Federated Learning (Aprendizado Federado):** Traz o modelo de treinamento (código) para os dados sensíveis (por exemplo, fotos pessoais) em vez de centralizar os dados.
    * **Flexibilidade:** Permite configurar sistemas distribuídos dinamicamente, como em sistemas de arquivos onde a implementação do protocolo cliente-servidor é enviada ao cliente.
* **Segmentos do Processo:**
    * **Segmento de Código (Code Segment):** O conjunto de instruções do programa.
    * **Segmento de Recurso (Resource Segment):** Referências a recursos externos (arquivos, dispositivos).
    * **Segmento de Execução (Execution Segment):** Estado atual da execução (dados privados, pilha, contador de programa).
* **Paradigmas de Mobilidade de Código:**
    | Paradigma | Iniciador | Migra | Modifica Estado |
    | :--- | :--- | :--- | :--- |
    | Client-Server (CS) | Cliente | Nenhum | Servidor |
    | Remote Evaluation (REV) | Remetente (Cliente) | Código | Servidor |
    | Code-on-Demand (CoD) | Receptor (Cliente) | Código | Cliente |
    | Mobile Agents (MA) | Remetente (Cliente) | Código + Estado | Cliente + Servidor |
* **Mobilidade Fraca (Weak Mobility):** Apenas o segmento de código é migrado (ex: Java applets).
* **Mobilidade Forte (Strong Mobility):** Migração do código e do estado de execução.
* **Migração de Máquinas Virtuais (VMs):** A migração de VMs é crucial em ambientes de cloud computing.
    * A abordagem **pre-copy (pré-cópia)**, que copia páginas de memória antes de um breve período de parada (stop-and-copy), resulta em um downtime de serviço muito baixo.

---

### Capítulo 4: Comunicação

O Capítulo 4 explora as bases da comunicação em sistemas distribuídos, desde os protocolos em camadas até os modelos de comunicação de alto nível.

**4.1 Fundamentos**

* **Protocolos em Camadas:**
    * A comunicação é estruturada em protocolos em camadas. O Modelo OSI define sete camadas, mas na prática, apenas as camadas inferiores e a Camada de Aplicação são usadas, sendo o restante agrupado no Internet Protocol Suite.
    * **Modelo de Referência Adaptado:** O middleware é tratado como uma camada adicional que contém protocolos independentes de aplicação (serviços de comunicação de alto nível, como RPC).
* **Tipos de Comunicação de Middleware:**
    * **Comunicação Transiente vs. Persistente:**
        * **Transiente (Transient):** A mensagem é armazenada pelo middleware apenas enquanto o remetente e o receptor estiverem em execução.
        * **Persistente (Persistent):** A mensagem é armazenada até ser entregue, permitindo que o remetente e o receptor estejam desacoplados no tempo (não precisam estar ativos simultaneamente).
    * **Sincronização:** O remetente pode bloquear até a submissão do pedido, a entrega ao destinatário, ou o processamento completo do pedido (retorno de uma resposta).

**4.2 Chamada de Procedimento Remoto (Remote Procedure Call - RPC)**

O RPC é um modelo de comunicação ideal para aplicações cliente-servidor que visa ocultar as complexidades da passagem de mensagens, realizando o que é conhecido como transparência de acesso.

* **Mecanismo:** O cliente invoca um **stub (coto)** que é responsável por empacotar (**marshalling**) os parâmetros para a rede. O stub do lado do servidor (também chamado de **skeleton**) desempacota (**unmarshalling**) os dados e invoca o procedimento localmente.
* **Assincronia e Multicast:**
    * **RPC Assíncrono:** O cliente envia a requisição e continua processando. O resultado é retornado por um callback.
    * **Multicast RPC:** Envia uma requisição RPC para um grupo de servidores, que processam o pedido de forma independente e paralela, retornando o resultado via callback.

**4.3 Comunicação Orientada a Mensagens (Message-Oriented Communication - MOM)**

A MOM é adequada quando a comunicação não pode ser estruturada em termos de chamadas e retornos.

* **Comunicação Transient:**
    * **MPI (Message Passing Interface):** Usado para programação paralela. Oferece operações de envio e recebimento, incluindo modos assíncronos (ex: MPI_BSEND copia a mensagem para um buffer local e permite que o remetente continue) e bloqueantes (MPI_RECV).
* **Comunicação Persistent (Message Queuing Systems - MQS):**
    * **Desacoplamento Temporal:** A característica mais importante é o desacoplamento temporal: a mensagem permanece na fila mesmo que o remetente e o receptor não estejam ativos.
    * **AMQP (Advanced Message Queuing Protocol):** Um exemplo de MQS que utiliza **exchanges (trocas)** para rotear mensagens e **queues (filas)** para armazená-las. As filas são ligadas às trocas por chaves de roteamento (ex: example-key).

**4.4 Comunicação Multicast**

Envolve a disseminação de informações de um remetente para múltiplos receptores.

* **Árvores de Multicast em Nível de Aplicação:** Soluções dinâmicas de P2P podem configurar árvores eficientes. O sistema Scribe, construído sobre Chord (um DHT), usa a topologia lógica para rotear mensagens de forma eficiente, com caminhos de ordem $O(\log N)$.
* **Métricas de Desempenho:** A qualidade de uma árvore é medida por **link stress** (quantas vezes um pacote atravessa o mesmo link físico) e **stretch** (relação entre o atraso real e o atraso no nível de rede).
* **Flooding (Inundação):** Transmite mensagens para todos os vizinhos. Embora robusto, pode ser ineficiente.
    * **Flooding Probabilístico:** Para economizar largura de banda, um nó retransmite uma mensagem com uma probabilidade $p_{\text{flood}}$.
* **Epidemic Protocols (Gossiping):** Técnicas robustas para disseminação de dados, inspiradas na propagação de doenças.
    * **Anti-entropy:** Processos trocam atualizações periodicamente. Pode ser **pull-based** (puxar atualizações), **push-based** (empurrar) ou **push-pull** (o mais rápido).

---

### Capítulo 5: Coordenação

O Capítulo 5 foca em mecanismos essenciais para a coordenação de processos em sistemas distribuídos, incluindo a sincronização do tempo, a exclusão mútua e a eleição de líderes.

**5.1 Sincronização de Relógios (Clock Synchronization)**

* **Necessidade:** Em sistemas centralizados, o tempo é não ambíguo. Em sistemas distribuídos, é crucial alcançar um acordo sobre o tempo, mesmo que não seja o tempo real absoluto.
* **Relógios Físicos:** São baseados em cristais de quartzo que oscilam em uma frequência definida, gerando interrupções (clock ticks).
    * **Padrões de Tempo:** **TAI (International Atomic Time)** e **UTC (Coordinated Universal Time)**.
    * **Drift Rate:** O software clock $C$ deve ter uma taxa de desvio ($\rho$) limitada. Para garantir uma precisão $\pi$ entre quaisquer dois relógios, eles devem ser ressincronizados no mínimo a cada $\pi/(2\rho)$ segundos.
* **Protocolos de Sincronização:**
    * **NTP (Network Time Protocol):** Permite que clientes contatem um servidor de tempo (timeserver). O servidor calcula o **offset** ($\theta$) e a estimativa de **delay** ($\delta$) com base em quatro timestamps ($T_1, T_2, T_3, T_4$). O NTP usa **strata (camadas)** para hierarquizar a precisão, onde servidores de estrato mais baixo (ex: estrato-1, usando um receptor UTC) são mais precisos. Ajustes de tempo devem ser feitos gradualmente (ex: adicionando 9ms em vez de 10ms por interrupt) para evitar problemas de causalidade.
    * **RBS (Reference Broadcast Synchronization):** Usado em redes de sensores, foca em permitir que os receptores ajustem seus relógios usando uma mensagem de referência broadcast do remetente, beneficiando-se do tempo de propagação aproximadamente constante.

**5.2 Relógios Lógicos (Logical Clocks)**

* **Happens-Before ($\rightarrow$):** Relação fundamental em relógios lógicos. $a \rightarrow b$ significa que todos concordam que o evento $a$ ocorreu antes do evento $b$. Eventos não relacionados são concorrentes.
* **Relógios de Lamport (Lamport’s Logical Clocks):**
    * **Propriedade:** Se $a \rightarrow b$, então $C(a) < C(b)$.
    * **Mecanismo:** Cada processo $P_i$ mantém um contador $C_i$.
        1.  Incrementa $C_i$ antes de cada evento.
        2.  Envia $ts(m) = C_i$ com a mensagem $m$.
        3.  Ao receber $m$, $P_j$ ajusta $C_j \leftarrow \max{C_j, ts(m)}$ e então executa o passo 1.
    * **Aplicações:** Usado para **Totally Ordered Multicasting (Multicast Totalmente Ordenado)**, crucial para manter réplicas de um banco de dados em estado consistente, garantindo que as atualizações cheguem na mesma ordem em todos os lugares. Também pode ser usado para Exclusão Mútua.
* **Relógios Vetoriais (Vector Clocks):**
    * **Propriedade:** Captura a causalidade potencial.
    * **Mecanismo:** Cada $P_i$ mantém um vetor $VC_i$. $VC_i[i]$ é o relógio local. Ao receber $m$, $P_j$ mescla o histórico causal definindo $VC_j[k] \leftarrow \max{VC_j[k], ts(m)[k]}$ para todo $k$.
    * **Uso:** Permite a detecção de potencial causalidade entre mensagens e é usado para impor **Causally Ordered Multicasting (Multicast Causalmente Ordenado)**.

**5.3 Exclusão Mútua (Mutual Exclusion)**

O objetivo é garantir que apenas um processo acesse uma região crítica por vez.

* **Algoritmo Centralizado:** Um coordenador único gerencia o acesso. Simples, mas cria um ponto único de falha.
* **Algoritmo Distribuído (Ricart & Agrawala):** Processos enviam mensagens de REQUEST com timestamps (Lamport's) a todos. O processo com o timestamp mais baixo ganha o acesso. Requer $2(N-1)$ mensagens por acesso/saída (requisições e mensagens OK).
* **Algoritmo de Anel de Token (Token-Ring):** Um token circula em um anel lógico; apenas o detentor do token pode entrar na região crítica.
* **Algoritmo Descentralizado:** Baseado em votação, um processo precisa obter permissão de uma maioria de coordenadores ($N_W > N/2$).
* **ZooKeeper:** Pode ser usado para bloqueio simples (simple locking), usando números de versão para prevenir que atualizações sejam baseadas em informações desatualizadas.

**5.4 Algoritmos de Eleição (Election Algorithms)**

Iniciados quando um processo detecta que o coordenador falhou.

* **Bully Algorithm:** Um processo $P_k$ envia ELECTION para todos os processos com IDs maiores. Se um ID mais alto responde, ele assume o controle. O processo com o ID mais alto em execução se torna o coordenador e envia uma mensagem COORDINATOR.
* **Ring Algorithm:** Uma mensagem ELECTION circula sequencialmente em um anel lógico, coletando IDs de todos os membros ativos. O ID mais alto na lista é o vencedor.
* **ZooKeeper/Raft:** Em Raft, servidores (em número pequeno, tipicamente cinco) operam em termos numerados, com um líder por termo. Servidores podem ser seguidores ou candidatos. Um candidato deve obter uma maioria de votos (incluindo o seu) para ser eleito líder. A elegibilidade para votar depende do status do log (termo mais recente e mais operações commitadas).

**5.5 Coordenação Baseada em Gossip (Gossip-based Coordination)**

Utiliza protocolos epidêmicos para propagar informações de forma robusta e descentralizada.

* **Agregação:** Processos trocam valores (e.g., $v_i, v_j \leftarrow (v_i + v_j)/2$), convergindo eventualmente para a média (útil para estimar o tamanho do sistema).
* **Peer-Sampling Service (PSS):** Mantém visões parciais (partial views) de vizinhos aleatoriamente selecionados.
* **Construção de Overlay:** Abordagem de duas camadas onde o PSS fornece aleatoriedade (camada baixa) e uma camada superior aplica funções de ranking (e.g., distância) para moldar a topologia lógica desejada (e.g., torus 2D).
* **Segurança:** A natureza rápida do gossiping torna-o vulnerável a ataques (ex: Sybil Attack), onde atacantes poluem as visões parciais com referências falsas. A solução requer forçar os atacantes a se comportarem corretamente de tempos em tempos.

**5.6 Casamento de Eventos Distribuídos (Distributed Event Matching)**

* **Sistemas Publish-Subscribe:** A comunicação é baseada em assinaturas.
* **Content-Based:** Assinaturas especificam valores ou intervalos de atributos. Filtros de Roteamento são criados para encaminhar notificações apenas para brokers relevantes.
* **Sub-2-Sub:** Combina gossiping com content-based matching ao particionar o espaço N-dimensional de atributos em subespaços, agrupando nós com interesses sobrepostos.

---

### Capítulo 6: Nomenclatura (Naming)

O Capítulo 6 explora como os recursos são nomeados, localizados e como as arquiteturas de roteamento são mantidas em sistemas distribuídos.

**6.2 Nomenclatura (Flat Naming)**

* **Chord Routing (DHT):** O sistema Chord (um Distributed Hash Table ou Tabela Hash Distribuída) organiza os nós em um anel lógico. A busca de uma chave $k$ é eficiente, ocorrendo em $O(\log N)$.
    * **Finger Tables (FT):** Usadas como atalhos para acelerar o roteamento. A correção do FT depende de procedimentos em segundo plano para checar o sucessor.
* **Proximity Routing:** Usa múltiplos sucessores para cada entrada na FT, permitindo que o nó selecione o caminho mais próximo a si mesmo sem "ultrapassar" o nó responsável pela chave.
* **Forwarding Pointers (Ponteiros de Encaminhamento):** Usados para gerenciar a localização de réplicas. Ao inserir ou atualizar um endereço em um domínio folha, uma cadeia de ponteiros é criada até um nó de diretório que já conhece o record da entidade.

**6.3 Nomenclatura Estruturada (Structured Naming)**

* **Resolução de Nomes (Name Resolution):** O processo de mapear um nome para um endereço.
    * **Resolução Iterativa:** O resolvedor do cliente envia a requisição ao nameserver, que retorna o endereço do próximo nameserver na hierarquia. O cliente repete o processo até obter a resolução completa (ex: DNS/FTP).
    * **Resolução Recursiva:** O nameserver de nível superior passa a resolução para o próximo nameserver, que faz o mesmo recursivamente, retornando o resultado final diretamente ao resolvedor do cliente inicial.
* **DNS Database:** Utiliza resource records como **NS** (servidores de nome) e **MX** (servidores de email, que têm uma prioridade de seleção).

**6.4 Nomenclatura Baseada em Atributos (Attribute-Based Naming)**

Nomes são resolvidos com base nos valores dos atributos de uma entidade.

* **Curvas de Preenchimento de Espaço (Space-Filling Curves):** Uma técnica, como a **Curva de Hilbert**, mapeia um espaço multidimensional (definido por atributos) em uma única dimensão (índice).
* **Vantagens/Desvantagens:** Suporta consultas de intervalo (range queries) facilmente. O lado negativo é que atualizações frequentemente precisam ser enviadas a múltiplos servidores e pode haver dificuldade em balancear a carga entre eles.

**6.5 Localização (Location)**

* **Sistemas de Localização:** Calcular a posição de um nó em um espaço m-dimensional requer $m+1$ medições de distância a nós com posições conhecidas (**landmarks**).
* **Centralized Positioning:** O nó $P$ mede a distância ($\tilde{d}$) a $m+1$ landmarks e resolve equações quadráticas para suas coordenadas, minimizando o erro agregado.
* **Vivaldi (Descentralizado):** Um sistema descentralizado que minimiza o erro agregado. A força $\vec{F}_{ij}$ que $P_i$ exerce sobre $P_j$ é proporcional à diferença entre a distância medida e a distância calculada. $P_i$ ajusta sua posição $\vec{x}_i \leftarrow \vec{x}_i + \delta \cdot \vec{u}$ para se mover na direção da força.
* **Outras Arquiteturas de Nomenclatura**
    * **NDN (Named Data Networking):** Roteadores NDN usam três componentes principais:
        * **Content Store:** Cache de dados.
        * **Pending Interest Table (PIT):** Rastreia requisições pendentes de dados.
        * **Forwarding Information Base (FIB):** Usada quando o roteador não pode atender a uma requisição localmente.

---

### Capítulo 7: Consistência e Replicação

O Capítulo 7 detalha a necessidade e os desafios da replicação de dados, introduzindo diversos modelos e protocolos de consistência.

**7.1 Introdução**

A replicação de dados é fundamental para melhorar a confiabilidade ou aumentar o desempenho de um sistema distribuído. O principal desafio é manter as réplicas consistentes, garantindo que as atualizações sejam propagadas de forma que as inconsistências temporárias não sejam notadas. Para atingir soluções eficientes, é frequentemente necessário relaxar a consistência.

**7.2 Modelos de Consistência Centrados em Dados**

Estes modelos definem o que pode ser esperado das operações de leitura e escrita em um data store distribuído.

* **Consistência Sequencial (Sequential Consistency):** Garante que todas as operações (leitura/escrita) se comportem como se fossem executadas em alguma ordem serial e que todos os processos vejam a mesma ordem de operações. A noção de tempo absoluto ("most recent") não é referenciada. Uma violação ocorre se os processos observarem diferentes interleavings de operações de escrita.
* **Linearizabilidade (Linearizability):** Uma forma mais rigorosa de consistência, que exige que o efeito de uma operação ocorra instantaneamente em algum momento entre o seu início e a sua conclusão.
* **Consistência Causal (Causal Consistency):** Distingue eventos potencialmente causalmente relacionados. Escritas causalmente relacionadas devem ser vistas por todos os processos na mesma ordem, enquanto escritas concorrentes podem ser vistas em ordem diferente em máquinas distintas.
* **Consistência Contínua (Continuous Consistency):** Permite que as aplicações especifiquem quanta inconsistência podem tolerar através de três eixos:
    * **Desvio Numérico (Numerical deviation):** Limita a variação nos valores das réplicas (ex: preços de ações). O desvio também pode ser medido pelo número de atualizações não vistas (weight).
    * **Desvio de Estagnação (Staleness deviation):** Relacionado ao tempo desde a última atualização da réplica (frequentemente usado em caches Web).
    * **Desvio de Ordenação (Ordering deviation):** O número máximo de escritas tentativas que podem estar pendentes em um servidor antes de serem sincronizadas.
    * **Conit:** Unidade de consistência (consistency unit) sobre a qual o desvio é medido.
* **Consistência Eventual (Eventual Consistency):** Modelo fraco e fácil de implementar. Garante que, se não houver mais atualizações, todas as réplicas convergirão para o mesmo valor.

**7.3 Modelos de Consistência Centrados no Cliente**

Estes modelos garantem que um único cliente veja um comportamento consistente, mesmo que acesse réplicas diferentes do data store.

* **Leituras Monotônicas (Monotonic Reads):** Um cliente que lê uma versão de dados nunca lerá uma versão anterior em leituras subsequentes.
* **Escritas Monotônicas (Monotonic Writes):** As operações de escrita de um cliente são realizadas na ordem em que foram iniciadas.
* **Leitura das Suas Escritas (Read Your Writes):** Uma operação de leitura de um cliente deve sempre refletir os efeitos de suas próprias operações de escrita anteriores.
* **Escritas Após Leituras (Writes Follow Reads):** Uma escrita que segue uma leitura é garantida de ocorrer sobre o mesmo valor ou um valor mais recente do que o lido. Útil, por exemplo, para garantir que a reação a um artigo de notícias seja postada somente depois que o artigo original tenha sido visto.
* **Implementação:** A implementação ingênua requer o rastreamento do conjunto de leituras (read set) e do conjunto de escritas (write set) para cada cliente, ou o uso de vetores de timestamps associados a sessões para manter estes conjuntos gerenciáveis.

**7.5 Protocolos de Consistência**

Os protocolos são as implementações dos modelos de consistência:

* **Protocolos Baseados em Primário (Primary-based):** Para consistência sequencial, todas as escritas são direcionadas a um único servidor.
    * **Remote-write:** O primário é fixo e coordena as atualizações das réplicas de backup.
    * **Local-write:** A cópia primária migra para o processo que deseja realizar a operação de escrita.
* **Protocolos de Escrita Replicada (Replicated-write):** Permitem que as escritas sejam realizadas em várias réplicas.
    * **Replicação Ativa (Active Replication):** Envia a operação para todas as réplicas, que as executam. Requer um mecanismo de multicast totalmente ordenado, frequentemente alcançado por um sequencer (coordenador central que atribui números de sequência).
* **Protocolos Baseados em Quorum:** Usam votação. Um cliente deve obter permissão de um quorum de leitura ($N_R$) e um quorum de escrita ($N_W$). Para evitar conflitos R/W, é necessário $N_R + N_W > N$ (onde $N$ é o total de réplicas), e para evitar conflitos W/W, $N_W > N/2$.
    * **ROWA (Read-One, Write-All):** Um caso especial com $N_R = 1$ (leitura rápida) e $N_W = N$ (escrita lenta).

---

### Capítulo 8: Tolerância a Falhas (Fault Tolerance)

O Capítulo 8 aborda a resiliência de processos e a comunicação confiável em face de falhas, com foco em algoritmos de consenso.

**8.1 Introdução à Tolerância a Falhas**

* **Conceitos Fundamentais:** A tolerância a falhas está ligada à dependabilidade (disponibilidade, confiabilidade, segurança e manutenibilidade).
* **Métricas Tradicionais:** **Mean Time To Failure (MTTF)**, **Mean Time To Repair (MTTR)** e **Mean Time Between Failures (MTBF)**. A Disponibilidade ($A$) é calculada como $MTTF / MTBF$.
* **Modelos de Falha:**
    * **Falha de Crash (Crash failure):** O servidor para, mas funcionava corretamente até parar.
    * **Falha de Omissão (Omission failure):** Falha ao responder (omissão de recebimento ou envio).
    * **Falha Arbitrária (Arbitrary failure/Byzantine):** O servidor pode produzir respostas arbitrárias em momentos arbitrários. Lidar com este tipo de falha é o pior cenário.
* **Mascaramento de Falhas (Redundância):** A técnica chave é a redundância física. Um exemplo é a **Triple Modular Redundancy (TMR)**, que usa três dispositivos replicados e votadores triplicados para mascarar falhas.

**8.2 Resiliência de Processos**

A resiliência é alcançada organizando processos idênticos em grupos de processos.

* **Organização de Grupo:** Pode ser plana (todos os processos iguais, sem líder, ex: P2P) ou hierárquica (um coordenador, os outros são trabalhadores, ex: primário-backup).
* **Consenso:** Para que um grupo de processos tolerante a falhas funcione como um único processo robusto, todos os processos não-falhos devem executar os mesmos comandos, na mesma ordem.
* **Consenso com Falhas de Crash:** É necessário um grupo de $2k + 1$ servidores para sobreviver a $k$ membros com falhas de crash.
    * **Paxos:** Algoritmo robusto de consenso. O processo é dividido logicamente em **Proposer** (proponente), **Acceptor** (aceitador/votante) e **Learner** (aprendiz/executor). Garante segurança (safety) (somente operações propostas são aprendidas) e vivacidade condicional (conditional liveness). Um proponente deve obter uma maioria de promessas/aceites usando timestamps de proposta.
    * **Raft:** Opera em termos, com um líder por termo. O líder conceitualmente envia o log (registro) aos seguidores e, ao receber uma maioria de reconhecimentos, executa e consolida (**commit**) a operação.
* **Consenso com Falhas Arbitrárias (Byzantine):** Requer pelo menos $3k + 1$ servidores para sobreviver a $k$ falhas arbitrárias. O **PBFT (Practical Byzantine Fault Tolerance)** usa um modelo primário-backup onde o consenso é alcançado quando um servidor não-falho registra $2k + 1$ mensagens correspondentes (pre-prepare, prepare, commit).
* **Limitações:** O consenso é impossível em sistemas assíncronos nos quais as mensagens não podem ser garantidamente entregues em um tempo finito conhecido, se houver apenas um processo com falha silenciosa.

**8.3 e 8.4 Comunicação Confiável**

* **Semântica de RPC em Falhas:** Falhas de servidor podem ocorrer antes ou depois da execução de uma operação.
    * **At-least-once semantics:** Tenta a operação repetidamente, mas é perigoso para operações não idempotentes (que causam efeitos colaterais se repetidas, ex: transferência de dinheiro).
    * **Idempotency:** A propriedade de um pedido que pode ser repetido com segurança sem causar danos (ex: leitura de dados).
* **Multicast Confiável Escalável:** Para grandes grupos, é preciso reduzir o número de mensagens de feedback.
    * **Feedback Suppression (SRM):** Os receptores enviam apenas **NACKs** (reconhecimentos negativos) se uma mensagem for perdida. O feedback é enviado com um atraso aleatório, permitindo que outros receptores suprimam os pedidos de retransmissão duplicados.
* **Virtual Synchrony:** Modelo de execução que define o multicast confiável em termos de visões de grupo (group views) e mudanças de visão (view changes). Garante que uma mensagem multicast para uma visão $G$ é entregue a todos os membros não-falhos ou a nenhum. Multicast virtualmente síncrono com entrega totalmente ordenada é chamado **Atomic Multicasting**.
    * **Atomic Multicasting:** Garante entrega all-or-nothing e entrega totalmente ordenada a todos os membros não-falhos.

**8.5 Commit Distribuído**

O problema de **distributed commit (consolidação distribuída)** exige que uma operação seja realizada por todos os membros de um grupo, ou por nenhum.

* **Two-Phase Commit (2PC):** Protocolo de commit. O coordenador coleta votos; se todos votarem commit, envia a mensagem GLOBAL-COMMIT. O principal problema é que os participantes podem ficar bloqueados na fase READY se o coordenador falhar.
* **Three-Phase Commit (3PC):** Adiciona um estado PRECOMMIT para evitar bloqueios na presença de falhas fail-stop.

**8.6 Recuperação**

A recuperação envolve restaurar um processo falho para um estado correto.

* **Backward Recovery:** Traz o sistema de volta a um estado correto previamente registrado, chamado **checkpoint**.
* **Checkpointing Independente:** Se cada processo salva seu estado de forma não coordenada, um crash pode levar ao **efeito dominó (domino effect)**, forçando a reversão de todos os processos ao estado inicial consistente.

---

### Capítulo 9: Segurança

O Capítulo 9 aborda os pilares da segurança e as técnicas criptográficas aplicadas a sistemas distribuídos.

**9.1 Introdução à Segurança**

A segurança envolve garantir **confidencialidade, integridade e disponibilidade**.

**9.2 Criptografia**

* **Homomorphic Encryption (HE):** Permite realizar operações matemáticas em dados criptografados ($E_K(x) \star E_K(y) = E_K(x \star y)$), sem que o servidor precise acessar o texto simples. Isso é crucial para computação em servidores não confiáveis.
* **Oblivious Transfer (OT):** Protocolo criptográfico onde Alice envia $N$ mensagens, mas Bob recebe apenas uma, e Alice não sabe qual.

**9.3 Autenticação**

* **Ataque de Reflexão (Reflection Attack):** Um exemplo de ataque que derrota protocolos de autenticação que usam desafios (challenges) idênticos para o iniciador e o respondedor.

**9.4 Confiança em Sistemas Distribuídos**

* **Sybil Attack:** O atacante cria múltiplas identidades falsas (Sybil nodes), violando a premissa de que cada entidade tem no máximo um identificador. O objetivo é obter influência desproporcional. O PSS (Peer-Sampling Service) pode ser vulnerável, necessitando de medidas para forçar o comportamento correto dos atacantes.

**9.5 Autorização**

O controle de acesso em sistemas distribuídos pode ser gerenciado de diversas formas:

* **Matriz de Controle de Acesso (Access Control Matrix):** Sujeitos vs. Objetos.
* **Capacidades (Capabilities):** Lista de direitos que um sujeito tem para cada objeto (como um bilhete), frequentemente protegida por uma assinatura digital.
* **MAC (Mandatory Access Control):** Impede o vazamento de informações de níveis de segurança mais altos para mais baixos.
* **WAVE:** Serviço de autorização descentralizada, focado em escalabilidade administrativa para operar em múltiplas unidades organizacionais.