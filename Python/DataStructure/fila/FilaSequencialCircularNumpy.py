import numpy as np

class FilaException(Exception):
    def __init__(self,mensagem):
        super().__init__(mensagem)


class Fila:
    def __init__(self, size:int=10):
        self.__array = np.full(size,None,dtype=object)
        self.__frente = 0
        self.__final = -1
        self.__tamanho = 0


    def estaVazia(self)->bool:
        return self.__tamanho == 0

    def estaCheia(self)->bool:
        return self.__tamanho == len(self.__array)


    def __len__(self)->int:
        return self.__tamanho


    def elemento(self, posicao:int)->any:
        try:
            assert self.estaVazia() == False, 'Fila está vazia'
            assert posicao > 0 and posicao <= len(self), f'Posição {posicao} é inválida para a fila com {len(self)} elementos'
            
            index = self.__frente
            for i in range(posicao-1): #dizer quantas interações vai ter
                index = (index + 1) % len(self.__array)
            return self.__array[index]
        except AssertionError as ae:
            raise FilaException(ae)


    def busca(self, key:any)->int:
        index = self.__frente
        for i in range(len(self)): #se for zero ele já sai
            if self.__array[index] == key:
                return i+1
            index = index = (index + 1) % len(self.__array)
        raise FilaException(f'A chave {key} não está presente na lista')


    def enfileira(self, carga:any):
        try:
            assert not self.estaCheia(), 'Fila está cheia'
            # if self.__final == len(self.__array)-1:
            #     self.__final = 0 #circular, então quando chegar no fim vá para frente
            # else:
            #     self.__final += 1
            self.__final = (self.__final + 1) % len(self.__array)
            #o dividendo é menor que o divisor, fica o dividendo 5/7 = 5
            #se for 7/7 = 0, vai pro início
            self.__array[self.__final] = carga
            self.__tamanho += 1
        except AssertionError as ae:
            raise FilaException(ae)


    def desenfileira(self)->any:
        #pega quem tá na frente e devolve a carga
        try:
            assert not self.estaVazia(), 'Fila está vazia'
            carga = self.__array[self.__frente] #tenho que acessar a frente e guardar a carga que está lá
            self.__frente = (self.__frente + 1) % len(self.__array) #quando a frente chegar no último elemento, ele volta para o início
            self.__tamanho -= 1
            return carga
        except AssertionError as ae:
            raise FilaException(ae)


    def __str__(self)->str:
        s = 'frente->[ '
        index = self.__frente #mesma ideia do cursor
        for i in range(len(self)):
            s += f'{self.__array[index]}, '
            index = (index + 1) % len(self.__array) #não pode colocar a frente direto, pq se não a esvazio
        s = s.rstrip(', ')
        s += ' ]'
        return s

