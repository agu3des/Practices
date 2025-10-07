# Algoritmos e Programação Estruturada

AULA 1: Introdução a Python

Assistir: Gustavo Guanabara → Python

→ Linguagem eficiente e produtiva; menor tempo de desenvolvimento, fácil interpretação, curva de aprendizagem reduzida, multiplataforma.

→ Usada para administrar grandes sistemas e desenvolver projetos.

→ Software livre, nenhuma empresa o possui → é formada de colaboradores

**→ Frameworks:** é aquilo que está na base de um sistema, funcionando como um suporte. Ele permite compartilhar um conjunto de códigos entre aplicações e oferece algum tipo de funcionalidade. Assim, essa ferramenta torna o processo de codificação mais rápido

→ Programa no IDE: ambiente de desenvolvimento integrado. No Python é o IDLE.

→ Colab: é web, é da google —> fácil login, fica salvo no drive.

→ Chame um arquivo de notebook, dá pra fazer mais de um programa;

→ Ele usa variáveis anteriores, o que atrapalha. Tem que limpar antes o ambiente de execução.

→ Pycharm/vscode

**→ VARIÁVEL:** espaço reservado na memória para armazenamento de dados;

o nome tem que ter a ver: é um nome, bote nome;

- **Atribuição (=):** atribui algo a variável

**→ Entrada(input):**

```python
a=input()
5
a
'5'

a=int(input())
5
a
5
```

OBS: Quando se usa o input o padrão é string, para mudar tem que colocar.

nome=input('digite um nome')

digite um nome

**→ Saída(print):**

Para mostrar algo, pode ser string, número, conteúdo de variável.

```python
nome=input('digite um nome:')
digite um nome: ananda

nome='joão'
idade=20
print(nome,'tem',idade,'anos')
joão tem 20 anos
```

OBS: sep: você usa para tirar a separação padrão

ex: print(nome,'tem',idade,'anos', sep='*')

```python
joão*tem*20*anos
print(nome,'tem',idade,'anos', sep='')
joãotem20anos
```

(Int): inteiro, não funciona texto

(String): Aspas, é texto

(Float): Números quebrados

OBS: Não se soma texto

1+2

3

'1+2'

‘1' + '2'

'12'

Bool/Boolean:  Se algo é verdadeiro(True) ou falso(False), 0 == false e 1==true

Operações:

Soma(+)

Subtração(-)

Multiplicação(*)

Divisão Real(/)

