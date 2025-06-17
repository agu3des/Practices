from ListaEncadeadaRecursividade import *


lst = Lista()
try:
    lst.inserir(1,25)
    print(lst)
    lst.inserir(2,30)
    print(lst)
    lst.inserir(3,40)
    print(lst)
    lst.inserir(1,50)
    print(lst)
    print('Lista invertida: ')
    lst.imprimirInvertido()
    print()
    # lst.remover(1)
    # print(lst.elemento(-8))
    #print(lst.elemento(10))
    #print(lst.elemento('a'))
    print(f'Função elemento(2): ',lst.elemento(2))
    print(f'Função busca(30): ',lst.busca(30))
    #print(f'Função busca(19): ',lst.busca(19))


    valor = lst.remover(4)
    print(f'Removendo o 4o elemento da lista: {valor}')
    print(lst)
    #valor = lst.remover(10)
    #print(lst)

    print('Tamanho: ',len(lst))

    print('modificar()')
    print(lst)
    lst.modificar(3,55)
    print(lst)
    lst.modificar(4,55)
except PosicaoInvalidaException as pie:
    print(pie)
except ValorInexistenteException as vie:
    print(vie)     
except Exception as e:
    print('Nossos engenheiros vao analisar esse problema')
    print(e.__class__.__name__)