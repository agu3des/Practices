Análise Arquitetural do Sistema RemoteList

1. Características e Limitações

Escalabilidade

O sistema apresenta limitações severas de escalabilidade vertical e horizontal devido à sua arquitetura centralizada e stateful:

Limitação de Memória (Vertical): Como todas as listas são mantidas em memória principal (map[int][]int) para garantir baixa latência, a capacidade do sistema é estritamente limitada pela RAM disponível no servidor.

Gargalo de Processamento (Concorrência): Embora a utilização de sync.RWMutex tenha otimizado leituras simultâneas, o servidor ainda é um ponto único de contenção. Operações de escrita (Append, Remove) bloqueiam exclusivamentetodas as listas, impedindo leituras durante aquele intervalo. Isso significa que um alto volume de escritas degradará a performance global linearmente.

Disponibilidade

O sistema opera com um Ponto Único de Falha (SPOF). Se o processo do servidor travar ou a máquina hospedeira falhar, o serviço torna-se 100% indisponível. A disponibilidade é diretamente afetada pelo MTTR (Mean Time To Recovery). Graças à estratégia híbrida implementada (Log + Snapshot), o tempo de reinicialização é otimizado, pois o servidor não precisa reprocessar todo o histórico de operações desde o início dos tempos, apenas as operações ocorridas após o último snapshot.

Consistência

O sistema oferece Consistência Forte (Strong Consistency). Como existe apenas uma instância do servidor e o acesso à memória é protegido por exclusão mútua (Mutex), todos os clientes visualizam a mesma ordem de operações. Não há risco de leituras obsoletas ("stale reads") ou conflitos de versão, pois a "verdade" é única e reside na memória do processo atual.

2. Pontos de Falha e Tratamento de Erros

O sistema foi robustecido para lidar com as falhas mais críticas de persistência:

Falha no Processo/Energia (Crash): Se o servidor desligar abruptamente, os dados na memória RAM são perdidos.

Tratamento: O sistema utiliza um padrão de Write-Ahead Log (WAL). Cada operação de modificação é gravada no disco (operations.log) antes de retornar sucesso ao cliente. Ao reiniciar, o servidor reconstrói o estado da memória reexecutando este log.

Falha durante o Snapshot (Corrupção de Dados): Um ponto crítico de falha seria o servidor travar enquanto grava o arquivo de snapshot, deixando um arquivo corrompido e um log já truncado.

Tratamento: A solução implementada utiliza Gravação Atômica. O snapshot é gravado em um arquivo temporário (snapshot.tmp). Somente após o sucesso total dessa gravação, o sistema operacional renomeia o arquivo para o nome oficial (snapshot.json) e limpa o log. Isso garante que nunca existirá um estado inconsistente no disco.

Falha de Disco: Se o disco estiver cheio ou inacessível.

Tratamento: O servidor detecta o erro de I/O e retorna um erro via RPC para o cliente, impedindo que o cliente acredite que o dado foi salvo ("falso positivo").

3. Melhorias de Escalabilidade e Trade-offs

Para superar as limitações atuais, a arquitetura precisaria evoluir para um sistema distribuído real. Duas abordagens principais seriam:

A. Sharding (Particionamento)

Dividir as listas entre múltiplos servidores com base no ID da lista (ex: Listas 1-1000 no Servidor A, 1001-2000 no Servidor B).

Impacto na Consistência: Mantém a consistência forte por lista, pois cada lista ainda reside em um único servidor autoritativo.

Impacto na Disponibilidade: Melhora parcialmente. Se o Servidor A cair, apenas as listas dele ficam indisponíveis; as do Servidor B continuam acessíveis.

B. Replicação (Mestre-Escravo ou Consenso)

Ter múltiplas cópias do servidor contendo os mesmos dados.

Impacto na Consistência: Aqui reside o maior trade-off (Teorema CAP).

Se optarmos por replicar para aumentar a velocidade de leitura (clientes lendo de réplicas), podemos introduzir Consistência Eventual (um cliente pode ler um dado antigo que ainda não chegou na réplica).

Se exigirmos consistência forte em um ambiente replicado (usando algoritmos como Raft ou Paxos), a latência de escrita aumentará significativamente, pois o sistema precisará confirmar a gravação em várias máquinas antes de responder ao cliente.