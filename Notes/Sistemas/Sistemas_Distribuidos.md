# Sistemas Distribuídos

Escala que os desenvolvedores se preocupam -> escala de tamanho
    - campacidade computacional, limitada pelas CPUs
    - capacidade de armazenamento, incluindo a taxa de transferência entre CPU e discos 
    - A rede entre o usuário e o serviço centralizado

### **Resumo - Capítulo 1**

**Definição:** uma coleção de computadores independentes que se apresenta aos usuários como um sistema único e coerente.

A chave é **coerência**, a distribuição dos componentes é invisível para o usuário final, que interage com o sistema como se ele fosse monolítico.

Composto por vários nós conectados em rede que suporte falhas parciais.

- Cloud Computing → redundância
- HPC → chekpoint

**Objetivos:** 

1. Facilidade de acesso a recursos: permitir que usuários e aplicações compartilhem e acessem recursos remotos de forma controlada e eficiente. Ex: impressoras, arquivos…
2. Transparência de distribuição: ocultar do usuário o fato de que os recursos e processos estão espalhados por uma rede. Existem vários tipos de transparência, como transparência de localização (o usuário não precisa saber onde um recurso está) e transparência de falhas (o sistema lida com falhas de componentes de forma que o usuário não seja afetado).
    1. *Acesso* - oculta as diferencias na representação dos dados e na forma como os recursos  são acessados. Ex: acessar um arquivo local e um arquivo remoto com a mesma sintaxe.
    2. *Migração* - oculta a movimentação de um recurso de um local para outro. Um recurso pode mudar de local sem que o usuário perceba.
    3. *Replicação* - oculta o fato de que múltiplos recursos estão sendo utilizados para garantir confiabilidade ou melhorar o desempenho. 
    4. *Concorrência* - oculta as interações de múltiplos processos ou usuários acessando o mesmo recurso  simultaneamente.
    5. *Falha* - oculta a falha e recuperação de um componente, permitindo que o sistema continue a funcionar.
    6. *Performance* - oculta a otimização de performance, como o balanceamento de carga, do usuário.
    7. *Escalonamento* - permite que o sistema expanda sua capacidade sem alterar a estrutura da aplicação ou a interação do usuário. 
3. Abertura: a capacidade de um sistema ser facilmente estendido ou modificado, permitindo que componentes de diferentes desenvolvedores e sistemas operacionais interajam, podem ser adicionados e interoperar, usando interfaces e protocolos padrão e bem definidos.
4. Escalabilidade: a capacidade de um sistema lidar com um aumento na carga de trabalho e no número de usuários ou recursos de forma eficiente, sem degradar o desempenho. Não é apenas sobre o número de máquinas, mas também sobre a capacidade de lidar com um aumento na rede e nos domínios administrativos.

**Desafios e Complexidades:**

1. Ausência de um Relógio Global: não há um único relógio para sincronizar eventos em todo o sistema. Isso torna a ordenação de eventos um problema fundamental.
2. Falhas Parciais: uma parte do sistema pode falhar enquanto outras continuam a funcionar. Em um sistema centralizados, ou tudo funciona ou tudo para. Em um sistema distribuído, é preciso gerenciar essas falhas de forma resiliente.
3. Heterogeneidade: componentes de hardware, sistemas operacionais, linguagens de programação e redes diferentes precisam interagir. O middleware desempenha um papel crucial a superação desse desafio.
4. Segurança: é um problema complexo, pois o controle e a comunicação estão espalhados. Autenticação, autorização e proteção de dados são desafios maiores do que em sistemas centralizados.
5. Aberto e Escalável: abertura e escalabilidade, embora sejam objetivos, também trazem desafios. Um sistema aberto pode ser vulnerável a ataques, e um sistema escalável deve evitar pontos de gargalo (bottlenecks), como um único servidor de nome centralizado.

**Arquiteturas do Sistema:**

1. Arquitetura Cliente-Servidor: é o modelo mais tradicional, onde os clientes solicitam serviços e os servidores os fornecem. O servidor e um ponto central de controle e recurso, e as requisições são direções e bem definidas.
2. Arquitetura Peer-to-Peer (P2P): não há distinção entre clientes e servidores. Cada nó na rede pode atuar como cliente (solicitando um serviço) e como servidor (oferecendo um serviço). Isso cria uma rede descentralizada e resiliente, como as utilizadas para compartilhamento de arquivos. Podem ser estruturadas (com um design organizado que garante que um nó encontre qualquer recurso em um número fixo de passos) e não estruturadas (onde a busca por um recurso é aleatória ou baseada em inundações da rede).