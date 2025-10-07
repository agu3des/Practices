# Programação Web 1

# Revisão javascript:

[https://github.com/agu3des/practice](https://github.com/agu3des/practice)

| Operador | Descrição | Exemplo |
| --- | --- | --- |
| Adição (+) | Operador binário (precisa de dois operandos). Retorna a soma entre os números passados. | 10 + 5 retorna 15. |
| Subtração (-) | Operador binário. Retorna a subtração entre os números passados. | 20 - 4 retorna 16. |
| Multiplicação (*) | Operador binário. Retorna a multiplicação entre os números passados. | 5 * 4 retorna 20. |
| Divisão (/) | Operador binário. Retorna a divisão entre os números passados. | 20 / 4 retorna 5. |
| Módulo (%) | Operador binário. Retorna o inteiro restante da divisão dos dois operandos. | 12 % 5 retorna 2. |
| Incremento (++) | Operador unário. Adiciona um ao seu operando. Se usado como operador prefixado (`++x`), retorna o valor de seu operando após a adição. Se usado como operador pósfixado (`x++`), retorna o valor de seu operando antes da adição. | Se `x` é 3, então `++x` define `x` como 4 e retorna 4, enquanto `x++` retorna 3 e, somente então, define `x` como 4. |
| Decremento (--) | Operador unário. Subtrai um de seu operando. O valor de retorno é análogo àquele do operador de incremento. | Se `x` é 3, então `--x` define `x` como 2 e retorna 2, enquanto `x--` retorna 3 e, somente então, define `x` como 2. |
| Negação (-) | Operador unário. Retorna a negação de seu operando. | Se `x` é 3, então `-x` retorna -3. |
| Adição (+) | Operador unário. Tenta converter o operando em um número, sempre que possível. | +"3" retorna 3.
+true retorna 1. |
| Operador de exponenciação (**) | Calcula a base elevada á potência do expoente, que é, base`expoente` | 2 ** 3 retorna 8.
10 ** -1 retorna 0.1 |

|  | A | Comunica | B |  |
| --- | --- | --- | --- | --- |
| Pacote é envolvido em um nível de aplicação → navegador, coloca a porta | Aplicação  | Dns/http | Aplicação  |  |
| Recebe e é encapsulada | Transporte | Tcp/udp | Transporte |  |
| Recebe e é encapsulada | Rede | Ip | Rede |  |
| Recebe e é encapsulada | Enlace |  | Enlace | Recebe e descapsula |
| Recebe e é encapsulada | Física |  | Física | Recebe e descapsula |

Ip é o endereço 

Porta é a aplicação 

Não posso usar o pid pois ele muda, e a porta é um número fixo

Não pode usar portas de 1024 para baixo

Http 80 x Https 443

Ts não se executa em navegador

```jsx
let numeros = [1,2,3,4,5,6,7,8,9,10];
numeros.forEach(numero => concole.log(numero)); //arrow function
numeros.forEach(imprimeNumero);
function imprimeNumero(numero) {
     console.log(numero);
}
const x = imprimeNumero;
x(25);
numeros.filter(); //filtra para menor ou igual ao tamanho do Array
const numerosPares = numeros.filter(numero => (numero%2) === 0); // uma função que só retorna boolean é um predicado
for(let numero of numerosPares) { // se fosse in no lugar do of, ele imprimirá suas posições no array, seus índices 
       console.log(numero);
}

const nomes = ['Ana', 'Maria', 'Braga'];

const listNameElement = document.createElement('ul');
document.body,appendChild(listNameElement);
for(let nome of nomes){
   
}
nomes.forEach(nome => listNameElement.appendChild(document.createElement('li').textContent = nome))
//,map para cada elemento faça isso, geralmente transforma o que recebe, não muda o tamanho
//.reduce reduz para um número único de elementos,não altera os elementos em si
```

```jsx
const names = ['Ana', 'Maria', 'Braga'];

const listNameElement = document.createElement('ul');
document.body,appendChild(listNameElement);
for(let name of names){
   const liElement = document.createElement('li');
    liElement.textContent = name;
    listNameElement.appendChild(liElement);
}
names.forEach(name => listNameElement.appendChild(document.createElement('li').textContent = name))

function inputName() {
    const inputNameElement = document.querySelector('#name');
    const liElement = document.createElement('li');
    const nameDigitado = inputNameElement.value;
    liElement.textContent = nameDigitado;

    listNameElement.appendChild(liElement);

}
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>IFPB</h1>

    <script src="js/script.js"></script>
    <input id="name" placeholder="Name">
    <button onclick="inputName()">Input</button>
</body>
</html>
```

A const pode ter outro valor, mas n mudar a posição, o ponteiro

visão → controlador → serviço → repositório

controlador n tem acesso ao que fazer, ele n sabe criar um objeto usuário, ele recebe os atributos o serviço que faz isso