"""
Diseña un programa que lea un vector de componentes enteras y lo ordene
de menor a mayor utilizando el siguiente método (conocido como método
de intercambio):

a) Buscar dentro del vector el mínimo e intercambiarlo con el valor 
   situado en la primera posición. Por ejemplo, si el vector original
   es v = (4,7,2,1,5), el mínimo es 1, y se intercambiaría con el 4, 
   quedando v = (1,7,2,4,5).

b) Volver al paso anterior avanzando una posición, y buscando el mínimo
   a partir de la posición siguiente a la intercambiada. En el ejemplo,
   habría que buscar el mínimo en (7,2,4,5).

El proceso termina cuando se llega al final del vector (a la última
posición). Una vez ordenado, el programa debe escribir el vector por
pantalla. Debes utilizar funciones para leer, ordenar y escribir el 
vector.

Ejemplo:
stdin=5 7 8 2 4 3 1
stdout=1 2 3 4 5 7 8
"""

def leer():             # Lee un vector números separados por espacios del teclado 
    return list(map(int,input().split()))

def minimo(v):          # Lee un vector y devuelve el mínimo (podría usarse la función min())
    a = v[0]                    # Presupongo que v[0] es el min
    for i in range(1,len(v)):   # Desde el 1 porque el 1 ya está metido
        if v[i] < a:            # Si  hay uno menor me lo guardo
            a = v[i]
    return a                    # devuelvo el minimo

def ordenar(v):         # Ordena un vector de menor a mayor por el método de intercambio
    for i in range(len(v)):         # Bucle para todo el vector
        peq = v[i]                  # Asumo que el más pequeño es el primero
        aux = i                     # Guardo la posición del más pequeño
        for j in range(i,len(v)):   # Busca el más pequeño desde la posición i
            if v[j] < peq:          # si hay uno más pequeño actualiza
                peq = v[j]
                aux = j
        v[aux], v[i] = v[i], v[aux] # intercambia el más pequeño con el antiguo
    return v

def escribir(v):        # Imprime un vector separado por espacios
    for i in v:         
        if i != v[len(v)-1]:    # Todo v menos la última posición       
            print(i,end = ' ')  # Imprime con espacios al final cada posición
    print(v[len(v)-1])          # Imprime la última posición y un cambio de línea

escribir(ordenar(leer()))
# Versiones anteriores de la función "ordenar"
# comentar la función escribir y descomentar para probar
# (son más o menos funcionales pero usan de alguna forma un vector w copia de v)

""" def ordenar(v):
    w = v.copy()
    for i in range(len(v)):
        for j in range(len(v)):     
            if v[j] == minimo(w):
                posiciónMin = j

        primero = v[i]
        v[i] = v[posiciónMin]
        v[posiciónMin] = primero

        for k in range(len(w)):
            if w[k] == minimo(w):
                posiciónW = k
        w.pop(posiciónW)
    return v """

""" def ordenar(v):
    for i in range (len(v)-1):
        w = v[::-1]
        for _ in range(i):
            w.pop()
        for n in range(len(v)):
            if v[n] == minimo(w):
                j = n
                break
        v[i],v[j] = v[j],v[i]
    return v """

""" def ordenar(v):         # Ordena un vector de menor a mayor por el método de intercambio
    for i in range (len(v)-1):          
        j = v.index(minimo(v[i:len(v)]))# j contencrá la posición del mínimo de v a partir de la posición i
        v[i],v[j] = v[j],v[i]           # intercambio el contenido de la posición i con j
    return v """