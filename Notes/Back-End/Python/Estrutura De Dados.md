# Estrutura De Dados

Estrutura de dados é o ramo da computação que estuda os diversos mecanismos de organização de dados para atender aos diferentes requisitos de processamento.

→ As estruturas de dados definem a organização, métodos de acesso e opções de processamento para a informação manipulada pelo programa.

→ API: conjunto de procedimentos que podem ser usados para manipular os dados na estrutura. Determina a visão funcional da estrutura de dados.

→ Tupla é empacotadora de dados, na lista você bota uma informação, na tupla se coloca várias.

aluno.append()

**↓       ↓**

objeto  método

Aprender sobre: (está no class)

- Arrays e Matrizes;
- Dicionários e tuplas; (1° tem métodos)
- Trabalhando com data e hora (datetime);
- Manipulação de arquivo texto;
- Manipulação de arquivo binário.

Introdução ao Paradigma O.O. (Programação Orientada a Objetos

→ Objetivo de auxiliar o programador

→Paradigma da programação, na qual o programador visualiza seu programa em execução como uma coleção de unidades (objetos) cooperantes que interagem entre si.

→ São conceitos abstratos.

Ex: uma transferência de dinheiro  entre das contas utiliza esses recursos / possuem as mesmas características (conta, é agência) porém valores diferentes (cpf, dinheiro/atributos) / funcionalidades ou métodos (podem transferir, receber) / classe (não manipulamos e sim definimos: dela você cria os objetos)

[](https://lh7-us.googleusercontent.com/4lWv8RxJuNEci_voOawhVobOAvqSyH8k4cWHNHxeKctmp4Hl8qCg-F1rqxYHTuhIPG5QRl-ASjcI_bNJsPYWF_TOU5wxI7-w9__zsMwVu-NVendyQTmFcBkvdut1gFWGHwCT4EXQAXS_FQ8AdwDS_ko)

- Os objetos possuem características/atributos/funcionalidade que são definidos na classe
- A classe é uma só, mas podem existir ‘n’ objetos

→Os objetos conhecem muito bem a si mesmos e respondem as mensagens de acordo com suas características(atributos) e com seus próprios métodos.

Objetos podem ser utilizados para modelar qualquer coisa → **↓**

[](https://lh7-us.googleusercontent.com/M_84feWnptcgXEvv6J0_hQ8RB18qcPXjwxc_TfYu5Mq56DXOxOumV2O_tiOxqLlJ0UM2QCQa4po2TpQib6lQVXMIQVrmJytHk7TFw90BCxOy5uFChWEoyW0C19rDcI1lWuDpsuEprkp0sHr0iMHzFdc)

- Facilidade de manutenção (programador 😄)
- Simplicidade
- Reusabilidade de código
- Modularização (faço em um ponto único)
- Vasta comunidade de usuários programando O.O.
- Aplicações Web
- Modelagem de Banco de Dados
- Aplicações Cliente/Servidor

Ex de Objeto:

[](https://lh7-us.googleusercontent.com/Jf46RCdV3513iQ_gA2vvuntZ7XXiKrc2iUyt068Pj8H48NfoJwTru0VtY2a_pWsolR34zQiiVgwg6ahu93INv2DHriCPSzasSG7GF-tmZLRu3gN1TOHmBGGWG8QxAoyCUtJ4mDY633yY7B6FFVbg2Mc)

| Estruturado | Orientado a Objetos |
| --- | --- |
| Procedimentos ativos agem sobre dados passivos
que foram passados a eles | Ao invés de passar dados a procedimentos,
requisita-se que objetos realizem operações
neles próprios |

→ Objetos (bloco fundamental de construção de programas)

→ Estrutura de dados (recebe funcionalidades)

→ Propriedades e Comportamento (são as caracterizações que os objetos recebem)

→ Mensagens (comunicação entre objetos)

→ O “dado” já vai estar disponível, de modo que não vai haver a possibilidade de pegar a informação errada.

1º Passo:

– Abstração (transpor essa entidade para o meu programa / pegar apenas as informações necessárias / entender um conceito numa linguagem de programação)

Ex: Uma lâmpada é um objeto que emite luz a uma certa intensidade quando está ligada.

[](https://lh7-us.googleusercontent.com/ONkCbXeDEQuLp1ux0mPUsnpUvGXk3tC8WL5frAiXto3Xk4XaTCXCttNgx_AZ635uCjeqpIqqAUuq_PcEWh991WTFetYbs2KA65GksnZvMw8Xi4l040A_aD1Y3DXXN4uzdVbwN58knKSV-WNTOZsMQtQ)

2º Passo:

–  AD (abstração de dados de acordo com o comportamento/manipulação apenas através de suas operações)  = definir as atribuições daquele objeto

– AP (abstração de procedimentos/tratar uma função como uma operação única e bem definida) = reter dados, têm essas ações / interagir com o objeto sem saber o que acontece lá dentro, chama a ação, métodos

– CLASSE (informar a linguagem o que estou inserindo / a especificação do dado inserido)

OBS: Cada método está correlacionado com uma propriedade

1º e 2º Ex: cartas de um baralho

cartas -classe → carta - objeto: 2 naipe copa → propriedades: naipe, cor → métodos: getnaipe()

peso, naipe, número, cor da carta: propriedades

Ex. abstração de um celular

[](https://lh7-us.googleusercontent.com/3eLskQxlfeLJEahJjB1UNm4KGBIw9xtSWzXWhC2J7sX7KGoD2_Z2xO2lZS8CsnvgiWBlVY8h4esXMKS43oOLsYPRI2qMhOhmKynjTnU84ogdF8PIweHOjAxXqAiHwtE6I0fNZ-8_khjmTXGjkUCF83I)

[https://drive.google.com/file/u/0/d/1Gh6Ao1jmEj7L036Ftn1s1-GF2wwQlRoO/view?usp=drive_web](https://drive.google.com/file/u/0/d/1Gh6Ao1jmEj7L036Ftn1s1-GF2wwQlRoO/view?usp=drive_web)

[](https://lh7-us.googleusercontent.com/rYf7h48w3aIO-6BLjcT72iyXgQtIvlP4h7rfbe5pjRxq2NbO4F3yG-A_HNjB-Pz6eZIkXmll-tTryifj65063Z4J6esyP85wDR1G_q-UPUmctUSLAHYryVx5hwfE6RkuSL91nX-pXaLRBbWBuXfIn8k)

→ Trabalhar com enumeração de modo que eu adiciono um nome e já relaciono direto, tem que ser relacionado, fazer sentido

ARRAY

→ Modelo para armazenar/gerenciar coleção de dados, permitindo acesso, remoção, etc

1° lineares: lista, fila e pilha (tem o deque também)

2° não lineares: árvore binária (se divide em de busca e avl), grafos

3° outra: hash table, matriz esparsa

Lista: pode inserir no começo, no final, onde quiser

também pode remover de qualquer parte

desde que seja uma posição válida no conjunto de elementos

Pilha: insere e remove da extremidade

Fila: insere por um lado e remove pelo oposto

Deque: insere e remove só pelas extremidades

→ **Técnicas** - sequencial e encadeada

- A **sequencial** deixa os elementos em posições consecutivas, como arrays
- Na **encadeada** os elementos são alocados individualmente, de forma dinâmica, e são interligados manualmente

° (guarda o endereço que está ligado), o último nó tem um terminador

→ Array (teoria) - tem tamanho fixo, tem que ser homogêneo com relação ao tipo de elementos dele

OBS: python não tem o array nativo

No array já vem pronto, na encadeada não, devemos criar - isto é chamado de nó

vai ser uma classe criada

ele vai ter uma carga: o que eu guardo dentro dele

ele só sabe quem tá na frente dele, seguindo uma sequência de link, quando ele encontrar um que possui um terminador, ele sabe que chegou ao fim

**LISTA SEQUENCIAL**

→ A lista tem uma liberdade máxima, eu posso alterá-la em qualquer local, de modo que o usuário pode fazer essa alteração. Precisa de uma segurança maior, pois o usuário pode fazer leseira

→ Na lista eu posso inserir em uma posição que já está presente, mas eu tenho que deslocar, é possível também o append

→ Pode funcionar como fila e como pilha, se adaptada

→ Tenho que ter acesso às duas extremidades, não trabalha com “topo”

→ Posição, pois eu posso escolher para onde vou

***PROVA:*** coloca um código para fazer outro

Pego o len - 1, por causa do índice / len (self) é o objeto, retorna o que está ocupado / ex: len de array = 7 x len de self = 4

Eu posso colocar ele nas posições que já tenho ou no próximo → logo len(self)+1

para fazer o append= posiçãoAtual + 1, posição -1, ele não vai sair do lugar, logo sai do for e só adiciona

**Conversão de Expressões**

→ Aplicação de Pilhas: pilha controla o fluxo de execução do programa

- os browsers implementam a ideia do histórico de páginas com a pilha
- ctrl z → vai restaurando do último para o primeiro

→ Formatos de expressão aritmética

→ **Infixo:** operador envolvido por operandos, um do lado direito e outro do esquerdo

com os parênteses pode-se mudar a precedência

- Pósfixa e Préfixa são formatos processados do infixa

**→ Pósfixa:** notação polonesa reversa

- Mais eficiente para expressões aritméticas
- Parênteses foram eliminados, precedência foi determinada

(5+3)/(2+7)

vai dar x / (2+7)

x / y = z

53-27+/ —-> 2 9 / -> 2/9

- O operador vem depois dos operandos
- Processa da esquerda para a direita

**→ Préfixa:** notação polonesa

- Os operadores vêm antes
- Pega o que tá mais perto dos operandos

/-AB+CD

***Termos:***

Operando: A…Z

Operadores: + -  2         * /   3     ^   4

Parênteses: ()  1

| Símbolo | Pilha | Saída |
| --- | --- | --- |
| A | [ ]← | A |
| + | [*] | A |
| ( | [*(] | A |
| B | [*(] | AB |
| + | [*(+] | AB |
| C | [*(+] | ABC |
| ) | [*] | ABC+ |
| / | [/] | ABC+* |
| D | [/] | ABC+*D/ |

→Se chegou operando manda para a saída (ex: tela)

→ Pelos dois operandos mais próximos (por par)

→ Se o operador no topo tiver prioridade maior ou igual ao que eu quero inserir, ele sai

→ A pilha é só para operador

→Parêntese de abertura: manda ele para a pilha, não precisa saber de nada dela

→Parêntese de fechamento: vai retirando até achar o de abertura / desempilha

→Retire com prioridade maior ou igual se já tiver algo

→Não pode ter dois de mesma procedência dentro da pilha

→Inverte a string de entrada, troca o fecha parênteses pelo de abre

**ÁRVORE**

Def: estrutura não linear adequada para a modelagem de relações hierárquicas

[](https://lh7-us.googleusercontent.com/Dfx_trQYZxLwESMnpZjfV8N9ZGuyHNGyOYhiUZJHTVHNS7LhiQ8maRTYJaqRZaSI-yOp8omJUx21Do9AWArlFg9_XiqwC-Y9N9tq4j1EW0lbq8c2TLB6gAs6BinqZUSQ5NnY5BMHdsUmgXsrDINT14A)

- Constituída por um conjunto de nós ou nodo = são os elementos
- Nó principal é a raiz
- Altura = são os níveis, quanto maior o nível, maior a altura. Futuramente isso pode afetar a busca, de forma que a árvore deve ser sempre otimizada

Ramificações ou subárvores = a partir de um ponto os ‘filhos’ dele, essa relação de filhos é de 1 distância

- O nó raiz depende do referencial
- Nó folha são os que não possuem filhos
- O número de subárvores de um nó determina seu grau
- O último nível de uma árvore diz sua profundidade
- Grau máximo: número máximo de subárvores

OBS: o grafo permite ser trabalhado sem ter um grau máximo definido

[](https://lh7-us.googleusercontent.com/ANijE2RrOuxm1p5UDvXIS1YMmkcOXexB9TS9f_wUBFC4kUxa866NzoD--9sgYIHR0OwrRCw2ZdNZCzyUtvum4COGR7_9zgLoSKEEW_kLs7fSXl6UkQ1gUEUThbopt2tuu3m7xbInKJ8i1gTDlBH59jE)

[](https://lh7-us.googleusercontent.com/9olL-odEqC79Imc62xiP0gQPLPDpAIAv5_f_TiKwz-d9vdtNG9OB5wh2JKUXp0y50g7KbjzlOeu-wDZMq1bIPWa5jQrWbs9UzyKQYA-H7f_AwjOeS1oZwxzrAcvRtccJ5Qq68rqVu3EYYLQgVGL0o5w)

ÁRVORE BINÁRIA

- Representação encadeada é melhor, a sequencial
- A diferença para o que estudamos é a parte hierárquica
- Sub-árvore: vem depois da raiz, uma sub-árvore pode ter um nó raiz
- A árvore completa é quando cada nó possui dois filhos, exceto os folhas - abriu um nível, todos os nós daquele nível devem ser preenchidos
- Os nós podem ter 1, 2 ou nenhum filho, um pai não se conecta com o filho de outro pai (não seria uma árvore binária)

Existem 3 tipos de árvores binárias:

1. Estritamente binárias: todos os nós não folhas possuem 2 descendentes
2. Completa: é estritamente binária e todos os nós folhas estão no mesmo nível de profundidade.

[](https://lh7-us.googleusercontent.com/O44flNIgSoFGU1L7BU06YU8USIEeqIwG0JBMHMoPjm1UTZi87aR50qEkwUFgkLK5vmRfrRgDyoNNsvyIgbLb7ccGDMAK3Jb2w9ACkQiYodbTC3tCwM59N-qD3Oot062CCZs7W9LCA8xhWH2HQf5loNs)

1. Quase-Completa: cada folha deve estar no nível d ou no nível d-1

escrita da esquerda para a direita, de cima para baixo

2p+1 e 2p+2

[](https://lh7-us.googleusercontent.com/UN6N1xYuLdsuKHbMaaeIuFUwePdiTwgZTM84YSBD4OtBEF0dJI23vE8Y7GQi8p2eEqSPddiUsN1KpQ4PFa_s-z1MyfbYbhhSEXmV2Cvxx24-uTY-LWfE4ZN2KhwEoD1HbqoDb8n8xJiWVTQTV8ryzvg)

preordem: chegando e fazendo

inordem: chega até o fim depois fazendo

posordem: chega até não ter mais nada e faz

Resolver questões que precisam de estruturas hierárquicas

ÁRVORE BINÁRIA DE BUSCA:

→ Def: Todos os nós da subárvore esquerda possuem valor numérico inferior e os da direita possuem valor maior que o nó raiz

→ A altura de um nó x em uma árvore binária é a distância entre x e o seu descendente mais afastado

Inordem, pela esquerda - ordem crescente

Inordem, pela direita = ordem decrescente

[](https://lh7-us.googleusercontent.com/KoFGe75En_qQelOAZPsyWo_ztGLXhmSK2jlnrpmb1uJWpvmD-ReTmOJl7tF7B9JVZYIVs_qmcIelEv_5pn-nStme9E1NSwkUx_Tm3OgC04-C3I_ML5pJtrbO2_mSLhamcD5gHv9SS-HLGC0t2MO7cyU)

→ Para adicionar o nó:

- Inicia-se a partir do nó raiz
- Se a chave do novo nó < node.dado, desce para o lado esquerdo. Caso contrário, desce para o lado direito
- Aplica a regra até encontrar um nó com filho esquerdo ou direito “vazio”
- Adiciona o novo nó no lado apropriado

OBS: Em python None é falso e qualquer outra coisa é verdadeiro

eq = equal, recebe um objeto e precisa comparar

Possibilidade de tratamento:

1. Nó a ser excluído não contém subárvores
2. O nó a ser excluído contém somente uma subárvore
3. O nó a ser excluído contém duas subárvores

A AVL é sobre balanceamento, ela faz rotações na árvore para mantê-la estável

A rotação tem um custo, que compensa

degeneração - sai como uma estrutura linear

0 nó folha

negativo o lado direito maior

positivo lado esquerdo maior

fb = he - hd

se tiver +1 -1 e zero tá balanceada

0 + 7 = 7 //2 = 3

3 divide para os dois lados

ele pega uma das metades

1+2+0 = 3 // 3 = 1

pega o 1 e coloca

0 para a esquerda

2 para a direita

r. esq

r. dir

r. esq + r. dir (dupla)

r. dir + r. esq (dupla)

quando tiver +2 e +1 ou seja mesmo sinal é simples = positivo direita

quando tiver -2 e -1 ou seja mesmo sinal é simples = negativo esquerda

pode estar balanceada, apenas sendo incompleta

- maior chave do esquerdo
- menor chave do lado direito
- subscreve e apaga

[](https://lh7-us.googleusercontent.com/YvLIC1gqk2sC7755gXS4Mbm6wMjqbt_Gp70FoENwKebKPV0p92zWylzdY3I2A9goncEmSOGh7ja-7tflpp1zcUf9_DtlreCRPLqH8Z_PKM1P436oWfpG1u4yPq5KD-p20LmCGgaaPwHa2lYKD0p3fX0)

**HASHING**

Mapeamento (chave, valor)

→ Valor é algo associado a chave

[](https://lh7-us.googleusercontent.com/oJ1EbZPk_y-Pys80T6BgFl-q5-wRsN9jmIL6iZDXTCSKEHTjY22ptCOmj3MsDfsKiFf0olUW6nQK2DBfxtGwm6rb8MHu7lhptqmZq8a8SK9TW68_jaS4Ee-pkoDwtYQn69SRIctTZd1UPExCTs7ItvM)

→ Para retornar um inteiro eu teria que fazer alguma operação que retornasse um número

→ Tem que gerar um índice dentro da tabela

→ Quando irá dar colisão:

→ Quanto mais simples melhor

k é a key

m é o len da tabela

h(K) = K % m

→esse k tem que chegar inteiro

→Não tem duplicidade, pois ela automaticamente substitui o valor existente

→O array deve ter um tamanho fixo

→Todos são inicializados com None

**REHASHING**

tô ocupado, vai para o da frente

Linear: pulo pequeno

rh(i) = (i+1) % m

Quadrática: pulo grande

No primeiro o ‘i’ é um número  inteiro que começa em 1, nas seguintes, a cada rehasing ele aumenta exponencialmente

rh(K) = (h(K) +i²)%m

Espalhamento duplo: mesmo que der errado, vai ser diferente por conta da relação k % numPrimo

h1 = K%m

h2 = numPrimo - (K%numPrimo)

numPrimo < m (nossa escolha)

rh(K) = (h1(K)+i*h2(K)) %m

**ENDEREÇAMENTO ABERTO**

→ Vantagem:

A busca é realizada diretamente ao bucket correspondente dentro da própria tabela hash

Ao invés de acessarmos ponteiros extras, calculamos a sequência de posições a serem percorridas

Aplicações com restrição de memória podem se beneficiar com esse tipo de implementação

→ Desvantagem:

Maior esforço de processamento para cálculo das posições disponíveis em caso de colisão (rehashing)

Em implementações de tabelas de dispersão de tamanho fixo, podemos lidar com a situação em que a hash table está cheia

**ENCADEAMENTO**

→ Se a posição do hash modular não tiver nenhuma, vai se inserir nela uma estrutura encadeada, que faça sentido, ex: listas

→ Cada índice do list eu crio outro list dentro dele

→ Pode-se fazer o instanciamento preguiçoso: eu tô por aqui, mas só vou agir se me chamar

[](https://lh7-us.googleusercontent.com/HPRX89SLVnpkFI4PqNBGOtGT67lLlTlonsOwfAheG0_uYqPWowqd95pkjAhuzZ1I3tRhOrRQneIyj7c5yi_qxuv320I8LcZmyS_r7mSj32WUDDKgUBvgdwPBfQu9BljqyZ4YjsAdMEnT9WvfBFH4sFg)

[](https://lh7-us.googleusercontent.com/GAOTia2xGQdGawKnlrMWvJDsiJgLazbtBdcH77VfLoA9AnXMa4MOPMjRsaUA8POAenabq18Ju9yoBLG_JOZKXbduPM1MqmvfWAXg0aMmideTpT5t_499Fb_sfwW9CsVNQabwra2_8aFuFcvyIWbmXys)