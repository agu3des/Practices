//Funções de entrada e saída
//Por exemplo, para que possamos pegar alguma informação do usuário, podemos usar a função prompt() (similar à função input() de Python).
let nome = prompt("Digite seu nome:");
console.log("Você digitou o nome:" + nome);
typeof prompt;

//Para se imprimir na tela do usuário uma mensagem, um alerta, podemos usar a função alert(). No console, digite:
alert("Olá");

//-----------------------------------------------------------------------------------------------------------------------//

//Transformando string em number, e vice-versa
//Às vezes, o desenvolvedor precisa transformar suas variáveis de um tipo para outro. Por exemplo, em:
console.log("10" + 2)
//se você quiser que o resultado seja a soma dos valores, não a concatenação entre "10" e "2", você pode fazer:
Number("10") + 2
//Similarmente, para você transformar algo em string, faz-se:
let idade = 20;
console.log("Eu tenho " + String(idade) + " anos");

//-----------------------------------------------------------------------------------------------------------------------//
//Métodos matemáticos
console.log(Math.max(30, 20)); //30
console.log(Math.min(30, 20)); //20
console.log(Math.sqrt(9)); // 3
console.log(Math.max(1,3,5,4,2,7,6)); // 7
console.log(Math.PI); // 3.14159...
console.log(Math.floor(Math.PI)); // 3
console.log(Math.ceil(Math.PI)); // 4

//Math tem diversos métodos, tais como sqrt (calcula a raiz quadrada), 
//floor (devolve o valor inteiro arredondando para baixo), 
//ceil (devolva o valor inteiro arrendondando para cima), entre outros.

//-----------------------------------------------------------------------------------------------------------------------//

//Métodos para lidar com tempo