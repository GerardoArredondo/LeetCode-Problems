def solution(inputString):
    izq = 0
    der = inputString.__len__() -1
    flag = True
    while izq < der and flag == True:
        if inputString[izq] == inputString[der]:
            izq += 1
            der -= 1
        else:
            return False
    return True


    

str = "aaabaaa"
print(solution(str))

    

