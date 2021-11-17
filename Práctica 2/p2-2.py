"""
Escribe una función que reciba dos vectores v y w de tamaño n
(la función tendrá, por tanto, tres argumentos), y devuelva un 
entero que indique si un vector es mayor, menor o igual que el otro. 
Se considera que un vector v es mayor que otro w cuando la componente
i-ésima de v es mayor que la misma componente de w y todas las 
componentes anteriores a i son iguales en ambos vectores.

Los siguientes ejemplos definen (informalmente) esta relación de
orden entre vectores.

v = (1,2,3,4,5) y w = (1,2,3,4,4)           1(v es mayor que w)
v = (1,2,3,4,5) y w = (1,2,3,5,4)          -1(v es menor que w)
v = (1,1,3,4,5) y w = (1,1,3,4,5)           0(v y w son iguales)

Una vez hayas diseñado la función, haz un programa que lea un número
entero n y dos vectores de n componentes cada uno (utilizando una
función que lea un vector) y los compare utilizando la función, 
escribiendo el resultado por pantalla.

Ejemplo:
stdin=5
1 2 3 4 5
1 2 3 5 4
stdout=-1
"""

def leer():             # Lee un vector números separados por espacios del teclado 
    v = list(map(int,input().split()))
    return v

def compare(n,v,w):     # Compara los vectores de tamaño n y devuelve 1 0 ó -1 en función de cuál es mayor
    equal = 0                   # inicialización
    ans = 2                     # inicializo a 2 por debug
    sameLen = 1                 # sameLen = false
    if len(v) == len(w) == n:   # si tienen el mismo tamaño y coinciden con n sameLen = true
        sameLen = 0
    if sameLen == 0:            # si son iguales en tamaño
        for i in range(len(v)): # compara cada componente i de cada vector
            if v[i] > w[i]:
                ans = 1         # si v es mayor devuelve 1 y acaba
                equal = 1
                break
            elif v[i] < w[i]:
                ans = -1        # si w es mayor devuelve -1 y acaba
                equal = 1
                break
        if equal == 0:          # si ninguno de los dos es mayor es que son iguales
            ans = 0
    return ans

n = int(input())

output = compare(n,leer(),leer())
if output != 2:         # Imprime solo si la comparación tiene sentido (debug línea 34)
    print(output)