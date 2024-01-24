import random
import math

def InsertionSort(array):
    n = array.__len__()
    for i in range(1, n):
        
        index = array[i]
        j = i -1
        while j >= 0 and array[j] > index:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = index
    return array


array = [math.floor(random.random()*100) for _ in range(10)]
print(InsertionSort(array))


