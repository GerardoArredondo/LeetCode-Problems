#Given two strings, find the number of common characters between them.

#Example

#For s1 = "aabcc" and s2 = "adcaa", the output should be
#solution(s1, s2) = 3.


def solution(s1, s2):
    
    
    return sum(min(s1.count(x), s2.count(x)) for x in set(s1))
    
    
                
        

