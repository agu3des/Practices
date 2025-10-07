# Design Patterns

- Exe01
    
    
    | **Princípio Violado** | **Onde e Como Foi Encontrado** | **Sugestão para Correção** |
    | --- | --- | --- |
    | **Encapsulamento**
    (Ocultação da informação) | leftChild e rightChild setters aceitam object, o que permite atribuição de tipos incorretos. | Verificar se newLeftChild e newRightChild são instâncias de Node ou None usando isinstance(). |
    | **SRP**
    (Princípio da Responsabilidade Única) | O método viewtree mistura lógica de dados com exibição (print), que não deveria estar dentro da estrutura de dados. | Separar a lógica de visualização da lógica da árvore. Criar um método que apenas **retorna** os dados a serem exibidos, e imprimir fora da classe. |
    | **DRY**
    (Don't Repeat Yourself) | No método __searchData, o mesmo self.__searchData(chave, node.leftChild) é chamado duas vezes. | Armazenar o resultado em uma variável (left_result) e reutilizar, evitando duplicação. |
    | **Coesão**
    (Alto acoplamento visual com print) | Uso excessivo de print dentro da classe BinaryTree, que deveria apenas estruturar dados e não exibir diretamente. | Substituir print por métodos que retornem dados manipuláveis (listas, strings, objetos), mantendo a responsabilidade de exibir fora da classe. |
    | **Substituibilidade de Liskov** | O método insertLeft e insertRight da classe Node podem permitir tipos incorretos sem verificação, o que quebra o contrato esperado para os filhos. | Verificar tipo em tempo de execução com isinstance(data, Node) ou criar exceções customizadas para sinalizar mau uso. |
    | **Coesão + SRP** | O main trata leitura de arquivos, criação da árvore, inserção, busca e interação com usuário — tudo em um único escopo. | Modularizar: separar lógica de **leitura de arquivo**, **construção da árvore**, **interface do usuário**, etc., em funções ou classes distintas. |
    | **Abstração / Uso de Padrões de Projeto** | Nenhum padrão como **Composite**, **Visitor** ou **Iterator** é aplicado na navegação ou exibição das árvores. | Avaliar uso de padrões: Composite para a estrutura de nós, Visitor para percursos e Iterator para navegar pelos filhos da árvore de forma genérica. |
    | **Robustez (Defensive Programming)** | A função deleteNode falha silenciosamente se o cursor não estiver posicionado corretamente ou se o key não for filho direto. | Lançar mensagens ou exceções explicando o erro ao usuário ou retornar um valor indicando falha na operação. |
    | **Abstração de Interface (Interface Segregation)** | Os métodos públicos da BinaryTree expõem diretamente Node, que é uma implementação interna. | Criar uma camada de abstração: em vez de retornar Node, criar um DTO ou uma interface de acesso (como TreeNodeView). |
    | **Naming / Readability (Boas práticas de nomeação)** | Variáveis como listaDeArvores, listaDaUrlBuscada e filho são usadas sem padronização, com nomes longos, pouco claros em contextos repetidos. | Usar nomes consistentes, descritivos e concisos como treeList, urlSegments, childNode, etc. |
    
    ```python
    '''
    Classe para instanciação de nós que vão ficar na memória
    '''
    
    from logging import root
    
    class Node:
        def __init__(self,data:object):
            self.__data = data
            self.__leftChild = None
            self.__rightChild = None
    
        @property
        def data(self)->object:
            return self.__data
    
        @data.setter
        def data(self, newData:object):
            self.__data = newData
    
        @property
        def leftChild(self)->'Node':
            return self.__leftChild
    
        @leftChild.setter
        def leftChild(self, newLeftChild:object):
            self.__leftChild = newLeftChild
    
        @property
        def rightChild(self)->'Node':
            return self.__rightChild
    
        @rightChild.setter
        def rightChild(self, newRightChild:'Node'):
            self.__rightChild = newRightChild
    
        def insertLeft(self, data:object):
            if self.__leftChild == None:
                self.__leftChild = Node(data)	
    
        def insertRight(self,data:object):
            if self.__rightChild == None:
                self.__rightChild = Node(data)
    
        def __str__(self):
            return str(self.__data)
    
        def hasLeftChild(self)->bool:
            return self.__leftChild != None
    
        def hasRightChild(self)->bool:
            return self.__rightChild != None
            
    
    '''
    Classe para a instanciação de Árvores Binárias
    Autor: Alex Sandro
    Data da última modificação: 11/05/2022
    '''
    class BinaryTree:
        # constructor that initializes an empty Tree 
        def __init__(self, data_root:object):
            self.__root = Node(data_root)
            # O cursor é um apontador usado para navegar na árvore (sem mexer no root)
            self.__cursor = self.__root
    
        def getRoot(self)->'Node':
            '''Obtem a referência para o nó "root"'''
            return self.__root
    
        def getCursor(self)->'Node':
            '''Obtem a referência para o nó apontado pelo "cursor"'''
            return self.__cursor
    
        def downLeft(self)->'Node':
            '''Desloca para o filho a esquerda do nó "cursor"
               Se não tiver filho, retorna None'''
            if(self.__cursor.hasLeftChild()): 
                self.__cursor = self.__cursor.leftChild
                return self.__cursor
            else:
                return None
                
        def downRight(self)->'Node':
            '''Desloca para o filho à direita do nó "cursor"
               Se não tiver filho, retorna None'''        
            if(self.__cursor.hasRightChild()): 
                self.__cursor = self.__cursor.rightChild
                return self.__cursor
            else:
                return None
    
        def addLeftChild(self, dado:object):
            '''Adiciona um filho à esquerda do nó apontado pelo "cursor"
               Se cursor já tiver filho esquerdo, não faz nada.'''
            if(not self.__cursor.hasLeftChild()):
                self.__cursor.leftChild = Node(dado)
                self.downLeft()
                
    
        def addRightChild(self, dado:object):
            '''Adiciona um filho à direita do nó apontado pelo "cursor"
               Se cursor já tiver filho direito, não faz nada.'''
            if(not self.__cursor.hasRightChild()):
                self.__cursor.rightChild = Node(dado)
                self.downRight()
    
        def resetCursor(self):
            '''Posiciona o cursor para o nó raiz'''
            self.__cursor = self.__root
    
        def search(self, chave:object )->Node:
            '''Realiza uma busca na árvore pelo nó cuja carga é igual à chave
               passada como argumento.
               Returns
               ---------
               True: caso a chave seja encontrada na árvore
               False: caso a chave não esteja na árvore
            '''
            return self.__searchData(chave, self.__root)
        
        def __searchData(self, chave, node):
            if (node == None):
                return None # Nao encontrou a chave
            if ( chave == node.data):
                return node
            elif ( self.__searchData( chave, node.leftChild)):
                return  self.__searchData( chave, node.leftChild)
            else:
                return self.__searchData( chave, node.rightChild)
    
        def preorderTraversal(self):
            '''Exibe os nós da árvore com percurso em pré-ordem'''
            self.__preorder(self.__root)
            
        def __preorder(self, node):
            if( node == None):
                return
            print(f'{node.data} ',end='')
            self.__preorder(node.leftChild)
            self.__preorder(node.rightChild)
    
        def viewtree(self, node):
            self.__viewtree(self.__root, node, False, "") 
    
        def __viewtree(self, node, printarSoApartirDesseNode, podePrintar, minhaString):
            if( node == None):
                return
            minhaString = minhaString + node.data + "/"
            if node.data == printarSoApartirDesseNode.data:
                podePrintar = True
            if podePrintar == True:
                print(minhaString)
            self.__viewtree(node.leftChild, printarSoApartirDesseNode, podePrintar, minhaString)
            self.__viewtree(node.rightChild, printarSoApartirDesseNode, podePrintar, minhaString)
    
        def deleteTree(self):
            '''Elimina todos os nós da árvore'''
            # garbage collector fará o trabalho de eliminação dos nós
            # abandonados 
            self.__root = None
    
        # o cursor tem que estar posicionado no nó pai
        # do nó que vai ser removido
        def deleteNode(self, key:object):
            '''Remove o nó determinado pela chave de busca.
               IMPORTANTE:
               a) o cursor deve estar posicionado no nó pai ao nó chave.
               b) se não puder ser removido (árvore vazia, cursor no local errado,...)
                  não é executada qualquer ação'''
            self.__deleteNode(self.__cursor, key)
    
        def __deleteNode(self,root, key):
    
            if root is None: 
                return
            elif root.leftChild == None and root.rightChild == None:
                return
            
            if root.leftChild == None:
                if root.rightChild.data == key:
                    root.rightChild = None
            elif root.rightChild == None:
                if root.leftChild.data == key:
                    root.leftChild = None
    
    if __name__ == '__main__':  
        print('Olá! Bem-vindo ao nosso programa ;D','\n')
        
    while True:
        try:
            obtendo_arq = input('DIGITE O NOME DO ARQUIVO TEXTO QUE VOCÊ QUER ABRIR: ')
            arq = open(obtendo_arq,'r')
            arquivo = arq.readlines()
            listaDeArvores = []
        except Exception:
            print('Arquivo inexistente, tente novamente um nome valido','\n')
            continue
    
        for dominio in arquivo:
            dominio = dominio.lower()
            listaDominio = dominio.split('/')
            # print(listaDominio)
            # o .strip() remove o \n
            dominioRaiz = listaDominio[0].strip() #obtem a raiz da árvore
    
            arvoreQueJaExiste = None
    
            # Aqui vamos pesquisar se ja existe uma arvore na listaDeArvores para o dominioRaiz
            for arvoreDaLista in listaDeArvores:
                if arvoreDaLista.getRoot().data == dominioRaiz:
                    arvoreQueJaExiste = arvoreDaLista
                    # se eh igual quer dizer que ja existe uma arvore para esse dominioRaiz
    
            if arvoreQueJaExiste == None:
                # cria uma nova arvore
                novaArvore = BinaryTree(dominioRaiz)
                listaDeArvores.append(novaArvore)
                arvoreQueJaExiste = novaArvore
    
            arvoreQueJaExiste.resetCursor()
            
            # usar o listaDominio para inserir os novos filhos
            for filho in listaDominio[1:]:
                filho = filho.strip()
                noFilho = arvoreQueJaExiste.search(filho)
                if noFilho == None:
                    # nao achou o filho, tem que inserir
                    if arvoreQueJaExiste.getCursor().hasLeftChild() == False:
                        # posso botar na esquerda
                        arvoreQueJaExiste.addLeftChild(filho)
                    else:
                        arvoreQueJaExiste.addRightChild(filho)
                        # preciso  botar na direita
                elif arvoreQueJaExiste.getCursor().leftChild.data == filho:
                    arvoreQueJaExiste.downLeft()
                else:
                    arvoreQueJaExiste.downRight()
    
        while True:
    
            urlBuscada = input('\nDigite a URL de pesquisa ou #sair para encerrar o programa.\nURL:').lower()
            listaDaUrlBuscada = urlBuscada.split("/")
            listaViewTreeSplit = urlBuscada.split(" ")
    
            if urlBuscada == "#sair" :
                print('PROGRAMA ENCERRADO!','\n')
                break
    
            if listaViewTreeSplit[0] == "#viewtree" :
                dominioViewTree = listaViewTreeSplit[1]
                dominioViewTreeLista = dominioViewTree.split("/")
                dominioViewTreeRaiz = dominioViewTreeLista[0]
                deuErrado = True
                # Aqui vamos pesquisar se ja existe uma arvore na listaDeArvores para o dominioRaiz
                for arvoreDaLista in listaDeArvores:
                    arvoreDaLista.resetCursor()
                    if arvoreDaLista.getRoot().data == dominioViewTreeRaiz:
                        deuErrado = False
                        for filho in dominioViewTreeLista[1:]:
                            if arvoreDaLista.getCursor().leftChild is not None and arvoreDaLista.getCursor().leftChild.data == filho:
                                arvoreDaLista.downLeft()
                            elif arvoreDaLista.getCursor().rightChild is not None and arvoreDaLista.getCursor().rightChild.data == filho:
                                arvoreDaLista.downRight()
                            else:
                                deuErrado = True
                        if deuErrado == False:
                            arvoreDaLista.viewtree(arvoreDaLista.getCursor())
                if deuErrado:
                    print("URL não existe")
                continue
    
            dominioRaiz = listaDaUrlBuscada[0]
    
            achei = True
            arvoreAserBuscada = None
    
            for arvore in listaDeArvores:
                arvore.resetCursor()
                raiz = arvore.getRoot()
                if raiz.data == dominioRaiz:
                    arvoreAserBuscada = arvore
    
            if arvoreAserBuscada == None:
                print('400 Bad Request - Servidor não atendeu a requisição.')
                continue
            
    
            for filho in listaDaUrlBuscada[1:]:
                if arvoreAserBuscada.getCursor().leftChild is not None and arvoreAserBuscada.getCursor().leftChild.data == filho:
                    arvoreAserBuscada.downLeft()
    
                elif arvoreAserBuscada.getCursor().rightChild is not None and arvoreAserBuscada.getCursor().rightChild.data == filho:
                    arvoreAserBuscada.downRight()
    
                else:
                    achei = False
    
            if achei:
                print('200 OK - Requisição bem-sucedida!')
            else:
                print('400 Bad Request - Servidor não atendeu a requisição.')
    
    ```