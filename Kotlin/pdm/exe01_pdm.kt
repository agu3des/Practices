package pdm

//Escreva uma função que receba um número e verifique se ele é positivo, negativo ou zero. Use o IF como expressão.
fun numberId(num: Int) {
    if (num < 0) {
        println("Você digitou: ${num}, que é um número negativo!")
    } else {
        println("Você digitou: ${num}, que é um número positivo!")
    }
}

//Implemente uma função que receba a idade de uma pessoa e use o when para verificar e retornar à faixa etária de uma pessoa (criança, adolescente, adulto, idoso).
fun faixaEtaria (idade: Int) {
    when {
        idade < 13 -> println("Idade: $idade | Faixa Etária: Criança")
        idade in 13..17 -> println("Idade: $idade | Faixa Etária: Adolescente")
        idade in 18 .. 59 -> println("Idade: $idade | Faixa Etária: Adulto")
        idade >= 60  -> println("Idade: $idade | Faixa Etária: Idoso")
    }
}

//Crie uma função que receba um valor e uma lista de valores (de tamanho indefinido e com valores de diferentes tipos de dados). A função deverá retornar quantas ocorrências do valor aparecem na lista.
/*fun listaValores(mutableListOf<Int>()) {

}
*/
//Escreva uma função que receba uma matriz e retorne qual o seu maior valor.

//Escreva uma função que receba um valor e uma matriz. O programa deverá imprimir e quais posições estão o valor parametrizado. Em seguida, faça um programa que gere uma matriz, identifique qual o seu maior e onde estão na matriz. Reuse a função da questão 4.

//Crie uma lista mutável contendo vários nomes. A entrada de dados se encerrará quando o usuário digitar a palavra ‘fim’. Em seguida, crie uma expressão lambda e use-a no método forEach da lista, para filtrar e imprimir todos os nomes que comecem com a letra ‘B’.

//Crie uma função que receba, via parâmetro, um nome (que pode ser nulo) e imprima uma saudação personalizada, apenas se o nome não for nulo.



fun main() {
    numberId(-4)
    numberId(8)

    faixaEtaria(15)
    faixaEtaria(18)
    faixaEtaria(12)
    faixaEtaria(34)
    faixaEtaria(61)


}