//Nota 90/100

let idade = 20;
const nome;
nome = "Maria";
console.log(`Meu nome é ${nome} e tenho ${idade} anos`); //SyntaxError: Missing initializer in const declaration


let x = 10;
let y = 20;
console.log(x < y);//true

/*
var signo = prompt("Qual é o seu signo?");
if (signo.toLowerCase() == "escorpião") {
    alert("Legal! Eu sou de escorpião também!");
}
else {
    alert("Hoje seu dia será maravilhoso");
}
*/

let serie = 4;
if (serie === 3) {
    console.log("Boa sorte!");
} else if (serie === 2) {
    console.log("Quase lá!");
} else if (serie === 1) {
    console.log("Ainda não pode fazer ENEM");
} else {
    console.log("Série desconhecida");
}

for (let i=1; i<=100; i++) {
    console.log(i);
}

for (let i=0; i<0; i++) {
    console.log(i);
}

let num = 5
while (num < 50) {
    num++;
    console.log(num);
}
