from typing import List # utilizar typehint para List[tipo]


#BUBBLE SORT
#version1
def bubble_sort(array):
    for i in range(len(array)-1,0,-1):
        troca = False
        for j in range(0,i):
            if (array[j] > array[j+1] ):
                array[j],array[j+1] = array[j+1],array[j] # Efetua a troca
                troca = True
        if( not troca ): # não houve troca
            return
        
#version2
def bubble_sort_recursivo(array):
    executaBolha(array,len(array))

def executaBolha(array,size):
    troca = False
    for j in range(size-1):
        if (array[j] > array[j+1] ):
            temp = array[j]
            array[j] = array[j+1] # Efetua a troca
            array[j+1] = temp
            troca = True
    if (troca):      # Houve troca
        executaBolha(array,size-1)



#SELECTION SORT
# version1
def selection_sort(array):
    for i in range(len(array)-1):
        min = i
        for j in range(i+1, len(array)):
            if(array[j] < array[min]):
                min = j
        array[min], array[i] = array[i], array[min] # troca

# version2
def selectionSort(array):
    selectionSortRec(array,0,len(array))

def selectionSortRec(array,inicio,size):
    min = inicio
    for j in range(inicio+1, size):
        if(array[j] < array[min]):
            min = j

    array[min], array[inicio] = array[inicio], array[min]
    if inicio+1 < size:
        selectionSortRec(array, inicio+1, size)


#INSERTION SORT
# version1
def insertion_sort(array):
    for i in range(1, len(array)):
        # chave do subarray desordenado
        key = array[i]

        j = i-1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key

# version2
def insertionSort(arr):
    insertion_Sort_Recursive(arr, len(arr))

def insertion_Sort_Recursive(arr,n):
    if n<=1:
        return
    insertion_Sort_Recursive(arr, n-1)
    last = arr[n-1]
    j = n-2
    while (j>=0 and arr[j]>last):
        arr[j+1] = arr[j]
        j = j-1
    arr[j+1]=last
    print('last:', last,'array:',arr)


#  MERGE SORT
def merge_sort(array:List[int]):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        # Chamada recursiva para cada metade do array
        merge_sort(right)
        merge_sort(left)

        # Aqui é iniciado o processo de merge dos vetores

        # iteradores para percurso das duas metades
        i = 0 # iterador para a metade esquerda
        j = 0 # iterador para a metade direita

        # iterador para o array principal
        k = 0

        # Comparando os elementos da metade da esquerda e da direita
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # O valor da metade esquerda é ordenado
              array[k] = left[i]
              # Avança o iterador da metade esquerda
              i += 1
            else:
                # o valor da metade direita é ordenado
                array[k] = right[j]
                # Avança o iterador da metade direita
                j += 1
            # Avança para o próximo slot do array principal
            k += 1

        # Os valores remanescentes, da metade esquerda, são copiados
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        # Os valores remanescentes, da metade direita, são copiados
        while j < len(right):
            array[k]=right[j]
            j += 1
            k += 1



# PARTITION - Algoritmo Clássico (Hoare & Lomuto)
def partition(array,low,high):
    pivot = array[low] # pivot

    a = low + 1 # indice que sobe de forma crescente
    b = high # indice que desce de forma decrescente

    while(True):
        while( a <= high  and array[a] <= pivot ): # Deslocando o indice para a direita
            a+=1

        while( array[b] > pivot): # Deslocando o indice do final para a esquerda
            b-=1

        if ( a < b ): # Se o indice "a" for menor que "b", realizamos a troca
            array[a],array[b] = array[b],array[a]
            a+=1
            b-=1

        if( a > b): # se a cruzar com b, sai do laço
            break
    # Ja foi encontrado o lugar do pivo. Agora vamos troca-lo com o elemento
    # que se encontra no indice
    array[low] = array[b]
    array[b] = pivot

    return ( b )

# função recursiva que aciona o particionamento e chamadas recursivas das
# subdivisões do array
def quickSortRun(array,low,high):
    if low < high:
        # pi é o índice de particionamento
        pi = partition(array,low,high)

        # Separadamente, os elementos antes e depois e antes da
        # partição são ordenados
        quickSortRun(array, low, pi-1)
        quickSortRun(array, pi+1, high)

def quick_sort(array):
    quickSortRun(array,0,len(array)-1)

def quick_sort_lc(vetor):
    if len(vetor) <= 1: return vetor
    pivo = vetor[0]
    iguais = [x for x in vetor if x == pivo]
    menores = [x for x in vetor if x < pivo]
    maiores = [x for x in vetor if x > pivo]
    return quick_sort_lc(menores) + iguais + quick_sort_lc(maiores)
