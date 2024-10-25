//Queremos saber qual a soma de todos os números num determinado intervalo de números.
// cria uma variável
let soma = 0;
let numAtual = 1;
// continua o laço enquanto a expressão for verdadeira
while(numAtual <= 10) {
  soma = soma + numAtual;
  numAtual++;
}
//função para logar no console do desenvolvedor o resultado
console.log(soma); //55
// não seria mais fácil o código abaixo?
//console.log(sum(range(1,10))); não reconhecido 


//--------------------------------------------------------------------------------------------//

//Um operador que informa qual o tipo de uma variável em Javascript é o typeof. 
console.log(typeof "javascript") //string
console.log(typeof 13) //number
console.log(typeof true) //boolean

//--------------------------------------------------------------------------------------------//


//Operações aritméticas
//Ordem na hora das operações faz diferença, logo prestar atenção com parênteses e precedência
console.log(10 + 5) //15
console.log(20 - 4) //16 
console.log(5 * 4) //20
console.log(15 / 5) //3
console.log(10 ** 2) //100


//--------------------------------------------------------------------------------------------//

//String é o tipo usado para representar texto. Em JS há 3 formas de representar.
console.log("Aqui é um texto")
console.log('Aqui é um texto')
console.log(`Aqui é um texto`)

//Dado um texto, podemos querer quebrar parte para ser apresentado em outra linha.
console.log("Este texto começa em uma linha...\ne conclui na outra")
//Se usarmos o caracter ` para envolver a string, basta dar uma quebra de linha na sua IDE que fará o mesmo efeito.
console.log(`Este texto começa em uma linha...
e conclui na outra`)

//--------------------------------------------------------------------------------------------//

//O uso do caracter ` indica que você está usando o que se chama template strings.
console.log(`A metade de 500 é ${500/2}`) //A metade de 500 é 250

//O que estiver entre ${} será executado como sendo uma expressão em JS. Pode ser uma expressão aritmética, booleana, ou mesmo uma variável a ser resolvida. 
//Por exemplo, se existir a variável nome="Gustavo", a string:
let nome="Ananda"
console.log(`Meu nome é ${nome}`) //Ananda

// Para saber qual o tamanho de uma string, usamos a propriedade length.
console.log(nome.length) //6

//--------------------------------------------------------------------------------------------//

//Concatenação: Strings não podem ser divididas, multiplicadas ou substraídas, porém, podemos usar o operador +.
console.log("java" + "script")

//--------------------------------------------------------------------------------------------//

//Podemos comentar nosso código utilizando comentários de linha simples //, ou comentários de múltiplas linhas /**/.

//--------------------------------------------------------------------------------------------//

// Distinguir valores entre verdadeiro ou falso, sim ou não, ligado e desligado. 
//Para esse tipo de necessidade JS tem os valores booleanos true e false.
console.log(1 < 2) //true
console.log(1 > 2) //false

console.log("java" < "javascript") //true
console.log("java" < "python") //true

console.log("carro" <= "terra") //true
console.log(10 >= 100) //false

console.log("java" != "java") //false --- diferente
console.log("java" === "java") //true --- identico

//--------------------------------------------------------------------------------------------//

//Operadores lógicos:  e (&&), ou (||) e not (!)

//Uma expressão com o operador && será true se os dois operandos tiverem o mesmo valor booleano. Caso contrário, será false. 
console.log(true && true)//true
console.log(true && false)//false
console.log(false && true)//false
console.log(false && false) //false

//No caso do operador ||, será verdadeiro se um dos operadores for verdadeiro. Veja:
console.log(true || true)//true
console.log(true || false)//true
console.log(false || true)//true
console.log(false || false) //false

//Já o operador ! inverte o valor booleano da expressão. Por exemplo, !true é false, e !false é true.
console.log("java" === "java") //true
//porém
console.log("java" != "java") //false


//Podemos misturar expressões booleanas com expressões aritméticas. Por exemplo:
console.log(10 < (50 + 1)) //true
console.log(100 === (10 ** 2)) //true

//--------------------------------------------------------------------------------------------//

//Criação de Variáveis/Constantes:  

let nomeDaVariavel;
//Perceba que, no exemplo acima, não foi definido o valor da variável nomeDaVariavel. Porém, quando uma variável não tem valor, como veremos no item 3.6.2, a variável terá o valor undefined.
//Se quisermos atribuir um valor ao se declarar uma variável, basta colocar um valor após o símbolo =. Veja abaixo:
let idade = 30; //definindo variável idade, com valor 30
//Podemos alterar a qualquer momento o valor de uma variável (o próprio nome já diz). Então, é válido a operação abaixo, após já ter criada a variável idade acima:
idade = 32; //mudando o valor da variável idade
//Podemos declarar, ao mesmo tempo, várias variáveis:
let x = 10, y = 20; //separamos as várias variáveis com uma vírgula
//Também podemos mudar o valor de uma variável numérica, por exemplo, fazendo operações aritméticas. Por exemplo:
let idade1 = 30;
idade1 += 2; //é o mesmo que idade = idade + 2
//Essa última linha muda o valor da variável idade, incrementando 2 ao seu valor.


//Como o próprio nome já diz, constantes são containers de valores que não permitem que seus valores sejam alterados após declarados. Para se declarar uma constante, utilizamos a palavra const.
const pi = 3.14;
//Não é permitido se declarar uma constante sem valor. A linha abaixo dará erro:
//const pi; //SyntaxError: Missing initializer in const declaration


//vazios: null e undefined. Ambos significam que não existe valor (falta valor). Eles podem ser usados de forma intercambiável, ou seja, significam a mesma coisa em JS. Porém, sugiro, se você quiser definir uma variável como vazio, use undefined:
let livro = undefined;

//--------------------------------------------------------------------------------------------//

//Conversões Automáticas:
console.log(9 * null); //0 pois o null se transforma em zero
console.log(9 * undefined); //NaN (not a number)
console.log("5" - 1); // 4 entende que é um number
console.log("5" + 1); //51 concatena string
console.log("cinco" * 10);


