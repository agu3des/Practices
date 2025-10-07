# POO

[Projeto POO - 1](POO%205e3418170ccd40f8a27d5f8abd0b2f50/Projeto%20POO%20-%201%204added353523416fbac305f8714aebbd.md)

[Projeto POO - 2](POO%205e3418170ccd40f8a27d5f8abd0b2f50/Projeto%20POO%20-%202%202c0fa909425e4e5b9cacafe0e8436ac2.md)

[Git into Eclipse](https://medium.com/@AlexanderObregon/getting-started-with-version-control-in-eclipse-ide-git-and-github-integration-a0cca7b15126)

[Atalhos - Eclipse/IntelliJ](https://gist.github.com/boaglio/5c70707ea5061940496e345a788c9b63)

### Introdução a Java - POO

Bibliotecas de desktop (se), se for para outras aplicações tem que baixar outros tipo o androidStudio

Maior mudança em termos de sintaxe em Java doi no 8

Se for string continua, se for número ele transforma em string

Letra maiúcula classe

Tipo primitivo minúsculo

Tipo primitivo e classe encapsuladora a partir de uma vrsão do java já se mesclam

```java
int a = 0; //valor
Integer b = 4; //objeto
a = b + 1; //5
b = a + 2; //7
```

Valores são comparados através dos operadores: == , != , = , < , <=

Objetos: equals(), compareTo()

and: &&  , or: ||  ,  not: !

São dois para otimização, pois se a primeira for falsa já n faz a segunda

```java
import java.util.Scanner; //util - pacote, scanner classe

public class Amigo {

	public static void main(String[] args) {

		Scanner teclado = new Scanner(System.in); //instancia o objeto
		System.out.println("Qual é o seu nome?");
		String nome1 = teclado.nextLine(); //pega o que tá escrito
		System.out.println(nome1+", de quem vc é amigo?");
		String nome2 = teclado.nextLine();
		System.out.println(nome1 +" é amigo de "+ nome2);
		teclado.close(); //finaliza

	}

}

```

![Untitled](POO%205e3418170ccd40f8a27d5f8abd0b2f50/Untitled.png)

Para utilizar o input usamos o scanner

Condições é obrigatório estar entre parênteses

Chaves só são necessárias se haver blocos de comandos

Declara fora, pois se declarar dentro ele vai criar uma variável nova a cada vez que rodar

Array é fixo, split em string gera array então geralmente é onde ele é usaddo

### Loop

![Untitled](POO%205e3418170ccd40f8a27d5f8abd0b2f50/Untitled%201.png)

for-each para cada elemento n dentro de um array número mostre n

Não guarda duas vezes na memória, ele só faz a referência, porém se criar usando construtor força a criar outro objeto

![Untitled](POO%205e3418170ccd40f8a27d5f8abd0b2f50/Untitled%202.png)

Ao contrário de ed que construia classes voltadas para a programação, em poo faremos classes voltadas para o problema

Progrmação orientada a função / lógica / objeto

Abstração: facilitar, quanto mais simples melhor

Encapsulo crio um nível de abstração maior

Ex: criei uma árvore, ralei que só + complicado pra mim, pra quem usar minha árvore será bem mais tranquila

Abstração X Paradigma

![Untitled](POO%205e3418170ccd40f8a27d5f8abd0b2f50/Untitled%203.png)

**Orientada a procedimento:** a Fortran, Basic, Pascal, C, Cobol, Cliper …, o processo é uma ‘tarefa’ | Confiança baixo-nível

Orientada a objeto: Smaltalk, C++, Eiffel, Lua, Delphi, VB, Python, Java, C#, PHP, JavaScript, ... | Classe é uma abstração de dados

Continua a abstração de processo, no entanto agora com a abstração de dados

Classe: conjunto de coisas (objeto) que possuem mesmos atributos e métodos

Objeto: instância de uma classe

Etapas de desenvolvimento OO

![Untitled](POO%205e3418170ccd40f8a27d5f8abd0b2f50/Untitled%204.png)

Modelagem de classes:

![Untitled](POO%205e3418170ccd40f8a27d5f8abd0b2f50/Untitled%205.png)

O professor modela, nós implementamos e instânciamos

Métodos: funções internas, só através dos métodos se altera os atributos do objeto

Atributos: variáveis internas

this -. objeto sendo construido

Todos as classes herdam da classe object

### **Construtores**

![Untitled](POO%205e3418170ccd40f8a27d5f8abd0b2f50/Untitled%206.png)

```java
public class Retangulo{ 
	public int id; //identificar qual o objeto
	public double largura; //atributo
	public double comprimento;
	
	public double calcularArea(){ //método
		return largura * comprimento;
	}
	
	public double calcularPerimetro()
}
```

Variável de referência: segura o objeto através da referência a menória onde ele está alocado

Variáveis globais (estão acessíveis em todo o programa) e variáveis locais (existem enquanto o bloco estiver em execução)

Se eu passo 3 parâmetros, ao chamá-los é na ordem e só pode ter 3

```java
public class Retangulo {
	public int id; // identificar qual o objeto
	public double largura; // atributo
	public double comprimento; //outra classe pode acessar esses dados
						//ao finalizar o uso os parâmetros que estão aqui somem
	public Retangulo(int id, double largura, double comprimento) { //meu construtor
		this.id = id;
		this.largura = largura;
		this.comprimento = comprimento; //pode ter vários construtores todos com o mesmo nome da casse
	}

	public Retangulo() {  //construtor vazio, só cria o objeto
	}
}
```

### Métodos

Chamada de método Individual

```java
String nome; 
nome = teclado.nextLine(); //individual
nome = nome.toUpperCase();

nome = teclado.nextLine().toUpperCase(); //encadeada, 2 objetos criados
//o primeiro é destruído após a execução do segundo

double x = new Retangulo(1,3,4).calcularArea();
```

![Untitled](POO%205e3418170ccd40f8a27d5f8abd0b2f50/Untitled%207.png)

Um método pode ter n parâmetros e no fim um return (para um método void isso não é necesário)

Void só altera infos

```java
public Retangulo(int id, double largura, double comprimento) { //meu construtor
		this.id = id;
		this.largura = largura;
		this.comprimento = comprimento; //pode ter vários construtores todos com o mesmo nome da casse
	}
```

![Untitled](POO%205e3418170ccd40f8a27d5f8abd0b2f50/Untitled%208.png)

Usado para distinguir um atributo do objeto de uma outra variável de mesmo nome

Indicar o que é do objeto e o que não é, não é obrigatória, apenas quando pode-se haver confusão

```java
	public boolean ehEquivalente(Retangulo outro) {
		return (this.calcularArea() == outro.calcularArea());
	} //tem que colocar os dois pq se não ele entende como o mesmo
```

### Sobrecarga

Sobrecarga: o mesmo fica com das tarefas no mesmo nome

Sobrecarga de construtores:

![Untitled](POO%205e3418170ccd40f8a27d5f8abd0b2f50/Untitled%209.png)

```java
	public int id; // identificar qual o objeto
	public double largura; // atributo
	public double comprimento; //outra classe pode acessar esses dados
				//ao finalizar o uso os parâmetros que estão aqui somem
	public Retangulo(int id, double largura, double comprimento) { //meu construtor
		this.id = id;
		this.largura = largura;
		this.comprimento = comprimento; //pode ter vários construtores todos com o mesmo nome da casse
	}

	public Retangulo() {  //construtor vazio, só cria o objeto
		// id = 1;    valor que eu posso definir como default caso não receba nenhuma atribuição
		// largura = 1;
		// comprimento = 1;
	}

	public Retangulo(double lado) { //construtor com apenas um argumento
		this.largura = lado;
		this.comprimento = lado; 
	}
```

### Encapsulamento

Modificadores de acesso

![Untitled](POO%205e3418170ccd40f8a27d5f8abd0b2f50/Untitled%2010.png)

Public não é uma boa prática, impede o acesso direto visando aumentar a abstração

Private impede o acesso do atributo fora de sua classe

Botar “bloqueios”

```java
public class Conta {
    private String numero; //private = apenas a classe pode acessar
    private String cpf;
    private double saldo;

    public Conta(String numero, String cpf) {
        this.numero = numero; //this = é o dessa classe
        this.cpf = cpf;
        this.saldo = 0; 
    }
    public double getSaldo() { //get = eu peço isso
    	return saldo;
    }
    public void setNumero(String numero) { //set = diga/transforme nisso
		this.numero = numero;
		}
```

Set → alterar atributos do objeto

Get → pegar o atributo

Ambos servem para proteger seus atributos

Ao serem inseridos no código, agora devem ser utilizados ao invés dos métodos “normais”

Se eu colocar os 2 pontos significa que eu vou ter uma lista de parâmetros variáveis

```java
public void creditar(double... lista) {
	for(double valor : lista)
		saldo = saldo + valor;
}
```

### Modelagem Orientada a Objetos

1. Instanciação: o objeto é criado na memória e
passa a ser referenciado por uma variável de
referência;
2. Uso: manipulamos o objeto através de seus
métodos
3. Destruição: quando o objeto não é mais
referenciado (acessível) ele torna-se elegível
para a coleta de lixo

![Untitled](POO%205e3418170ccd40f8a27d5f8abd0b2f50/Untitled%2011.png)

![Untitled](POO%205e3418170ccd40f8a27d5f8abd0b2f50/Untitled%2012.png)

```java
Retangulo r1 = null;
for(int i=1; i<=10; i++){
r1 = new Retangulo(i,i,i); //cria dez objetos
System.out.println(r1.calcularArea());
}
System.out.println(r1.getId()); // 10

Retangulo r1,r2,r3;
r1 = new Retangulo(1,5,30);
r2=r1;
r3=r1;
r3.setLargura(7);
r2.setLargura(8);
...println(r1.calcularArea()); //240
...println(r2.calcularArea()); //240
...println(r3.calcularArea()); //240

Retangulo r1,r2,r3;
r1 = new Retangulo(1, 5,30);
r2 = new Retangulo(2, 10,10);
r3=r2;
r2=r1;
r1=null;
```

Static: Todos podem ver

Método estático só pode chamar outro estático 

Bloco estático: uma palavrea estática solta no meio da classe, quando der run ele vai ser executado imediatamente

### Polimorfismo e Herança

abstract impossibilita a instanciação não a utilização

método abstrato a classe obrigatoriamente tem que ser abastrata

são polimóficas e por serem subtipos delas pode essa atribuição. Sempre vai do tipo do objeto,

Pai p = new Filho();

P.quemsoueu();

“sou filho”

super sobre para a classe pai

b escreva () -> b super.escreva() -> a escreva() -> b escreva(3) -> b superescreva(3+1) -> a escreva(4+2)

### Casting

Forçar uma variável a receber outro tipo, variáveis polimórficas são para isso

```java
Animal a1 = new Cachorro("rex", 5);
Cachorro c1 = a1; //dá erro, pois cachorro não pode receber animal
Cachorro c1 = (Cachorro) a1; //dá certo, pois o compilador só consegue analisar o tipo da variável
Animal a2 = new Cachorro("lis",6);
Gato g2 = (Gato) a2; //dá erro
```

```java
		//casting implicito
		ArrayList<Gato> gatos = new ArrayList<>();
		for (Animal a : animais){
			if(a instanceof Gato g) //casting implicito*
				gatos.add(g);
		}
		System.out.println( "Lista de Gatos: " + gatos ); // [fifi,nino]
	
	//
		ArrayList<Gato> saltadores = new ArrayList<>();
		for (Animal a : animais){
			if(a instanceof Gato g && g.getSalto()>= 5)
				saltadores.add(g);
		}
		System.out.println( saltadores ); // [fifi]
```

```java
		//explicito
		ArrayList<Gato> saltadores = new ArrayList<>();
		for (Animal a : animais){
			if(a instanceof Gato && ((Gato)a).getSalto()>= 5) //o ponto tem mais prioridade que o parenteses então tem que adicionar mais um parenteses
				saltadores.add((Gato)(a));
		}
		System.out.println( saltadores ); // [fifi]
```

### Relacionamento entre objetos

Um aponta para o outro

```java
maria = new Pessoa("maria","...");
joao = new Pessoa("joao","...");
maria.setConjugue(joao);
joao.setConjugue(maria);
```

![image.png](POO%205e3418170ccd40f8a27d5f8abd0b2f50/image.png)

**Quanto a direção:** Unidirecional, Bidirecional

**Quanto à Cardinalidade:** 

um para um (1:1)

```java
		Motor motor = new Motor("Zetec", 1.0);
		Motorista motorista = new Motorista("1111");
		Carro carro = new Carro("AAA1234", motor, motorista);
		
		//carro puxa motor e motorista
				Carro carro2 = new Carro("BBB5678", 
							new Motor("Zetec", 1.5),
							new Motorista("2222"));
```

![image.png](POO%205e3418170ccd40f8a27d5f8abd0b2f50/image%201.png)

**Navegação:**

```java
System.out.println("Cnh antes: "+carro3.getMotorista().getCnh());//1111
carro3.getMotorista().setCnh("3333");
System.out.println("Cnh depois: "+carro3.getMotorista().getCnh());//3333
```

um para muitos (1:*)

```java
package aulaJava.Prateleira;

import java.util.ArrayList;

public class Prateleira {
	private int id;
	private int tamanho;
	private ArrayList<Produto> produtos = new ArrayList<>();
	
	public Prateleira(int id, int tamanho) {
		this.id = id;
		this.tamanho = tamanho;
	}
	
	public void adicionar(Produto p) {
		produtos.add(p);
		p.setPrateleira(this);
	}
	
	public void remover(Produto p) {
		produtos.remove(p);
		p.setPrateleira(null);
	}
	
	public Produto localizar(String nome) {
		for(Produto p: produtos) {
			if(p.getNome().equals(nome))
				return p;
	
		}return null;
	}
	
	public int getId() {
		return id;
	}

	public int getTamanho() {
		return tamanho;
	}
	public ArrayList<Produto> getProdutos() {
		return produtos;
	}
	
	
	
	public void setTamanho(int tamanho) {
		this.tamanho = tamanho;
	}

	public void setProdutos(ArrayList<Produto> produtos) {
		this.produtos = produtos;
	}
	
	public void setId(int id) {
		this.id = id;
	}

	
	
	@Override
	public String toString() {
		return "Prateleira [id=" + id + ", tamanho=" + tamanho + ", produtos=" + produtos +"]";
	}
}
```

```jsx
package aulaJava.Prateleira;

public class Produto {
	private String nome;
	private double preco;
	private Prateleira prateleira;
	
	public Produto(String nome, double preco) {
		this.nome = nome;
		this.preco = preco;
	}
	
	public void setPrateleira(Prateleira p) {
		prateleira = p;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}
	
	public void setPreco(double preco) {
		this.preco = preco;
	}
	
	
	
	public String getNome() {
		return nome;
	}
	
	public Prateleira getPrateleira() {
		return prateleira;
	}
	
	public double getPreco() {
		return preco;
	}
	
	
	
	@Override
	public String toString() {
		return "Produto: nome=" + nome + ", preco=" + preco + ", prateleira=" + prateleira.getId() + ";";
	}

}

```

```jsx
package aulaJava.Prateleira;

public class PrateleiraTeste {

	public static void main(String[] args) {
		Produto arroz,feijao,carne,leite;
		
		arroz = new Produto("arroz", 5.0) ;
		feijao = new Produto("feijao", 8.0) ;
		carne = new Produto("carne", 40.0) ;
		leite = new Produto("leite", 5.0) ;
		
		Prateleira prat1 = new Prateleira(1, 10);
		Prateleira prat2 = new Prateleira(2, 20) ;
		
		prat1.adicionar(arroz);
		prat1.adicionar(feijao);
		prat1.adicionar(carne);
		prat2.adicionar(leite);
		
		//arroz.setPrateleira(prat1);
		//feijao.setPrateleira(prat1);
		//carne.setPrateleira(prat1);
		//leite.setPrateleira(prat2);
		
		System.out.println(prat1);
		System.out.println(prat2);
		System.out.println(arroz);
		System.out.println(feijao);
		System.out.println(carne);
		System.out.println(leite);
		
		//localizar leite na prateleira 2
		Produto p = prat2.localizar("leite");
		if(p == null)
		System.out.println("Não localizou");
		else
		System.out.println("Localizou: " + p);
		
		//transferir arroz da prateleira 1 para 2
		prat1.remover(arroz);
		prat2.adicionar(arroz);
		arroz.setPrateleira(prat2);
		System.out.println("transferiu arroz");
		
		//exibir os objetos relacionados (final)
		System.out.println(prat1);
		System.out.println(prat2);
		System.out.println(arroz);
		System.out.println(feijao);
		System.out.println(carne);
		System.out.println(leite);

	}

}

```

Se a prateleira tem produto, produto está na prateleira, os dois tem que estar existentes.

Os objetos podem existir, mas o relacionamento não

O desligamento e o ligamento é bidirecional

muitos para muitos *(** : *)

```java
package aulaJava.Livro;

import java.util.ArrayList;

public class Livro {
	private String titulo;
	private ArrayList<Autor> autores;
	private ArrayList<String> categorias = new ArrayList<>();
	
	
	public Livro(String titulo, String categ) {
		this.titulo = titulo;
		this.autores = new ArrayList<>();
		categorias.add(categ);
	}
	
	public void adicionar(Autor aut) {
		if (!autores.contains(aut)) {
			autores.add(aut); //adiciona no array aut
			aut.adicionar(this); //em aut ele chama o metodo adicionar	
		}
	}
	
	public void remover(Autor aut) {
		 if (autores.contains(aut)) {
			 autores.remove(aut);
			 aut.remover(this);
		 }
	}
		
	public Autor localizar(String nome) {
		for(Autor aut: autores)
			if(aut.getNome().equals(nome))
				return aut;
		return null;
	}
		
	public String getTitulo() {
		return titulo;
	}
	
	public ArrayList<String> getCategorias() {
		return categorias;
	}

	public void setCategorias(ArrayList<String> categorias) {
		this.categorias = categorias;
	}

	public void setTitulo(String titulo) {
		this.titulo = titulo;
	}
	
	public ArrayList<Autor> getAutores() {
		return autores;
	}
	
	public void setAutores(ArrayList<Autor> autores) {
		this.autores = autores;
	}
	
	@Override
	public String toString() {
		return "Livro [titulo=" + titulo + ", autores=" + autores + "]";
	}
	
	
}
```

```java
package aulaJava.Livro;

import java.util.ArrayList;

public class Autor {
	private String nome;
	private ArrayList<Livro> livros;
	
	public Autor(String nome) {
		this.nome = nome;
		this.livros  = new ArrayList<>();
	}
	
	
	public void adicionar(Livro liv) {
		if (!livros.contains(liv)) {
			livros.add(liv);
		}
	}
	public void remover(Livro liv) {
		if (livros.contains(liv)) {
			livros.remove(liv);
		}
	}
		
	public Livro localizar(String titulo) {
		for(Livro liv: livros)
			if(liv.getTitulo().equals(titulo))
				return liv;
		return null;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public ArrayList<Livro> getLivros() {
		return livros;
	}

	public void setLivros(ArrayList<Livro> livros) {
		this.livros = livros;
	}

	@Override
	public String toString() {
		return "Autor [nome=" + nome + ", livros=" + livros + "]";
	}
	
	
}

```

```java
package aulaJava.Livro;

public class LivroTeste {

    public static void main(String[] args) {
        // Criação dos livros e autores
        Livro java = new Livro("java", "ciencia moderna");
        Livro php = new Livro("php", "pratica");
        Autor joao = new Autor("joao");
        Autor maria = new Autor("maria");

        // Adiciona autores aos livros
        java.adicionar(joao);
        java.adicionar(maria);
        php.adicionar(maria);

        // Adiciona livros aos autores
        joao.adicionar(java);
        maria.adicionar(java);
        maria.adicionar(php);

        // Transferir autor “joao” de um livro para outro
        // Aqui, assumimos que 'localizar' está correto para 'Autor'
        Autor a = java.localizar("joao");
        if (a != null) {
            // Remove joao de java e adiciona em php
            java.remover(a);
            php.adicionar(a);

            // Remove java de joao e adiciona php
            a.remover(java);
            a.adicionar(php);
        }

        // Exibe o estado final dos livros e autores
        System.out.println(java);
        System.out.println(php);
        System.out.println(joao);
        System.out.println(maria);
    }
}

```