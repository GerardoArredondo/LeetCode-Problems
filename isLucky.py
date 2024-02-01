#Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

#Given a ticket number n, determine if it's lucky or not.

#Example

    #For n = 1230, the output should be
    #solution(n) = true;
    #For n = 239017, the output should be
    #solution(n) = false

def solution(n):
    n = str(n)
    longitud  = len(n)
    mitades = longitud // 2
    sumatoria = 0
    sum2 = 0
    
    for i in range(mitades):
        sumatoria += int(n[i])
    
    for i in range(mitades, longitud):
        sum2 += int(n[i])
        
    if sumatoria == sum2:
        return True
    else:
        return False
    
        
        

