# Angular

https://material.angular.io/components/categories

Criação de SPAs: trabalha com uma arquitetura de front separada do back, utilizando api

Compõe a stack mean

```bash
#instalar o angular no linux
npm install -g @angular/cli

#criar projeto 
ng new <nome>

#testar o projeto
ng serve

#criar um componente
ng generate <nome>
#para importar o componente basta utilizar o seu selector em um html de outro componente

#para cr5iar dentro de uma pasta de componentes
ng generate component components/first-component
```

node_modules = dependências do projeto

src = onde vamos programar a aplicação

src/app = pasta principal para componentes, services e etc

componentes = ts (lógica - seria o controler), html (template - view), css (estilo - criado para o componente) e testes 

- do angular para o servidor
    
    o professor vai dar o servidor, nessa primeira entrega só vamos fazer uso do servidor
    json server
    o padrão hoje é o rest
    é uma representação de estado, desenvolvida no doutorado de alguém
    acronimo para representação de estado transacional
    usa os métodos que http sempre teve
    usa o protocolo http
    o json server implementa essa forma de trabalhar
    http é um protocolo de comunicação da web, conjunto de regra
    http tem requisições
    tem métodos, ou predicados
    GET
    POST
    DELETE
    PUT
    TRACE
    PATCH
    geralmente método/ação/verbo + recurso que quer fazer aquela ação
    recurso: geralmente ligado a página ou arquivo no servidor
    exemplo no json-server
    página public om index.html
    GET /public/index.html
    códigos → 200 sucesso, 404 não achou
    pega algo do servidor e não altera
    pode ter efeitos colaterais, exemplo (email lido o gmail atualiza dizendo que o usuario leu)
    Post - envia e normalmente envia no sentido de inserir algo novo
    ex: post de um usuário é um cadastro de usuario
    Put - altera algo existente, atualiza
    get usuario/1
    
    chave primária sintética: para não ter que fazer atualizações, não é uma chave “verdadeira”