import math
import random

def bubbleSort(array):
    longitud  = array.__len__()
    for i in range(longitud-1):
        for j in range(0, longitud-1-i):
            if array[j] > array[j+1]:
                (array[j], array[j+1]) = (array[j+1], array[j])
    
    return array

array = [math.floor(random.random()*100) for _ in range(10)]
print(bubbleSort(array))