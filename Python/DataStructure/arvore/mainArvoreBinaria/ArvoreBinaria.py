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
    
class ArvoreBinaria:
    def __init__(self, raiz:any):
        '''Inicializa a árvore com um nó raiz'''
        self.__raiz = No(raiz)
        self.__cursor = self.__raiz
        
    def estaVazia(self)->bool:
        return self.__raiz == None

    def getRaiz(self)->any:
        '''Obtem a carga do nó "root"'''
        return self.__raiz.carga if self.__raiz != None else None

    def getCursor(self)->any:
        '''Obtem a carga do nó apontado pelo "cursor"'''
        return self.__cursor.carga if self.__raiz != None else None

    def resetCursor(self):
        '''Posiciona o cursor para o nó raiz'''
        self.__cursor = self.__raiz

    def descer_para_esquerda(self):
        '''Desloca o cursor para o seu filho esquerdo, apenas 
           se tiver filho esquerdo'''
        if self.__cursor is not None:
            if self.__cursor.esq is not None:
                self.__cursor = self.__cursor.esq

    def descer_para_direita(self):
        '''Desloca o cursor para o seu filho direito, apenas 
           se tiver filho direito'''
        if self.__cursor is not None:
            if self.__cursor.dir is not None:
                self.__cursor = self.__cursor.dir

    def addFilhoEsquerdo(self, carga:any):
        '''Adiciona um novo nó à esquerda do "cursor"
           Se cursor já tiver filho esquerdo, não faz nada.'''
        
        if self.__cursor is not None and self.__cursor.esq == None:
            self.__cursor.esq = No(carga)

    def addFilhoDireito(self, carga:any):
        '''Adiciona um novo nó à direita do "cursor"
           Se cursor já tiver filho direita, não faz nada.'''
        if self.__cursor is not None and self.__cursor.dir == None:
            self.__cursor.dir = No(carga)


    def busca(self, chave:any )->bool:
        '''Percorre a árvore à procura de um nó cuja carga corresponde
           à chave passada como argumento.
           Returns
           ---------
           True: a chave está presente na árvore
           False: caso a chave não esteja na árvore
        '''
        return self.__busca(chave, self.__raiz)

    def __busca(self, chave:any, no:No )->bool:
        if no is None:
            return False
        elif no.carga == chave:
            return True
        elif (self.__busca(chave,no.esq)):
            return True
        else:
            return self.__busca(chave, no.dir)


    def preordem(self):
        self.__preordem(self.__raiz)

    def __preordem(self, no):
        '''Exibe na tela os nós da árvore com percurso em pré-ordem'''
        if no is not None:
            print(no.carga, end=' ')
            self.__preordem(no.esq)
            self.__preordem(no.dir)

    def emordem(self):
        self.__emordem(self.__raiz)

    def __emordem(self, no):
        '''Exibe na tela os nós da árvore com percurso em-ordem'''
        if no is not None:
            self.__emordem(no.esq)
            print(no.carga, end=' ')
            self.__emordem(no.dir)

    
    def posordem(self):
        self.__posordem(self.__raiz)

    def __posordem(self, no):
        '''Exibe na tela os nós da árvore com percurso em pos-ordem'''
        if no is not None:
            self.__posordem(no.esq)
            self.__posordem(no.dir)
            print(no.carga, end=' ')

    def esvazia(self):
        '''Elimina todos os nós da árvore'''
        self.__raiz = self.__esvazia(self.__raiz)

    def __esvazia(self, no ):
        if ( no is not None):
            no.esq = self.__esvazia(no.esq)
            no.dir = self.__esvazia(no.dir)
        return None

    def remove(self, key:object):
        '''Remove o nó determinado pela chave de busca.
           IMPORTANTE:
           a) o cursor deve estar posicionado no nó pai referente ao nó chave.
           b) se não puder ser removido (árvore vazia, cursor no local errado,...)
              não é executada qualquer ação'''
        if self.__cursor is not None:
            if self.__cursor.esq is not None:
                if self.__cursor.esq.esq is None:
                    self.__cursor.esq = None            
            elif self.__cursor.dir is not None:
                if self.__cursor.dir.esq is None:
                    self.__cursor.esq = None


    def __str__(self):
        '''Exibe os nós da árvore com percurso em pré-ordem'''
        return 'Em desenvolvimento'

