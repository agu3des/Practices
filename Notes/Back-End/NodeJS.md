# NodeJS

PARA INSTALAÇÃO DO NODE NO WINDOWS

> https://github.com/agu3des/portfolio/tree/194731179ebe9ccd6d73268526bfaa781fdd1508/NodeJS
> 

[https://nodejs.org/en/download/current](https://nodejs.org/en/download/current)

PARA INSTALAÇÃO DO NODE NO LINUX

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install curl
# instala a fnm (Fast Node Manager, ou Gestor Rápido de Node)
curl -fsSL https://fnm.vercel.app/install | bash
# ativar a fnm
source ~/.bashrc
# decarregar e instalar a Node.js
fnm use --install-if-missing 22
# verifica se a versão correta da Node.js está no ambiente
node -v # deve imprimir `v22.11.0`
# verifica se a versão correta da npm está no ambiente
npm -v # deve imprimir `10.9.0`
```

```jsx
node -v
npm -v
```

LIBERAR O SUDO UBUNTU

```nasm
su root
```

NEXTJS

```jsx
npm install next@latest react@latest react-dom@latest
```

O node é um interpretador javascript que não depende do navegador

![Untitled](NodeJS%20f1f268adf3574643a74b78407ba1ec64/Untitled.png)

v8 é responsável por entender o javascript, a libuv é uma biblioteca que deu caracteríticas de uma linguagem back para o node

Vantagens: leve, pouco uso de memória ram e melhor aproveitamento da cpu. Utiliza javascript. Tem um dos maiores ecossistemas de bibliotecas, módulos e plug-ins do mundo

```jsx
console.log("Hello World!");

var nome = "Ananda"
var sobrenome = "Guedes"
console.log(nome+" "+sobrenome);

var num1 = 10
var num2 = 64
function sum(a,b){
    return a + b;
}
console.log(sum);
```

![Untitled](NodeJS%20f1f268adf3574643a74b78407ba1ec64/Untitled%201.png)

Mostra os erros como qualquer outro interpretador

### Módulos

Vou dividir o meu código de calculadora em 4 partes

```jsx
var sum = function(a,b){
    return a + b;
}

module.exports = sum;

//em outro arquivo
var somaFunc = require("./Somar");
```

### HTTP

'fs' - trabalhar com arquivos dentro do seu sistema operacional

```jsx
var http = require('http'); //web
//abrir um servidor http
http.createServer(function(req,res){res.end("Olá")}).listen(8081);
                //qual porta de rede você quer abrir
                //toda alteração até esse momento tem que fechar o servidor e rodar novamente
console.log("Servidor rodando!")

```

### EXPRESS

```powershell
npm install express --save
```

FrameWork: facilitar seu trabalho manipulando uma linguagem

Express conecta ao node

Função de callback é executada quando algo acontece, a partir do disparo de um evento

![Untitled](NodeJS%20f1f268adf3574643a74b78407ba1ec64/Untitled%202.png)

Erro por não ter rota definida

Criar um caminho → criar uma rota

![Untitled](NodeJS%20f1f268adf3574643a74b78407ba1ec64/Untitled%203.png)

tem que botar a barra no código

```jsx
const express = require("express"); //evitar que sobreescreva a variável e dê erro na aplicação
var app = express(); //cria uma intância, cópia inteira //é a principal desse sistema

app.get("/", function(req, res){
    res.send("Seja bem-vindo ao meu app");
});

app.get("/sobre", function(req, res){
    res.send("Minha página sobre");
});

app.get("/blog", function(req, res){
    res.send("Bem-vindo ao meu blog");
});

app.listen(8081, function(){
    console.log("Servidor rodando na url http://localhost:8081");
});//função do express, que pede um único parâmetro obrigatório, uma porta
//tem que ser a última do código para poderr rodar
```

### PARÂMETROS

Exibir o nome de uma pessoa utillizando parâmetros (valor dinâmico que o usuário consegue passar)

Botou o parametro obrigatoriamente tem que usar ele

```jsx
app.get("/ola/:nome", function(req, res){
    res.send("Ola!");
});
```

![Untitled](NodeJS%20f1f268adf3574643a74b78407ba1ec64/Untitled%204.png)

```jsx
app.get("/ola/:nome/:cargo", function(req, res){
    res.send(req.params);
});
```

//chamar a função send uma vez

### NODEMON

```powershell
npm install --save nodemon -g
```

automatiza as alterações

__dirname - diretório raiz da aplicação

```jsx
app.get("/sobre", function(req, res){
    //res.send("Minha página sobre");
    res.sendFile(__dirname+"/Html/sobre.html")
});

```

### MySQL

```powershell
npm install --save sequelize

npm install --save mysql2
```

Gerar uma tableta sql através do nodejs

### Model

Model é basicamente uma referência a sua tabela dentro do sequelize

Pode ser usado para criar tabelas dentro do node

![d4b3f47e-0f46-4585-a817-3f2f20e86491.jpg](NodeJS%20f1f268adf3574643a74b78407ba1ec64/d4b3f47e-0f46-4585-a817-3f2f20e86491.jpg)

```powershell
mysql -h localhost -u root -p
show databases
;
use livraria
show tables
describe postagens
```

Cria campos de controle: id (único), createat e updateat (data de criação e a última atualização)

### HandleBars

Não tem template html, por conta do main

```jsx
*const* handlebars = require('express-handlebars')
    //Template Engine                              //template padrão da sua aplicação
    app.engine('handlebars', handlebars({defaultLayout: 'main'}))
    app.set('view engine', 'handlebars')//usar o template handlebars pro engine
```