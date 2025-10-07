# Extras

Curso: https://github.com/loiane/curso-java-basico

[Unimed](Extras%20e66c2710203346d285a5682abd9cb45a/Unimed%201912e5a697c380ceb80be0209c5392e1.md)

java —> class —> programa 

JVM = java virtual machine, precisamos compilar para a linguagem java

Por isso ao escrever apenas um código posso rodá-lo em qualquer plataforma = wora (write once run anywhere)

API interface e programação de java, é um conjunto de bibliotecas

API + JVM = plataforma java

### Repositório:

![Untitled](Extras%20e66c2710203346d285a5682abd9cb45a/Untitled.png)

O nome da classe começa com letra maiúscula e segue camel case, nome da classe = nome do arquivo

Case sensitive

É criado um arquivo .class

![Untitled](Extras%20e66c2710203346d285a5682abd9cb45a/Untitled%201.png)

```java
class HelloWorld {
	public static void main (String[] args){
		System.out.println("Hello World");
	}
}
```

class = declaração

HelloWorld = nome da classe

public static void main = dentro da primeira chave/método

public static = modificadores de acesso, esse não muda

void = tipo de retorno, logo, nada

main = nome do método

(String[] args) = parâmetros/argumentos do método

System.out.println("Hello World"); = código

```java
package aulas;
class Argumentos {
	public static void main (String[] args){
		System.out.println("Você digitou " + args[0]);
	}
}
```

Executado pela linha de comando

Como esse args é um array de strings, podemos acessar qualquer posição dessa string

Linguagem compilada e interpretada

![Untitled](Extras%20e66c2710203346d285a5682abd9cb45a/Untitled%202.png)

![Untitled](Extras%20e66c2710203346d285a5682abd9cb45a/Untitled%203.png)

### **Erros:**

Sintaxe - arquivo errado

Semântica - declaração de variáveis 

Tempo de Execução - métodos errados ou códigos “errados”

```java
package Aulas;
class Error {
	public static void main (String[] args){
		System.out.println("Hello World)
	}
}

// retire a aspa e o ponto e vírgula = erro de sintaxe

```

```java
package Aulas;
class HelloWorld {
	public static void main (String[] args){
		System.out.println("Hello World");
	}
}

//se o nome da class (HelloWorld) estiver diferente do arquivo (Error)= erro de execução
//pois ao gerar o class, este vai ser com o nome da função
```

```java
package Aulas;
class Error {
	public static void Main (String[] args){
		var int cont;
		System.out.println("Você digitou: " + cont);
	}
}

// Main = é uma método de uma classe, mas não é o ponto de entrada de java, quebra na execução
// var = erro de semântica, o java não reconhece o var
//  + cont = erro de semântica, pois a variável não foi acessada
```

```java
package Aulas;
class Error {
	public static void Main (String[] args){
		System.out.println("Você digitou: " + 1/0); //= erro de execução
	}
}
```

Paradigmas Esstruturado X Orientado a objeto

Java foi feita para ser orientada, ela já é  em si

Vantagens de OO:

Reuso do código, reflete o mundo real, facilita a manutenção no código

Classes: descrição de um grupo de objetos, nome, conjunto de atributos (descrição), conjunto de métodos (comportamento)

Objetos (), herança, polimorfismo

Objeto é a instanciação da classe, quando vc dá vida a ela

**Classe** → planta da casa

**Objeto** → casa da Maria

**Método** → comportamento/ações e uma classe

**Herança** → permite que você use uma estrutura

**Polimorfismo** → ter mais de um tipo

Pastas também é sobre armazenar bibiotecas

### Variável

área de memória associada a um nome que pode armazenar valores de um determinado tipo

<tipo> <nome da variavel>; ou <tipo> <nome da variavel> = <valor>;

![Untitled](Extras%20e66c2710203346d285a5682abd9cb45a/Untitled%204.png)

Convenção nomeclatura

a-z A-Z_& 0-9 esse & não é legal

case sensitive: apesar de poder começar com qualquer letra, geraalmente se começa com minúscula = nomeDaPessoa

Tipos: int, float, char, bool

![Untitled](Extras%20e66c2710203346d285a5682abd9cb45a/Untitled%205.png)

Inteiros:

Byte - 1

Short - 2 bytes

Int - 4 bytes

Long - 8 bytes

Padrão é int e long

![Untitled](Extras%20e66c2710203346d285a5682abd9cb45a/Untitled%206.png)

Pontos Flutuantes

Float - 32 -  ex.100.30f

Double - 64 - ex.100.30

A diferença é o tamanho e o espaço de memória, padrão é o double

Char

Uma string basicamente, pode ser um número se utilizarmos a tabela ASCII

```java
char o = 111;
char i = 105;
char interrogacao = 0x00E1;
System.out.println(””+o+i+interrogacao); 
//bota as aspas para ele não somar os valores
```

Unicode para ser acessível a diversas linguagens

Boolean

True or false

```java
System.out.println("Boolean");
boolean verdade = true;
boolean falsidade = false;
System.out.println("O valor de verdade é = "+verdade +"\n" +"O valor de falso é = "+falsidade);
```

```java
System.out.println("Curiosidade");
        int var1 = 214783647;
        int var2 = 1;
        System.out.println(var1+var2);
        //não dá erro
        //No momento que eu somo e vai para o limite ele fica negativo
        //-214783648
```

Literais

Deixar explícito que o valor que vc tá usando é long bota o l, como no float vc coloca o f

