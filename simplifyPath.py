class Solution:
    def simplifyPath(self, path: str) -> str:
        res = "/" #El path de respuesta siempre empezará con esto
        carpetas = path.split('/') #Obtenemos las carpetas haciendo splits en todo el string, carpetas serán las que están en medio de /
        for i in carpetas: #Iteramos sobre la lista de carpetas
            if i == '': #Cadena vacía (inicio y final)
                pass
            elif i == '.': #Nos quedamos en la misma carpeta
                pass
            elif i == '..': #Regresamos una carpeta hacia arriba
                res = res[:-1] #Quitamos el primer /, este es donde estaba "/.."
                char = '1'
                i = len(res)-1
                aux = len(res)-1
                
                while char != '/': #Mientras que no encontremos otro / iteraremos de derecha a izquierda para obtener la carpeta completa, dicha carpeta será en la cual subimos un nivel
                    char = res[i]
                    i -= 1

                aRestar = aux -i #Obtenemos la cantidad de caracteres que fue la carpeta
                res = res[:-aRestar+1] #Y restamos esa cantidad al string de respuesta

            else: #Llegamos aquí si en la iteración estamos en una carpeta (i.e. /Downloads)
                res += i #Metemos la carpeta al path
                res += '/' #Agregamos un / para la siguiente carpeta
        res = res[:-1] #Cuando ya no hay carpetas, eliminamos ese último / que metimos en la línea 25
        if res == '': #Si llegamos a root res estará vacío, devolvemos /
            return '/'
        else:
            return res 

            


            


string = "/home/downloads/../udemy/python/../"
prueba  = Solution()
res = prueba.simplifyPath(string)
print(res)