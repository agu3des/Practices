from PilhaSequencialNumPy import *

p1 = Pilha()

# print(p1)

if p1.estaVazia():
    print('p1 esta vazia.')

print('Tamanho da pilha:', len(p1))

try:
    for i in range(1,11):
        p1.empilha(i*10)
    print('Tamanho da pilha:', len(p1))
    conteudo = p1.elemento(3)
    print(f'Elemento(3): {conteudo}')
    posicao = p1.busca(50)
    print(f'Posicao do elemento 50: {posicao}')
    print('Topo: ', p1.topo())

    for i in range(15):
        print('Desempilhando:', p1.desempilha())
    print(p1)
except PilhaException as ae:
    print(ae)
print(p1)

# print('Tamanho de P1:', len(p1))


# try:
#     for i in range(1,11):
#         p1.empilha(i*10)

#     print(p1)

#     print('Tamanho: ',len(p1))

    

#     posicao = 4
#     print(f'Elemento({posicao}):',p1.elemento(posicao))
#     print('busca(40):', p1.busca(40))

#     print('Removendo os 3 primeiros elementos do topo da pilha')
#     for i in range(3):
#         print(p1.desempilha())
#     print(p1)

    
# except PilhaException as pe:
#     print('ERRO:',pe)
# except Exception as e:
#     print('Erro:',e,'Classe: ',e.__class__.__name__)




