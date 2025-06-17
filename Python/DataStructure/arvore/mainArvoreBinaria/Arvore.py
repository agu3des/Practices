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
    def esq(self):
        return self.__esq

    @property
    def dir(self):
        return self.__dir

    @carga.setter
    def carga(self, novaCarga):
        self.__carga = novaCarga

    @esq.setter
    def esq(self, novoEsq):
        self.__esq = novoEsq

    @dir.setter
    def dir(self, novoDir):
        self.__dir = novoDir

    def __str__(self):
        return f'{self.__carga}'

def preorder(node):
    if node is not None:
        print(node.carga, end=' ')
        preorder(node.esq)
        preorder(node.dir)

# main
raiz = No(10)
raiz.esq = No(5)
raiz.dir = No(15)
raiz.esq.esq = No(2)
raiz.esq.dir = No(7)
raiz.dir.esq = No(12)
raiz.dir.dir = No(20)
preorder(raiz)
