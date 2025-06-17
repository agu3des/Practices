# QUESTÃO 1
#     def get(self, key:any)->any:
#         slot = self.__hash(key)
#         for i in range(len(self.__table[slot])):
#             if key == self.__table[slot][i].key:
#                 return self.__table[slot][i].value
#         else:
#             raise KeyError(f'key {key} not found')


# QUESTÃO 2
# def insertionSort(arr):
#     insertion_Sort_Recursive(arr, len(arr))

# def insertion_Sort_Recursive(arr,n):
#     if n<=1:
#         return
#     insertion_Sort_Recursive(arr, n-1)
#     last = arr[n-1]
#     j = n-2
#     while (j>=0 and arr[j]>last):
#         arr[j+1] = arr[j]
#         j = j-1
#     arr[j+1]=last
#     print('last:', last,'array:',arr)

# if __name__ == "__main__":    
#     array = [32,23,5,41,35]
#     insertionSort(array)

# last: 23 array: [23, 32, 5, 41, 35]
# last: 5 array: [5, 23, 32, 41, 35]
# last: 41 array: [5, 23, 32, 41, 35]
# last: 35 array: [5, 23, 32, 35, 41]
# Main program to test insertion sort


# QUESTÃO 3
# def quickSort(array):
#     return quickSortRun(array, 0, len(array) - 1)

# def quickSortRun(array, low, high):
#     if low < high:
#         pi = partition(array, low, high)
#         quickSortRun(array, low, pi - 1)
#         quickSortRun(array, pi + 1, high)
#     return array

# def partition(array, low, high):
#     pivot = array[low]  # pivot
#     a = low + 1
#     b = high

#     while True:
#         while a <= b and array[a] <= pivot:
#             a += 1
#         while array[b] >= pivot and b >= a:
#             b -= 1
#         if b < a:
#             break
#         else:
#             array[a], array[b] = array[b], array[a]

#     array[low], array[b] = array[b], array[low] #troca o pivô
#     return b
#a) [10, 28, 17, 34, 55, 20, 65, 88, 92, 72]
#b) [10, 28]
# if __name__ == "__main__":    
#     array = [65,28,17,34,55,72,88,10,92,20]
#     quickSort(array)
