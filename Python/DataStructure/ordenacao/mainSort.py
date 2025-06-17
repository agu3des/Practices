from sort import*
import timeit   # computar o tempo de processamento

array = [1,22,67,82,16,4]


#BUBBLE SORT 
print('BUBBLE SORT')
print("array desordenada = ", array)
bubble_sort(array)
print("array ordenada = ", array)
print(timeit.timeit(lambda:bubble_sort(array), number=10))
print()
#BUBBLE SORT RECURSIVO
print('BUBBLE SORT RECURSIVO')
print("array desordenada = ", array)
bubble_sort_recursivo(array)
print("array ordenada = ", array)
print(timeit.timeit(lambda:bubble_sort_recursivo(array), number=10))

print()

#SELECTION SORT 
print('SELECTION SORT')
print("array desordenada = ", array)
bubble_sort_recursivo(array)
print("array ordenada = ", array)
print(timeit.timeit(lambda:selection_sort(array), number=10))

print()

#INSERTION SORT 
print('INSERTION SORT')
print("array desordenada = ", array)
bubble_sort_recursivo(array)
print("array ordenada = ", array)
print(timeit.timeit(lambda:insertion_sort(array), number=10))

print()

# QUICK SORT RECURSIVO - CLÁSSICO
print('QUICK SORT 1')
print("array desordenada = ", array)
quick_sort(array)
print("array ordenada = ", array)
print(timeit.timeit(lambda:insertion_sort(array), number=10))

print()

# QUICK SORT RECURSIVO - LIST COMPREHENSION
print('QUICK SORT 2')
print("array desordenada = ", array)
quick_sort_lc(array)
print("array ordenada = ", array)
print(timeit.timeit(lambda:insertion_sort(array), number=10))

print()

# QUICK SORT
print('QUICK SORT 3')
print("array desordenada = ", array)
quick_sort_iterativo(array)
print("array ordenada = ", array)
print(timeit.timeit(lambda:insertion_sort(array), number=10))

print()

# MERGE SORT
print('MERGE SORT')
print("array desordenada = ", array)
merge_sort(array)
print("array ordenada = ", array)
print(timeit.timeit(lambda:insertion_sort(array), number=10))
