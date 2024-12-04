== Objetivo ==
Alterar o código do sistema bancário para gerenciar clientes

== Preparação ==
1. Baixe o projeto e o descompacte;
2. Apague a pasta node_modules e o arquivo package-lock.json;
3. Dê um npm install na linha de comando na raiz do projeto. Deveria compilar e gerar a pasta node_modules com as dependências;
4. Dê um npm start para iniciar o node em watch mode;
5. Abra o arquivo index.html no navegador e teste a aplicação.

== Passos ==

Ponto de partida do seu código, baseado no código apresentado em sala: https://github.com/gugawag/banco-node/releases/tag/v7-armazenamento-contas-poupanca-contabonificada (se ainda não foi apresentado em sala, será nesta semana)

Agora é sua vez de alterar o sistema bancário. Precisamos gerenciar clientes do banco. Para isso, você deve:

1. Desenvolver a classe Cliente, contendo como atributos: nome, cpf e uma conta (apenas para simplificar), e seus respectivos métodos get e set;
2. Desenvolver a classe Clientes, que armazenará todos os clientes do banco num array de clientes (atributo da classe), e terá os seguintes métodos:
2.1 inserir, que recebe um parâmetro do tipo Cliente inserirá um cliente no array de clientes da classe Clientes
2.2 remover, que recebe um cpf e removerá o cliente daquele cpf, se existir
2.3 listar, que devolverá um array de Cliente
2.4 pesquisar, que receberá o cpf do cliente e devolverá o cliente encontrado (se encontrar)
3. Alterar o arquivo app.ts para criar um objeto da classe Clientes e inserir clientes dentro, listar, remover e pesquisar (pode fazer o código diretamente no app.ts e imprimir no console o resultado)
4. Criar o html clientes.html, que terá os inputs para acrescentar para inserir um novo cliente, e inserirá as referências para os arquivos .js necessários
5. Desenvolver a classe ClienteController, que fará a ponte entre a tela e as ações que podem ser feitas em clientes
6. Desenvolver a classe ClienteEspecial, que herda de Cliente e tem uma lista de dependentes (array de Cliente) (mas a tela de Cliente não precisa pensar em colocar os dependentes, apenas um cliente básico)

== O que entregar? ==
prints das novas classes criadas;
print do seu código executando;
O link do github de seu projeto.