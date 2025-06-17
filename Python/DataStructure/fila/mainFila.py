from FilaSequencialCircularNumpy import *


f1 = Fila()


if f1.estaVazia():
    print('f1 esta vazia.')

print('Tamanho da fila:', len(f1))

try:
    for i in range(1,8):
        f1.enfileira(i, i*10)
    print('Tamanho da fila:', len(f1))
    print(f1)
    f1.enfileira(1,55)
    print('Tamanho da fila:', len(f1))
    print(f1)

    carga = f1.desenfileira(1)
    print('Carga removida:', carga)
    print(f1)

    conteudo = f1.elemento(3)
    print(f'Elemento(3): {conteudo}')
    posicao = f1.busca(50)
    print(f'Posicao do elemento 50: {posicao}')

    for i in range(15):
        print('removendo:', f1.desenfileira(1))
    print(f1)
except FilaException as ae:
    print(ae)
print(f1)