```java
package CursoJava;

import java.util.Scanner;

public class DadosTeclado {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        /*String nome = scan.next(); //ler oq foi colocado e virar str
        int idade = scan.nextInt(); //inteiro
        double altura = scan.nextDouble(); //double*/
        
		/*
		 * System.out.println("Digite seu nome completo: "); 
		 * String nomeCompleto = scan.nextLine(); 
		 * System.out.println("Seu nome completo é: "+nomeCompleto);
		 * 
		 * System.out.println("Digite seu primeiro nome: "); 
		 * String primeiroNome = scan.next(); 
		 * System.out.println("Seu primeiro nome é: "+primeiroNome);
		 * 
		 * System.out.println("Digite sua idade: "); 
		 * int idade = scan.nextInt();
		 * System.out.println("Sua idade é: "+idade);
		 * 
		 * System.out.println("Digite sua altura: "); 
		 * double altura = scan.nextDouble();
		 * System.out.println("Sua altura é: "+altura);
		 */
        
        System.out.println("Digite seu primeiro nome, idade, altura, quantos filhos e se tem pet: ");
        
        String primeiroNome = scan.next();
        int idade = scan.nextInt();
        float altura = scan.nextFloat();
        byte qtdFilhos = scan.nextByte();
        boolean temPet = scan.nextBoolean();
        
        System.out.println("Você digitou os seguintes valores:");
        System.out.println("Primeiro Nome: "+primeiroNome);
        System.out.println("Idade: "+idade);
        System.out.println("Altura: "+altura);
        System.out.println("Quantidade de Filhos: "+qtdFilhos);
        System.out.println("Tem pet: "+temPet);
    }
}

```

### Operadores

![Untitled](Extras%20e66c2710203346d285a5682abd9cb45a/Untitled%207.png)

### Herança

Eu tinha várias classes e agora eu crio uma geral e instancio ela nas outras, com eu criando apenas o necessário que é específico daquela classe

Animal é pai de cachorro, gato e pássaro, pois essas classes vão herdar o que a classe animal tm

**Não posso usar o private** se estou trabalhando com herança, logo tenho que alterar o modificadores de acesso

@Override: serve para pegar um método que é do pai daquela classe e altera o resultado dele

```java
@Override
public void soar() {
	System.out.println("Piu Piu");
}
```

Se eu tenho isso, não posso apagar apenas do pai, pois as classes filhas irão reclamar, tem que apagar de tudo 

Creating constructor that matchs super = crie uma construtor que combine com o pai

### Polimorfismo

```java
public void darBanho(Animal animal) {
	animal.setEstadoDeEspírito("Limpo");
}//aceita todos os animais

public void darBanho(Cachorro cachorro) {
	animal.setEstadoDeEspírito("Tosado");
}//só aceita cachorro
//Mesmo que ambos sejam animais o método 
//instanciado só aceita cachorro, se for 
//passado outro animal ele irá relatar erro
```

O polimorfismo é a capacidade de um objeto ser referenciado de várias formas, o objeto não se muda, mas sim a forma como referenciamos ele

1. Eu posso criar um gato dentro de um gato
2. um gato dentro de um animal
3. mas não um animal dentro de gato, pois animal pode ser qualquer coisa e java quando for transformar não vai saber ao certo como criar
4. também não posso criar um gato dentro de um cachorro pois um gato não é um cachorro é um animal

Na realidade não existe um Animal animal, por isso a transformamos em uma classe abstrata, logo ela não pode ter nada concreto, eu não posso definir o que o animal faz

```java
public abstract class Animal
// agora eu não posso criar Animal animal = new Animal()

public abstract void soar(); //não tem corpo
//todo animal tem o método soar, mas cada um vaia ter a sua forma
```

Uma classe abstrata é só a ideia, a planta de algo

### Estrutura de Dados

Dados primitivos

![Untitled](Extras%20e66c2710203346d285a5682abd9cb45a/Untitled%208.png)

![Untitled](Extras%20e66c2710203346d285a5682abd9cb45a/Untitled%209.png)

Dados não primitivos

Lista de supermercado:

Adicionar intens em uma lista

Ponteiro fora, apontando para nada

Inseri o arroz → ponteiro aponta para o índice do arroz

O ponteiro aponta e fica onde ele apontou

Se eu removo o feijão fica um buraco vazio, de forma a como controlar o que está vazio ou não. Utilizar o shift para puxar da direita (ponta) para 

TODA VEZ QUE UMA CLASSE IMPLEMENTA UMA INTERFACE, Esta CLASSE

NÃO SENDO ABSTRATA EU SOU OBRIGADA A IMPLEMENTAR TODOS os MÉTODOS

![Untitled](Extras%20e66c2710203346d285a5682abd9cb45a/Untitled%2010.png)

Estrutura de dados é uma forma específica de armazenar dados

TIpo abstrato de dado é o uso de uma estrutura de dados com comportamento específico

![Untitled](Extras%20e66c2710203346d285a5682abd9cb45a/Untitled%2011.png)

Lista Ligada ou Lista Encadeada é uma estrutura de dados dinâmica,linear, formada por nós. Cada nó é capaz de armazenar uma informação e|referenciar O próximo nó.

Não tem tamanho fixo, poisvai se adicionando ao longo da criação 

![Untitled](Extras%20e66c2710203346d285a5682abd9cb45a/Untitled%2012.png)

![Untitled](Extras%20e66c2710203346d285a5682abd9cb45a/Untitled%2013.png)

O nó de uma lista ligada sempre tem que apontar a algo para se referenciar

tem que percorrer tudo a partir do começo se eu quiser ir para uma posição aletória

![Untitled](Extras%20e66c2710203346d285a5682abd9cb45a/Untitled%2014.png)

![Untitled](Extras%20e66c2710203346d285a5682abd9cb45a/Untitled%2015.png)