Divisão inteira(//) pega só antes da vírgula → 2,5 vira 2

Resto de uma divisão (%)

**PRÁTICA EM CASA:**

```python
**nome=input('digite um nome:')
digite um nome: ananda
nome='ananda'
idade=18
print(nome,'tem',idade,'anos')
ananda tem 18 anos
print(nome,'tem',idade,'anos',sep='')
anandatem18anos
x=input('eu sou incrível')
eu sou incrível**
```

→ Substituir o float por f’:

**print('A média de {} entre {}, {} e {} é igual a {}'.format(nome, n1, n2, n3, média))**

por →

**print(f'A média de {nome} entre {n1}, {n2} e {n3} é igual a {média}')**

→ Todo int é um float, mas nem todo int é um float

→ Manipulação de números:

**inteiro = 45**

**decimal = 45.789522458663236**

**print(f'{inteiro} {decimal:.5f}')**

- casas

**print(f'{inteiro} {decimal:+5f}')**

**print(f'{inteiro} {decimal:015.5f}')**

- casas antes

→ Para inverter os valores tem-se que colocar uma auxiliar para receber o valor antigo:

aux = x

x = y

y = aux

→ Para pular linha: /n

CÓDIGOS DA AULA:

[https://colab.research.google.com/drive/1DNqK8oHgf2xm9vcIHMzy1iTEo2iTmBLn#scrollTo=_9wdWDgqATTb](https://colab.research.google.com/drive/1DNqK8oHgf2xm9vcIHMzy1iTEo2iTmBLn#scrollTo=_9wdWDgqATTb)

[https://colab.research.google.com/drive/1HirtY6sy3qIKcwGskB6ta81QvJ3ydGMe?usp=share_link](https://colab.research.google.com/drive/1HirtY6sy3qIKcwGskB6ta81QvJ3ydGMe?usp=share_link)

[https://colab.research.google.com/drive/1eY3fnZEsrBvO_Y4uvGUHK9UB07qY6X_S?usp=share_link](https://colab.research.google.com/drive/1eY3fnZEsrBvO_Y4uvGUHK9UB07qY6X_S?usp=share_link)

**AULA 3: ESTRUTURA DE DECISÃO**

→ Permite tomada de decisão;

→ Expressões Lógicas =

- Operadores relacionais (== igualdade, >maior, <menor, >=maior ou igual, <= menor ou igual, !=diferente) tem que ter dois operandos, que pode ser de qualquer tipo

→ Operadores lógicos (and, or, not)

- bool: true or false
- Tabela ASCII
- Vai pelo código do elemento na tabela para fazer essas diferenças e igualdades, ex: ‘a’>’B’ false, pois 97>66;
- Compara de letra a letra "jose">"joaquim" é True pois o s vem depois do a
- '120'>'15' é False, pois vai de caracter a caracter e não o valor numérico
- 0 == false e 1==true
- O and só é true se ambos estiverem verdadeiros, um falso e dá false → T and T = T, todo o resto é false
- O or é true se um dos termos for atendido ou ambos forem
- O not é o oposto, V → F e F → V
- Prioridade: not → and → or

[](https://lh7-us.googleusercontent.com/kxT9ZZvGhrAZ9dDR8gu9izpndxy6FPL-AbQVWqgwfyVnpdJqdPp8AOWVkgBczOVgGYVAi-Hph_bTjoUKEIvI6otkMbpFIqZek6ONPiJTeS7sD2e01FC0OScMfEMOHcte4Jskr7TiOy_aJyUpIp4hxEc)

→ ord(‘a’) devolve o código do caractere → ord("U") 85

→ chr(97) devolve a correspondência → chr(85) 'U'

→ Só pode um por vez nesse sistema de ord

→ (IF :) comando só é executado se ele for true; else tá dentro do if; elif é a junção dos dois

- quando usa o elif: a primeira é if, as seguintes são elifs e a última é else;
- Decisão simples: sem o else;
- Decisão composta: tem o else; °Lembrar que o else já tem a condição do if nele, então não a coloque novamente
- Decisão aninhada: tem o elif;
- Quanto menos comparação mais desempenho: nos ifs ele faz todos, pois estão separados o que o torna mais lento e com menos desempenho do que o com else;
- O else e o elif possuem o mesmo desempenho o que é melhor no elif é a diminuição de espaços;
- .upper(): coloca tudo na maiúscula, bom para diminuir variáveis;
- no “or” tem que colocar as duas variáveis ou pode dar erro;

CÓDIGOS DA AULA:

[https://colab.research.google.com/drive/1njZpSdZbu2z81q5vmlraO57-dwk2exGq?usp=share_link](https://colab.research.google.com/drive/1njZpSdZbu2z81q5vmlraO57-dwk2exGq?usp=share_link)

[https://colab.research.google.com/drive/1HapAudETjFAiiEz22B1JS8wxEumLsyGi#scrollTo=6ZctgGeZu7LF](https://colab.research.google.com/drive/1HapAudETjFAiiEz22B1JS8wxEumLsyGi#scrollTo=6ZctgGeZu7LF)

**AULA 4: ESTRUTURA DE REPETIÇÃO**

→ **FOR:** o ‘in’, os ‘:’ e o ‘range’ são obrigatórios, afinal são usados para a repetição

- Quantidades de repetições determinadas
- Else: opcional, quando acabar os comandos;
- Existe sem o range

→ i

- O valor de *i* é setado para o valor do primeiro elemento da lista (ex: valor 0).

1. O código a ser repetido é executado.

2. O valor de i passa a ser o valor do elemento seguinte da lista, se houver um próximo elemento. Se não houver, encerra a execução do *for*. Se houver, volta ao passo *2*, com o valor de *i* já atualizado.

→ RANGE

- Tem três parâmetros:

° range (start, stop, step)

°valor inicial/start - opcional - valor 0, ou seja, a partir de onde eu quero começar;

°valor final -1/stop - obrigatório, ou seja, o máximo que vai ou até onde eu quero;

°incremento/step - opcional - valor 1, ou seja como eu quero a alternação ou de quanto em quanto ele vai até o valor final.

° ex:

maior = int(input())

for i in range (20)

n= int(input())

if n >maior:

maior = n

n = int(input('Digite um número inteiro n: '))

x = int(input('Digite um número inteiro x: '))

y = int(input('Digite um número inteiro y: '))

print('Os múltiplos de',n,'entre',x,'e',y,'são:')

for i in range (x,y+1):

if i % n == 0:

print(i,end=' ')

- coloca mais 1 pq eu quero que pare no 20 e não no 19.
- Eu quero que o resto da divisão seja zero, por isso uso o porcento e após o igual.

**→ WHILE:**

- definir as variáveis (0 ou 1, se operações)
- se a condição for True, entra no while
- input antes do laço e no final dele

1. Por contagem:

- for
- while

2. Por flag:

- while

° ler vários números e exibir a soma deles

(obs: a leitura do valor 999 indica o final dos dados)

s = 0

n = int(input('Digite um número inteiro: '))

while n != 999:

s = s + n

n = int(input('Digite um número inteiro: '))

print('Soma = ',s)

3. Por contagem:

→ Variável: o que eu quero usar, ex: i, se colocado com o termo que quero repetir ele faz uma contagem a partir do zero;

Olhar para ver o cálculo: [http://www.decom.ufop.br/romildo/2014-2/bcc701/praticas/p06-while-for-1.sol.pdf](http://www.decom.ufop.br/romildo/2014-2/bcc701/praticas/p06-while-for-1.sol.pdf)

**→ BREAK:**

- Quebra do laço
- while True: continue if not break
- O teste fica dentro do if, se ele for falso ele para

**→ CONTINUE:**

- Continua de onde ele está, forçado

CÓDIGOS DA AULA:

[https://colab.research.google.com/drive/1FZvJeOBGOinQrYa7LRZFtXkjmRJRlZFd#scrollTo=HK7FFWFLzqJe](https://colab.research.google.com/drive/1FZvJeOBGOinQrYa7LRZFtXkjmRJRlZFd#scrollTo=HK7FFWFLzqJe)

[https://colab.research.google.com/drive/1DuC1oEtDEq75Y8yAA-ZYAXvPlGWMFNkM?usp=sharing](https://colab.research.google.com/drive/1DuC1oEtDEq75Y8yAA-ZYAXvPlGWMFNkM?usp=sharing)

**AULA 5: VETOR**

→ É um tipo de dado;

→ Tipo estruturado (um monte de variáveis simples em conjunto ou variáveis compostas)

→ Vantagem de poder usar os dados repetidas vezes, com todos armazenados em um mesmo lugar

→ Possui um identificador e cada elemento pode ser diferenciado pelo índice

→ Vetores:

- Variável composta homogênea: tudo tem que ser o mesmo, ex: se é float é tudo float
- No python existe uma flexibilidade, porém no conceito original as listas para homogêneas e as tuplas para heterogêneas
- listas (pode-se remover, inserir, ou seja, possui uma flexibilidade) tuplas e dicionários
- O range cria um vetor

→ Como usar?

- Índice: posições dos elementos dentro dos vetores

°Começam do zero e são fixos

- Pode ser um vetor de qualquer tipo
- Crio o vetor com valores nulos [none] - se quiser mais índices eu coloco mais nones - e vou adicionando com inputs
- Um vetor não pode ser atribuído diretamente para outro vetor
- Acessar uma posição inválida de um vetor causará um erro na execução do programa

→LISTA: mesma coisa do vetor, na verdade vetor “não existe”;

- Lista vazia: []
- Para mostrar os elementos:

[0] = um só

[2:] = o que vem a partir do segundo

[:2] = até antes dele

[1:3] = do primeiro elemento citado até antes do segundo

[:] = a lista inteira

[-1] = volta 1 do fim pro início

→ Dá pra somar que nem nos elementos

CÓDIGOS DA AULA:

[https://colab.research.google.com/drive/1XGZ731i1PH6OCpNFjviyE4ujL3lhzcCv](https://colab.research.google.com/drive/1XGZ731i1PH6OCpNFjviyE4ujL3lhzcCv)

[https://colab.research.google.com/drive/11jrQIUwhdVNP-ZBudbAoKpfb8jbzBm42](https://colab.research.google.com/drive/11jrQIUwhdVNP-ZBudbAoKpfb8jbzBm42)

| ESTRUTURAS DE COMANDO | SINTAXE |
| --- | --- |
| Atribuição | = |
| Entrada | input |
| Saída | print |
| Decisão | if, elif, else |
| Repetição | for, while |

![Untitled](Algoritmos%20e%20Programa%C3%A7%C3%A3o%20Estruturada%20aa238c7ae3fe4c27ba9b5c7910a38943/Untitled.png)

![Untitled](Algoritmos%20e%20Programa%C3%A7%C3%A3o%20Estruturada%20aa238c7ae3fe4c27ba9b5c7910a38943/Untitled%201.png)

![Untitled](Algoritmos%20e%20Programa%C3%A7%C3%A3o%20Estruturada%20aa238c7ae3fe4c27ba9b5c7910a38943/Untitled%202.png)

![Untitled](Algoritmos%20e%20Programa%C3%A7%C3%A3o%20Estruturada%20aa238c7ae3fe4c27ba9b5c7910a38943/Untitled%203.png)