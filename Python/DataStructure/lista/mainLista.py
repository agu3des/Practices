from ListaSequencialNumPy import *
#from ListaSimplesmenteEncadeada import Lista,ListaException

l1 = Lista()

# print(l1)

if l1.estaVazia():
    print('l1 esta vazia.')

print('Tamanho da lista:', len(l1))

try:
    for i in range(1,8):
        l1.inserir(i, i*10)
    print('Tamanho da lista:', len(l1))
    print(l1)
    l1.inserir(1,55)
    print('Tamanho da lista:', len(l1))
    print(l1)

    carga = l1.remover(1)
    print('Carga removida:', carga)
    print(l1)

    conteudo = l1.elemento(3)
    print(f'Elemento(3): {conteudo}')
    posicao = l1.busca(50)
    print(f'Posicao do elemento 50: {posicao}')

    for i in range(15):
        print('removendo:', l1.remover(1))
    print(l1)
except ListaException as ae:
    print(ae)
print(l1)

# print('Tamanho de l1:', len(l1))


# try:
#     for i in range(1,11):
#         l1.empilha(i*10)

#     print(l1)

#     print('Tamanho: ',len(l1))

    

#     posicao = 4
#     print(f'Elemento({posicao}):',l1.elemento(posicao))
#     print('busca(40):', l1.busca(40))

#     print('Removendo os 3 primeiros elementos do topo da pilha')
#     for i in range(3):
#         print(l1.desempilha())
#     print(l1)

    
# except PilhaException as pe:
#     print('ERRO:',pe)
# except Exception as e:
#     print('Erro:',e,'Classe: ',e.__class__.__name__)




