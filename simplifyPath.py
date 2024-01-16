class Solution:
    def simplifyPath(self, path: str) -> str:
        res = "/"
        carpetas = path.split('/')
        # ['', 'a', '.', 'b', '..', '..', 'c', '.', 'd', 'e', '']
        for i in carpetas:
            if i == '':
                pass
            elif i == '.':
                pass
            elif i == '..':
                res = res[:-1]
                char = '1'
                i = len(res)-1
                aux = len(res)-1
                print("El valor de res es: " + res + "\n.El valor de i es: " + str(i))
                
                while char != '/':
                    char = res[i]
                    i -= 1

                aRestar = aux -i
                res = res[:-aRestar+1]

            else:
                res += i
                res += '/'
        res = res[:-1]
        if res == '':
            return '/'
        else:
            return res

            


            


string = "/home/downloads/../udemy/python/../"
prueba  = Solution()
res = prueba.simplifyPath(string)
print(res)