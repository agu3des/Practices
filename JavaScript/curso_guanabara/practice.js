let idade = 18
let sexo = "M"

console.log(idade);
console.log(sexo);


idade = 19
let nome = 'Ananda'
let nota = 10
console.log('A aluna '+nome +'com' +idade +'anos, tirou a nota ' +nota);
console.log(`A aluna ${nome} com ${idade} anos, tirou a nota ${nota}`);

let n = 3
let m = 5
n = n+4
n += 5
//para todos os outros operadores aritméticos é válido esse tipo de sintexe

console.log("Operadores relacionais: "+
    "m > n"+m > n,
    "m < n"+m < n,
    "m >= n"+m >= n,
    "m <= n"+m <= n,
    "m == n"+m == n,
    "m != n"+m != n,
    "5 == 5"+5 == 5, //true
    "5 == '5'"+5 == '5', //true
    //Não testa o tipo e sim o mesmo valor/grandeza
    "5 === '5'"+5 === '5' //false 
    //mesmo valor e mesmo tipo
);
//se tiver operadores aritméticos e relacionais, os aritméticos são feitos antes


console.log("Operadores lógicos: "+
    "true && false"+true && false,
    "true && true"+true && true,
    "false || false"+false || false,
    "true && truetrue || false"+true || false,
    "true || true"+true || true
);

console.log("m > n && m % 2 == 0"+m > n && m % 2 == 0 + "m <= n || m!= n"+ m <= n || m!= n);


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