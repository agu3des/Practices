class PilhaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class No:
    def __init__(self, carga:any):
        self.carga = carga
        self.prox = None #acabou
    @property
    def carga(self):
        return self.__carga

    @property
    def prox(self):
        return self.__prox

    @carga.setter
    def carga(self, novaCarga):
        self,__carga = novaCarga

    @prox.setter
    def prox(self, novoProx):
        self,__carga = novoProx


class PilhaEncadeada:
    def __init__(self):
        #eu n coloco o tamanho, pois vai variar
        #self.__array = np.full(size, None, dtype=object)
        self.__topo = None #não tem nenhum encadeado, nenhum elemento
    #assim não funciona, pois eu teria que percorrer ela todinha, se eu considerar o primeiro como topo eu já tenho acesso direto
        self.__tamanho = 0 #o len
    def estaVazia(self)->bool:
        return self.__topo == None
    
    def __len__(self)->int:
        return self.__tamanho
    #não quiser adicionar nenhum atributo: pego o len e pulo de 1 em 1
    #adicionar atributo a mais: um contador / ganha em velocidade

    def elemento(self, posicao:int)->any:
        #me diga qual a carga que está armazenada em tal posição
        try:
            assert self.estaVazia() == False, 'A pilha está vazia.'
            assert posicao > 0 and posicao <= len(self), f'Posição {posicao} é inválida paara a pilha com {len(self)} elementos.'
            
            contador = 1
            #quanto eu avancei nos nós
            #tenho que saltar e salvar
            cursor = self.__topo
            while (cursor is not None):
                if contador == posicao:
                    return cursor.carga
                cursor = cursor.prox
                contador += 1
            # return self.__array[posicao-1]

        except AssertionError as ae:
            raise PilhaException(ae)
    
    def busca(self, key:any)->int:
        for i in range(len(self)):
            if self.__array[i] == key:
                return i+1
        raise PilhaException(f'A chave {key} não está presente na pilha.')
    
    def topo(self)->any:
        if self.estaVazia():
            raise PilhaException('Pilha vazia.')
        return self.__topo.carga
        # return self.__array[self.__topo]
        contador = 1
        cursor = self.__topo
        while (cursor is not None):
            if cursor.carga == key:
                return cursor.carga
            cursor = cursor.prox
            contador += 1
    
    def empilha(self, carga:any):
        # if self.__topo == len(self.__array)-1:
        #     raise PilhaException('Pilha cheia.')
        no = No(carga)
        novo.prox = self.__topo
        self.__topo = novo
        sel.__tamanho += 1
        # self.__topo += 1
        # self.__array[self.__topo] = carga

    def desempilha(self):
        #ela pode estar vazia
        #ele me delvolve  carga que estava armazenada / eliminando nó
        if self.estaVazia():
            raise PilhaException('Pilha vazia.')
        carga = self.__topo.carga #eu quero a carga do nó
        #eu tenho qwue salvar a carga antes para que python n lhe apague automaticamente
        #pois eu preciso que devolva a carga
        #eu quero que ele armazene o outro
        self.__topo = self.__topo.prox
        self.__tamanho -= 1
        return carga
    
    def __str__(self) -> str:
        s = 'topo->[ '
        cursor = self.__topo
        while (cursor is not None):
            s += f'{cursor.carga}, '
            cursor = cursor.prox
        s = s.rstrip(', ')
        s += ' ]'
        return s

        #para fazer percurso em dupla cadeada tbm
        #vai receber o sinal de partida / não pode usar o topo pq perdemos o valor dele
        #cursor = self.__topo
        #while (cursor is not None): #enquanto ele estiver apontando para algo real / objeto válido
            #quando vhegar no none sabe que ele percorreu tudo
            #<faz alguma coisa>
            #cursor = cursor.prox
            #estrutura encadeada até o último elemento
            #p/ fazer o str eu tenho que passar por todo mundo
    
