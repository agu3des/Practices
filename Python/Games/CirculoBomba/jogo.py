from ListaEncadeadaCircular import *
from PilhaSimplesmenteEncadeada import *
import random
from termcolor import colored, cprint
import time

class JogoException(Exception):
    """Classe de exceção lançada quando uma violação no acesso aos elementos
    do jogo, indicado pelo usuário, é identificada.
    """
    def __init__(self,msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
        embutir na exceção.
        """
        super().__init__(msg)


class Jogo:
    def __init__(self):
        """
        No construtor da classe jogo, criamos os atributos jogadores e removidos e instanciamos a lista e a pilha nos mesmos.
        """
        self.__jogadores = Lista() #Aqui nossa lista é instanciada
        self.__removidos = Pilha() #Aqui nossa pilha é instanciada
        self.__qtdVencedores = 0

    def addParticipantes(self, posicao:int, participante):
        """
        Método que adiciona os participantes na lista.
        """
        try:
            assert posicao > 0 and posicao <= len(self.__jogadores)+1, f'Posição inválida. O jogo contém {self.__tamanho} participantes.'
            self.__jogadores.inserir(posicao, participante)#aqui nosso objeto da classe lista insere os jogadores

        except AssertionError as ae:
            raise ListaException(ae)

    def addQtdVencedores(self, qtdVencedores:int):
        """
        Método que recebe a quantidade de vencedores.
        """
        try:
            self.__qtdVencedores = qtdVencedores

        except AssertionError as ae:
            raise ListaException(ae)
    

    def rodada(self, num):
        """
        Método que gera as rodadas do jogo de acordo com as regras do mesmo.
        """
        self.__temp = random.randint(4, 16)
        print(colored(f'Participantes:{self.__jogadores}', attrs=['bold'])) #nossa lista de jogadores
        print(f'Rodada: {num}') #numero da rodada
        print(colored(f'Pointer: {self.__jogadores.pointer()}', 'blue')) #jogador/a da vez
        print(f'K: {self.__temp}')#numero de voltas
        for i in range(self.__temp):
            carga = self.__jogadores.pedirProximo()
            print(f'A bomba está passando por: {carga}')
            time.sleep(1)
            if i+1 == self.__temp:
                posicao = self.__jogadores.busca(carga)
                self.__removidos.empilha(carga)#aqui quem foi removido é passado pra pilha de removidos
                print(colored(f'Removido: {carga}', 'red'))  
                self.__jogadores.remover(posicao)#aqui ele/ela é deletado


    def executar(self):
        """
        Método que executa jogo.
        """
        self.__jogadores.preparaPercurso(1)#prepara o ponteiro para percorrer a lista a partir do nó correspondente à posicao indicada, no caso, 1.
        num_rodada = 0 #contador das rodadas
        while len(self.__jogadores) > self.__qtdVencedores: #laço que controla as iterações da jogada de acordo com a regra estabelecida.
            num_rodada += 1
            self.rodada(num_rodada)#nossa função rodada é chamada aqui, de forma que nela, o jogo de fato começa a funcionar de acordo com as regras pré-estabelecidas.
        print(colored(f'Vencedor(es) após {num_rodada} rodadas: <<< {self.__jogadores} >>>', 'green')) 

    def printPilha(self):
        """ Método que retorna a ordenação atual dos elementos da pilha, do
            topo em direção à base.

        Returns:
        str: Participantes eliminados do jogo, são elementos da pilha, do topo até a base.
        """  
        eliminados = 'Percurso para a vitória: '
        for i in range (len(self.__removidos)):
            eliminados += f'{self.__removidos.desempilha()} < ' #mostra os eliminados do último para o primeiro
        eliminados = eliminados.rstrip('< ') #remove o último <
        eliminados += ' '
        print (eliminados)