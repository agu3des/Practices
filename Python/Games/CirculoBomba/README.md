<h1 align="center">PROJETO CÍRCULO BOMBA</h1>


`"Círculo Bomba"` - Aplicação que simula um jogo. 

## Requisitos
+ `Python 3`
+ `VS Code`

## Instalação
1. Instale `Python 3` na sua máquina (caso não tenha).
2. Baixe ou clone o projeto para o seu computador.
3. Abra o terminal ou prompt de comando e navegue até o diretório do projeto.
4. Execute o comando `pip install numpy` para instalar as bibliotecas necessárias.
5. Inicie o programa executando o arquivo `main.py`.

## Uso
>  Mini projeto desenvolvido na disciplina de Estrutura de Dados (2023.2), utilizando a linguagem python, ministrada pelo professor Alex Cunha, no curso de Sistemas para Internet (IFPB).


## Exigências
+ `Estruturas de Dados: ` Pilha Encadeada, Lista Encadeada(com adaptações para funcionar de maneira circular)


## Funcionamento
O jogo funciona da seguinte maneira:
+ A brincadeira do círculo da bomba começa com a definição das pessoas que irão participar (sem limite de quantidade). 
+ Os participantes vão se organizar em círculo. Determina-se, então, quantas pessoas serão vencedoras, com 0 < numVencedores <= nº participantes -1.  
+ Uma pessoa é escolhida aleatoriamente para iniciar a passagem da bomba de confetes.
+ A partir do inicializador, uma música será tocada e a bomba será deslocada para os participantes seguintes, da direita para a esquerda, até que a música pare. Neste momento, o participante que ficou com a bomba é eliminado do jogo e a partida recomeça a partir do jogador sucessor. 
+ Enquanto a música estiver tocando, a bomba estará circulando pela roda de participantes. + Vamos considerar que a música vai ser tocada em uma quantidade de segundos 4 <= tempo <= 15 a cada iteração, e que cada segundo é o tempo da bola mudar de participante. 
+ Quando o programa identificar o(s) vencedor(es), será exibido o rastreamento dos participantes eliminados.


## Descrição do arquivo
| Nome | Descrição |
| ------ | ----------- |
| ListaEncadeadaCircular.py | Neste arquivo existe uma classe Lista, com seus respectivos métodos.|
| PilhaSimplesEncadeada.py | Neste arquivo existe uma classe Pilha, com seus respectivos métodos.|
| jogo.py | Neste arquivo existe uma classe Jogo, com seus respectivos métodos.|
| main.py | Neste arquivo existe a execução do jogo.|
| jogo.txt | Neste arquivo existe o armazenamento dos jogadores por rodada.|



### Alunas
- [Ananda Guedes](https://github.com/agu3des)
- [Angêlica Araújo](https://github.com/araujo-angel)