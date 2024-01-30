import math
import random

def quicksort(arr, inicio, final):
    if final <= inicio:
        return
    else:
        index = partirArray(arr, inicio, final)
        quicksort(arr, inicio, index-1)
        quicksort(arr, index+1, final)

def partirArray(arr, inicio, final):
    pivote = arr[final]
    i = inicio-1
    for j in range(inicio, final):
        if arr[j] <= pivote:
            i += 1
            temporal = arr[i]
            arr[i] = arr[j]
            arr[j] = temporal
    
    return i+1

array = [math.floor(random.random()*100) for _ in range(10)]
print(quicksort(array, 0, len(array)))

    
    
    
    