package pdm// **Declaração de variáveis**
/*
val a: Int = 1    // Atribuição imediata
val e: Short      // Tipo definido sem inicialização
// Explicação: A variável `a` é imediatamente atribuída com o valor 1, enquanto `e` apenas tem seu tipo definido.

var b = 2         // O tipo 'Int' é inferido
b = a             // Reatribuição de 'var' é permitida
// Explicação: A variável `b` tem seu tipo inferido como `Int`. Como é uma variável `var`, ela pode ser reatribuída posteriormente.

val c: Int        // Tipo requerido quando não há inicializador
c = 3             // Atribuição adiada
// Explicação: Quando uma variável `val` é declarada sem inicialização, é necessário definir seu tipo explicitamente. A atribuição pode ser feita posteriormente.

const val NAME = "Kotlin"     // Pode ser calculado em tempo de compilação
val nameLowered = NAME.lowercase()  // Não pode ser calculado em tempo de compilação
// Explicação: Constantes definidas com `const val` podem ser calculadas em tempo de compilação, enquanto valores imutáveis com `val` não.


// **Funções**

fun sum(a: Int, b: Int): Int {
    return a + b
}

fun mul(a: Int, b: Int) = a * b

fun printMul(a: Int, b: Int): Unit {
    println(mul(a, b))
}

fun printMul1(a: Int = 1, b: Int) {
    println(mul(a, b))
}

fun printMul2(a: Int, b: Int = 1) = println(mul(a, b))
// Explicação: A função `sum` retorna a soma de dois números. A função `mul` retorna o produto dos dois números.
// A função `printMul` imprime o resultado da multiplicação. As funções `printMul1` e `printMul2` têm valores padrões para os parâmetros.

fun maxOf(a: Int, b: Int): Int {
    return if (a > b) a else b
}

fun maxOf(a: Int, b: Int) = if (a > b) a else b
// Explicação: A função `maxOf` retorna o maior número entre os dois parâmetros `a` e `b`. A versão de uma linha utiliza expressão condicional `if`.


// **Condicionais (if, when)**

when (x) {
    1 -> print("x == 1")
    2 -> print("x == 2")
    else -> {
        print("x is neither 1 nor 2")
    }
}
// Explicação: O bloco `when` é uma forma alternativa ao `if-else`. Ele verifica o valor de `x` e executa o código correspondente.

when {
    x < 0 -> print("x < 0")
    x > 0 -> print("x > 0")
    else -> print("x == 0")
}
// Explicação: O `when` pode ser utilizado como uma expressão booleana, onde cada condição é verificada até encontrar a verdadeira.


// **Loops (for, while, do-while)**

val items = listOf("apple", "banana", "kiwifruit")

for (item in items) {
    println(item)
}
// Explicação: O loop `for` percorre todos os itens da lista e imprime cada um deles.

for (index in items.indices) {
    println("item at $index is ${items[index]}")
}
// Explicação: O loop `for` usa o índice para acessar cada item na lista `items`.

for ((index, item) in items.withIndex()) {
    println("item at $index is $item")
}
// Explicação: O loop `for` também pode ser utilizado com a função `withIndex()`, que retorna um par `(índice, item)`.

var index = 0
while (index < items.size) {
    println("item at $index is ${items[index]}")
    index++
}
// Explicação: O loop `while` continua enquanto a condição for verdadeira (neste caso, enquanto `index` for menor que o tamanho da lista).

var toComplete: Boolean
do {
    // Algum código
    toComplete = true
} while (toComplete)
// Explicação: O loop `do-while` executa o código pelo menos uma vez antes de verificar a condição no final.


// **Quebra e continuação em loops**

myLabel@ for (item in items) {
    for (anotherItem in otherItems) {
        if (...) break@myLabel
        else continue@myLabel
    }
}
// Explicação: O uso de labels (`@`) permite que você quebre ou continue loops internos a partir de um loop externo.


// **Ranges**

val x = 10
if (x in 1..10) {
    println("fits in range")
}
// Explicação: O operador `in` verifica se o valor de `x` está dentro do intervalo especificado (de 1 a 10, inclusivo).

for (x in 1..5) {
    print(x)
}
// Explicação: O loop percorre o intervalo de 1 até 5.

for (x in 9 downTo 0 step 3) {
    print(x)
}
// Explicação: O loop `downTo` percorre o intervalo de 9 a 0, com um passo de 3.


// **Segurança contra nulidade (Null Safety)**

val notNullText: String = "Definitely not null"
val nullableText1: String? = "Might be null"
val nullableText2: String? = null
// Explicação: O `String?` indica que a variável pode ser nula. O `String` normal não permite valores nulos.

fun funny(text: String?) {
    if (text != null)
        println(text)
    else
        println("Nothing to print :(")
}
// Explicação: A função `funny` verifica se `text` não é nulo antes de imprimir o valor. Caso contrário, imprime uma mensagem de erro.

fun funnier(text: String?) {
    val toPrint = text ?: "Nothing to print :("
    println(toPrint)
}
// Explicação: O operador Elvis `?:` retorna o valor de `text` se não for nulo, caso contrário retorna o valor à direita do operador.

fun loadInfoById(id: String): String? {
    val item = findItem(id) ?: return null
    return item.loadInfo() ?: throw Exception("...")
}
// Explicação: A função `loadInfoById` usa o operador Elvis para retornar `null` caso o item não seja encontrado. Caso contrário, tenta carregar as informações do item.


// **Funções Lambda**

val sum: (Int, Int) -> Int = { x: Int, y: Int -> x + y }
val mul = { x: Int, y: Int -> x * y }
// Explicação: As funções `sum` e `mul` são definidas como expressões lambda. Elas recebem dois parâmetros e retornam um resultado.

val goodProduct = items.fold(1) { acc, e -> acc * e }
// Explicação: A função `fold` percorre a lista `items`, acumulando o resultado da multiplicação de todos os elementos.

run { println("Very Cool") }
// Explicação: A função `run` executa a lambda sem necessidade de parênteses, quando a lambda é o único argumento.


// **Strings e StringBuilder**

val i = 10
val s = "Kotlin"

println("i = $i")
println("Length of $s is ${s.length}")
// Explicação: A string `i = $i` e `Length of $s is ${s.length}` demonstram a interpolação de variáveis dentro de uma string.

val sb = StringBuilder()
sb.append("Hello")
sb.append(", world!")
println(sb.toString())
// Explicação: A classe `StringBuilder` é usada para construir strings dinamicamente. Ela é mais eficiente em loops e manipulações contínuas de strings.
*/