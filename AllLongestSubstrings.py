#Given an array of strings, return another array containing all of its longest strings.

#Example

#For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
#solution(inputArray) = ["aba", "vcd", "aba"].

def solution(inputArray):
    aux = []
    aux2 = []
    for i in inputArray:
        aux.append(i.__len__())
        
    longest = max(aux)
    
    for i in inputArray:
        if i.__len__() == longest:
            aux2.append(i)
    
    return aux2
    
    
