# Sistemas Distribuídos

Escala que os desenvolvedores se preocupam -> escala de tamanho
    - capacidade computacional, limitada pelas CPUs
    - capacidade de armazenamento, incluindo a taxa de transferência entre CPU e discos 
    - A rede entre o usuário e o serviço centralizado
- Middleware -> camada no meio entre a aplicação e o sistema operacional que serve para a comunicação
- Serviços essenciais:
    1. Comunicação: permite a um nó se comunicar com outro
    2. Transação: possibilita executar no modo tudo ou nada, de forma atômica
    3. Composição de serviços: junção de funções
    4. Confiabilidade: envio de mensagens sendo recebidas por todos os processos ou nenhum

- Transparência:
    - Acesso: esconder diferenças na representação de dados e como um objeto é acessado
    - Localização: esconder que um objeto é localizado
    - Migração: esconder que um objeto pode se mover para outra localização
    - Replicação: esconder que um objeto é replicado
    - Falha: esconder a falha e a recuperação de um objeto

- Estilos Arquiteturais 
    1. Camadas: 
    2. Objetos e Serviços: 