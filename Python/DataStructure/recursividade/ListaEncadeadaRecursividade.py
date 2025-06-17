'''
Classe que representa um nó na memória
'''


class Node:
    def __init__(self,data):
        self.__data = data
        self.__next = None        

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, newData):
        self.__data = newData

    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, newNext):
        self.__next = newNext


    def hasNext(self):
        return self.__next != None
    
    def __str__(self):
        return str(self.data)

class PosicaoInvalidaException(Exception):
    """Classe de exceção lançada quando uma violação no acesso aos elementos
       da lista, indicado pelo usuário, é identificada.
    """
    def __init__(self,msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
        """
        super().__init__(msg)


class ValorInexistenteException(Exception):
    def __init__(self,msg):
        super().__init__(msg)         
	    
'''
Esta classe implementa uma estrutura Lista Simplesmente Encadeada
'''
class Lista:
    # constructor initializes an empty ListaEncadeada of integers
    def __init__(self):
        self.__head = None
        self.__tamanho = 0

    def estaVazia(self):
        return True if self.__tamanho ==0 else False

    def __len__(self):
        return self.__tamanho

    def elemento(self, posicao):

        try:
            assert posicao > 0

            if (self.estaVazia()):
                raise PosicaoInvalidaException(f'Lista vazia')

            cursor = self.__head
            contador = 1
            while( (cursor != None) and (contador < posicao) ):
                cursor = cursor.next
                contador += 1

            if ( cursor != None ):
                return cursor.data
        
            raise PosicaoInvalidaException(f'A lista não contém {posicao} elementos. O máximo é {self.__tamanho}')

        except TypeError:
            raise PosicaoInvalidaException(f'A posição deve ser um número inteiro')            
        except AssertionError:
            raise PosicaoInvalidaException(f'A posicao não pode ser 0 (zero) ou um número negativo')
        except:
            raise


    def modificar(self, posicao, valor):
 
        try:
            assert posicao > 0, f'A posicao não pode ser 0 (zero) ou um número negativo'
            assert posicao <= self.__tamanho, f'Posicao invalida. Lista contém {self.__tamanho} elementos'
            assert not self.estaVazia(), 'Lista vazia'

            cursor = self.__head
            contador = 1
            while( cursor != None and contador < posicao ):
                cursor = cursor.next
                contador += 1

            cursor.data = valor
        except TypeError:
            raise PosicaoInvalidaException(f'A posição deve ser um número inteiro')            
        except AssertionError as ae:
            raise PosicaoInvalidaException(ae.__str__())
        except:
            raise      
    
    def busca(self, valor):
        if (self.estaVazia()):
            raise PosicaoInvalidaException(f'Lista vazia')

        cursor = self.__head
        contador = 1

        while( cursor != None ):
            if( cursor.data == valor):
                return contador
            cursor = cursor.next
            contador += 1
            
        raise ValorInexistenteException(f'O valor {valor} não está armazenado na lista')

    def inserir(self, posicao, valor ):

        try:
            assert posicao > 0

            # CONDICAO 1: insercao se a lista estiver vazia
            if (self.estaVazia()):
                if ( posicao != 1):
                    raise PosicaoInvalidaException(f'A lista esta vazia. A posicao correta para insercao é 1.')

                self.__head = Node(valor)
                self.__tamanho += 1
                return
            
            # CONDICAO 2: insercao na primeira posicao em uma lista nao vazia
            if ( posicao == 1):
                novo = Node(valor)
                novo.next = self.__head
                self.__head = novo
                self.__tamanho += 1
                return

            # CONDICAO 3: insercao apos a primeira posicao em lista nao vazia
            cursor = self.__head
            contador = 1
            while ( (contador < posicao-1) and  (cursor != None)):
                cursor = cursor.next
                contador += 1

            if ( cursor == None ):
                raise PosicaoInvalidaException(f'A posicao {posicao} é invalida para a atual lista')

            novo = Node(valor)
            novo.next = cursor.next
            cursor.next = novo
            self.__tamanho += 1

        except TypeError:
            raise PosicaoInvalidaException(f'A posição deve ser um número inteiro')            
        except AssertionError:
            raise PosicaoInvalidaException(f'A posicao não pode ser um número negativo ou 0 (zero)')
        except:
            raise


    def remover(self, posicao):
        try:
            assert posicao > 0

            if( self.estaVazia() ):
                raise PosicaoInvalidaException(f'Não é possível remover de uma lista vazia')

            cursor = self.__head
            contador = 1

            while( (contador <= posicao-1) and (cursor != None) ) :
                anterior = cursor
                cursor = cursor.next
                contador+=1

            if ( cursor == None ):
                raise PosicaoInvalidaException(f'Posicao {posicao} invalida para remoção')

            data = cursor.data

            if( posicao == 1):
                self.__head = cursor.next
            else:
                anterior.next = cursor.next

            self.__tamanho -= 1
            return data
        
        except TypeError:
            raise PosicaoInvalidaException(f'A posição deve ser um número inteiro')            
        except AssertionError:
            raise PosicaoInvalidaException(f'A posicao não pode ser um número negativo')
        except:
            raise       
              
    def __str__(self):

        str = 'Lista: [ '

        cursor = self.__head

        while( cursor != None ):
            str += f'{cursor.data}'
            cursor = cursor.next
            if (cursor != None):
                str += ', '
        str += ']'
        return str

    def printAuxiliar(self, No):
        if (No == None): #se o nó estiver vazio, retorne
            return 
        self.printAuxiliar(No.next)
        print(No.data, ' ', end='') #puxxe o próximo nó
        #avaançar recursivamente para o próximo nó

    def imprimirInvertido(self):
        self.printAuxiliar(self.__head) #não preciso me preocupar com a condição de parada
        #pois o printAuxiliar já fará isso internamente
