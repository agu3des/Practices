class ArvoreException(Exception):
    def __init__(self,mensagem):
        super().__init__(mensagem)


class No:
    def __init__(self, carga:any):
        self.__carga = carga
        self.__esq = None
        self.__dir = None

    @property
    def carga(self):
        return self.__carga
    
    @property
    def prox(self):
        return self.__prox

    @carga.setter
    def carga(self, novaCarga):
        self.__carga = novaCarga

    @prox.setter
    def prox(self, novoProx):
        self.__prox = novoProx

    @esq.setter
    def esq(self, novoEsq):
        self.__esq = novoEsq

    @dir.setter
    def dir(self, novoDir):
        self.__dir = novoDir

    def __str__(self):
        return f'{self.__carga}'
    
class ArvoreBinaria:
    #não vai permitir o erro "humano", permite o crescimento
    def __init__(self):
        self.__root = None
        self.__tamanho = 0 #já pego o tamanho direto
        self.__cursor = None #o root não pode sair daqui, então o cursor percorre para remoção e inserção

#com função
def preordem(no:No):
    if no is not None:
        print(no, end='')
        preordem(no.esq) #chamada recursiva para esquerda
        preordem(no.dir) #chamada recursiva para direita
        #chega no A ve que n é none printa, vai pro c ve se n é none printa vai pro d verifica esquerda e direita como
def inordem(no:No):
    if no is not None:
        inordem(no.esq) 
        print(no, end='')
        inordem(no.dir) 

def posordem(no:No):
    if no is not None:
        posordem(no.esq) 
        posordem(no.dir) 
        print(no, end='')

#na mão
if __name__ == '__main__':
    root = No('A')
    root.esq = No('C')
    root.dir = No('B')
    root.esq.dir = No('E')
    root.esq.esq = No('H')
    root.dir.dir = No('Z')
    root.dir.esq = No('H')
    root.dir.esq = root.dir

    preordem(root)

# class Arvore:
#     def __init__(self):
#         self.__head = None
#         self.__tamanho = 0
        
#     def estaVazia(self)->bool:
#         return self.__head == None

#     def __len__(self)->int:
#         return self.__tamanho

#     def elemento(self, posicao:int)->any:
#         try:
#             assert self.estaVazia() == False, 'Pilha está vazia'
#             assert posicao > 0 and posicao <= len(self), f'Posição {posicao} é inválida para a pilha com {len(self)} elementos'

#             contador = 1
#             cursor = self.__head
#             while( cursor is not None ):
#                 if contador == posicao:
#                     return cursor.carga
#                 cursor = cursor.prox
#                 contador += 1            
#         except AssertionError as ae:
#             raise ArvoreException(ae)
                
#     def busca(self, key:any)->int:
#         if (self.estaVazia()):
#             raise ArvoreException('Pilha está vazia')
#         contador = 1
#         cursor = self.__head
#         while( cursor is not None ):
#             if cursor.carga == key:
#                 return contador
#             cursor = cursor.prox
#             contador += 1
#         raise ArvoreException(f'A chave {key} não está presente na pilha')


#     def inserir(self, posicao:int, carga:any):
#         try:
#             assert posicao > 0 and posicao <= len(self)+1, f'Posição {posicao} é inválida para a Arvore com {len(self)} elementos'

#             # CONDICAO 1: insercao se a Arvore estiver vazia
#             if (self.estaVazia()):
#                 self.__head = No(carga)
#                 self.__tamanho += 1
#                 return 
#             # CONDICAO 2: insercao na primeira posicao em uma Arvore nao vazia
#             if ( posicao == 1):
#                 novo = No(carga)
#                 novo.prox = self.__head
#                 self.__head = novo
#                 self.__tamanho += 1
#                 return
#             # CONDICAO 3: insercao apos a primeira posicao em Arvore nao vazia
#             cursor = self.__head
#             contador = 1
#             while ( contador < posicao-1):
#                 cursor = cursor.prox
#                 contador += 1
#             novo = No(carga)
#             novo.prox = cursor.prox
#             cursor.prox = novo
#             self.__tamanho += 1

#         except AssertionError:
#             raise ArvoreException(f'A posicao não pode ser um número negativo ou 0 (zero)')


#     def remover(self, posicao:int)->any:
#         try:
#             assert not self.estaVazia(), 'Arvore está vazia'
#             assert posicao > 0 and posicao <= len(self), f'Posição {posicao} é inválida para a Arvore com {len(self)} elementos'

#             cursor = self.__head
#             contador = 1
#             while( contador <= posicao-1) :
#                 anterior = cursor
#                 cursor = cursor.prox
#                 contador+=1

#             carga = cursor.carga

#             if( posicao == 1):
#                 self.__head = cursor.prox
#             else:
#                 anterior.prox = cursor.prox

#             self.__tamanho -= 1
#             return carga
#         except AssertionError as ae:
#             raise ArvoreException(ae)
        
#     def __str__(self)->str:
#         s = 'head->[ '
#         cursor = self.__head
#         while( cursor is not None ):
#             s += f'{cursor.carga}, '
#             cursor = cursor.prox
#         s = s.rstrip(', ')
#         s += ' ]'
#         return s



        

 

