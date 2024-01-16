class Solution:
    def isValid(self, s: str) -> bool:
        parentesis = cuadrado = corchete = 0
        for i in s:
            if i == '(':
                parentesis += 1
            elif i == '[':
                cuadrado += 1

            elif i == '{':
                corchete += 1

            elif i == ')':
                parentesis -= 1
            elif i == ']':
                cuadrado -= 1
            elif i == '}':
                corchete -=1
        if parentesis == 0 and cuadrado == 0 and corchete == 0:
            return True
        else:
            return False
    
string = "{}{}()"
prueba = Solution()
print(prueba.isValid(string))

