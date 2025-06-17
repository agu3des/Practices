class ListaException(Exception):
    def __init__(self,mensagem):
        super().__init__(mensagem)


class No:
    def __init__(self, carga:any):
        self.__carga = carga
        self.__prox = None
    
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

    def __str__(self):
        return f'{self.__carga}'




class Lista:
    """A classe Pilha implementa a estrutura de dados "Pilha".
       Técnica: <Encadeamento/Sequencial>
       A classe foi desenvolvida de maneira a permitir que qualquer tipo de dado
       seja armazenado como carga de um nó.

     Atributos:
     ---------------------
        *definir a lista de atributos*
    """
    def __init__(self):
        """ Construtor padrão da classe Pilha sem argumentos. Ao instanciar
            um objeto do tipo Pilha, esta iniciará vazia. 
        """
        self.__head = None
        self.__tamanho = 0
        
    def estaVazia(self)->bool:
        return self.__head == None

    def __len__(self)->int:
        return self.__tamanho

    def elemento(self, posicao:int)->any:
        try:
            assert self.estaVazia() == False, 'Pilha está vazia'
            assert posicao > 0 and posicao <= len(self), f'Posição {posicao} é inválida para a pilha com {len(self)} elementos'

            contador = 1
            cursor = self.__head
            while( cursor is not None ):
                if contador == posicao:
                    return cursor.carga
                cursor = cursor.prox
                contador += 1            
        except AssertionError as ae:
            raise ListaException(ae)
                
    def busca(self, key:any)->int:
        if (self.estaVazia()):
            raise ListaException('Pilha está vazia')
        contador = 1
        cursor = self.__head
        while( cursor is not None ):
            if cursor.carga == key:
                return contador
            cursor = cursor.prox
            contador += 1
        raise ListaException(f'A chave {key} não está presente na pilha')



    def inserir(self, posicao:int, carga:any):
        try:
            assert posicao > 0 and posicao <= len(self)+1, f'Posição {posicao} é inválida para a lista com {len(self)} elementos'

            # CONDICAO 1: insercao se a lista estiver vazia
            if (self.estaVazia()):
                self.__head = No(carga)
                self.__tamanho += 1
                return
            
            # CONDICAO 2: insercao na primeira posicao em uma lista nao vazia
            if ( posicao == 1):
                novo = No(carga)
                novo.prox = self.__head
                self.__head = novo
                self.__tamanho += 1
                return

            # CONDICAO 3: insercao apos a primeira posicao em lista nao vazia
            cursor = self.__head
            contador = 1
            while ( contador < posicao-1):
                cursor = cursor.prox
                contador += 1

            novo = No(carga)
            novo.prox = cursor.prox
            cursor.prox = novo
            self.__tamanho += 1

        except AssertionError:
            raise ListaException(f'A posicao não pode ser um número negativo ou 0 (zero)')


    def remover(self, posicao:int)->any:
        try:
            assert not self.estaVazia(), 'Lista está vazia'
            assert posicao > 0 and posicao <= len(self), f'Posição {posicao} é inválida para a lista com {len(self)} elementos'

            cursor = self.__head
            contador = 1
            while( contador <= posicao-1) :
                anterior = cursor
                cursor = cursor.prox
                contador+=1

            carga = cursor.carga

            if( posicao == 1):
                self.__head = cursor.prox
            else:
                anterior.prox = cursor.prox

            self.__tamanho -= 1
            return carga
        except AssertionError as ae:
            raise ListaException(ae)

        
    def __str__(self)->str:
        s = 'head->[ '
        cursor = self.__head
        while( cursor is not None ):
            s += f'{cursor.carga}, '
            cursor = cursor.prox
        s = s.rstrip(', ')
        s += ' ]'
        return s



        

 

