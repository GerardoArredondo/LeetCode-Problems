import math
import random

def selectionSort(array):
    longitud = array.__len__()
    index = 0
    for i in range(longitud):
        min = i
        for j in range(i+1, longitud):
            if array[j] < array[min]:
                min = j
        
        (array[i], array[min]) = (array[min], array[i])
    
    return array


array = [math.floor(random.random()*100) for _ in range(10)]
print(selectionSort(array))

        
        
