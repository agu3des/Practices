# JavaScript

> https://github.com/agu3des/portfolio/tree/325db1a1dedd26aa756922acf1a5639176ce7cef/JavaScript
> 

[Programação Web 1](JavaScript%2044f16c284c1d4e87aaade365803a6d8a/Programa%C3%A7%C3%A3o%20Web%201%201292e5a697c380dcb1e9de8264d13dfd.md)

Install NodeJS → the same idea of idle from python

baixar um plugincliente http possa conversarrest cliente 

- plugin do vscodecomando de curl 

- dispara http e conversa com o supabasemétodos, rotas específicas

ferramentas: curl ou rest para testar se está transmitindo

get post e deletefecth é nativo, se for para programação

o axius e o supabase cliente são bibliotecas 

- o vite que tem a build toolsse não tem o build tools (npm install) 

vc procura o linka

nível profissional: build tools 

Data types:

![Untitled](JavaScript%2044f16c284c1d4e87aaade365803a6d8a/Untitled.png)

- number = 5 18.2 -15

Infinity

NaN

- string = ananda

- null

- undefined

- boolean = true false

- object

array

- function

typeof: como saber o tipo de uma variável

```jsx
var n1 = window.prompt('Digite um número:')
var n2 = window.prompt('Digite um número:')
var soma = n1 + n2
window.alert('A soma dos valores é '+ soma) // desse modo ele vai concatenar 

var idade = 19
var nome = 'Ananda'
var nota = 10
'A aluna '+nome +'com' +idade +'anos, tirou a nota ' +nota
`A aluna ${nome} com ${idade} anos, tirou a nota ${nota}`
```

number + numer soma
string + string concatena
no exemplo acima ele reconhece como duas strings
Number.parseInt() para número inteiro
Number.parseFloat() para ser um float
Number() vai para número de todo jeito
String() converte para string

var s =  ‘JavaScript’
‘Eu estou aprendendo s’ → não interpola
‘Eu estou aprendendo’ + s → concatena
‘Eu estou aprendendo ${s}’ → template string

s.length → tamanho

s.toUpperCase() → maiúsculas

s.toLowerCase() → minúsculas

n1.toFixed(2) → duas casa definidas

n1.toFIxed(2).replace(’.’,’,’) → substituir um por outo

n1.toLacaleString(’pt-BR’, {style: ‘currency’, currency: ‘BRL’})

**Operadores aritméticos**

Binários: estes precisam de aenas dois operandos, +, -, *, /, %, **

ex: 5+3/2 → segue a regra matemática de preferência

( ) > ** > * / % > + - 

nas que forem iguais começa pela esquerda ou seja quem aparece primeiro

Auto-atribuições: var n = 3, n = n+4, n += 5

Para todos os outros operadores aritméticos é válido esse tipo de sintexe

n++ ou  n- - ou ++n e - -n

**Operadores relacionais**

```jsx
    m > n,
    m < n,
    m >= n,
    m <= n,
    m == n,
    m != n
```

```jsx
console.log(
    5 == 5, //true
    5 == '5', //true !=
    //Não testa o tipo e sim o mesmo valor/grandeza
    5 === '5' //false !==
    //mesmo valor e mesmo tipo
)
```

**Operadores lógicos**

! negação

&& conjunção

|| disjunção

![Untitled](JavaScript%2044f16c284c1d4e87aaade365803a6d8a/Untitled%201.png)

**Operadores ternário**

? :

![Untitled](JavaScript%2044f16c284c1d4e87aaade365803a6d8a/Untitled%202.png)

```jsx
function calcularMedia(n1,n2,n3){
    const media = (n1+n2+n3)/3;
    return media;
}
const nota1 = 7;
const nota2 = 3;
const nota3 = 5;
let media = calcularMedia(nota1,nota2,nota3);
console.log("Média = "+media);
console.log("Situação =",media >= 7 ? "Aprovado" : "Reprovado");
media += 3;
console.log("Média = "+media); 
console.log("Situação =",media >= 7 ? "Aprovado" : "Reprovado");
```

### DOM

Versão web para o qual javascript foi criado

Document Object Model

Árvore DOM do site

Raiz - window

Por marca - getElementsByTagName()

Por Id - getElementById()

Por nome - getElementsByName()

Por classe - getElementsByClassName()

Por seletor - querySelector() querySelectorAll()

![Untitled](JavaScript%2044f16c284c1d4e87aaade365803a6d8a/Untitled%203.png)

### API

- traz dados
- Interface
- interface são nomes de métodos quando falamos das linguagens
- api web (http)
- interface - url
- urls podem ser projetadas para terem retornos específicos
- Rest cliente

- JS (fetch - função que pode consumir)
- Toda comunicação vem através de http - os dados vem por json
- Serveless - ‘não tem’ backend
- preciso saber o domínio ou seja a url que irá indicar e o token
- Rest API: métodos específicos para fazer o crud

```jsx
npm install supabase

"dependencies": {
    "@supabase/supabase-js": "^2.38.5",
```

Utilização do **regex**:

```jsx
const [email, setEmail] = useState('');

const [emailErr, setEmailErr] = useState(false);

const validate = async () => {
     if (!validEmail.test(email)) {
        setEmailErr(true);
     }
  }

export const validEmail = new RegExp('^[a-zA-Z0-9._:$!%-]+@[a-zA-Z0-9.-]+.[a-zA-Z]$');
```