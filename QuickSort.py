import math
import random

def quicksort(arr, inicio, final):
    if final <= inicio: #Base case, where we can no longer divide the array (its length is 1)
        return
    else:
        index = partirArray(arr, inicio, final) #Here we obtain the index in which the current pivot is in, in other words, 
                                                #in this index, the element in it is in its final position, so we only move the left side and right side
        quicksort(arr, inicio, index-1) #left side
        quicksort(arr, index+1, final) #rigth side

def partirArray(arr, inicio, final):
    pivote = arr[final] #pivot is the last element in the current array
    i = inicio-1 
    for j in range(inicio, final):
        if arr[j] <= pivote: #if the element in arr[j] is less than or equal to the pivot, that value should be on the most left side, so we swap it with the 
                                # current element in arr[i], which we know is greater than the pivot
            i += 1
            temporal = arr[i]
            arr[i] = arr[j]
            arr[j] = temporal #Swapping thing 
    
    #At the "last iteration", we swap the pivot and arr[i+1], we know arr[i+1] is greater than the pivot so at the end it should end up on the right side, thats
    #what we're doing, eventually, the right side will be called in a recursive function and sort again
    temporal = arr[i+1] 
    arr[i+1] = arr[final]
    arr[final] = temporal
    
    #We return the index in which the pivot ends up, its final position
    return i+1 

array = [math.floor(random.random()*100) for _ in range(10)]
quicksort(array, 0, len(array)-1)

print(array)

    
    
    
    
