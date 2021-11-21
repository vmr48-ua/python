"""
Diseña un programa que:

    a) Lea dos enteros, n y m
    b) Lea un vector v de n componentes (reales)
    c) Lea m vectores de n componentes cada uno y los guarde en una matriz.
    d) Escriba por pantalla el vector de los m vectores que esté más cercano
       a v, utilizando la distancia euclídea.

Ejemplo:
stdin=3
4
1.1 2.2 3.3
1.05 1.99 3.2
7.08 4.56 3.21
9.21 3.2 6.5
0.96 8.7 2.1
stdout=1.05 1.99 3.2
"""

def leer():                 # Lee un vector números separados por espacios del teclado 
    return list(map(float,input().split()))

def leerMatriz(n):          # Lee una matriz de números separados por espacios y saltos de línea
    m = []                  # inicializo
    for _ in range(n):      # de 0 a n-1
        m.append(leer())    # añado a m un vector
    return m

def distanciaEuclidea(v,w): # Devuelve la distancia euclídea entre dos vectores
    suma = 0                    # inicializo
    for i in range(len(v)):     # len de v pero podría ser len de w porque len(v) = len (w)
        suma += (w[i]-v[i])**2  # guardo el sumatorio
    return suma**(0.5)          # devuelvo la raíz cuadrada del sumatorio

def vectorMin(v,A):         # Devuelve el vector más cercano a v de las filas de la matriz A
    w = A[0]                    # asumo que el más pequeño es el primero
    for i in range(len(A)):     # len de A es m, es decir el número de filas de A
        if distanciaEuclidea(v, A[i]) < distanciaEuclidea(v, w): # comparo
            w = A[i]            # Actualizo si es menor
    return w                    # devuelvo el mínimo

def escribir(v):            # Imprime las componentes de un vector por pantalla separadas por espacios
    j = -1                                  # Empieza en -1 para que -1+1 = 0 en el último print en el caso de que el vector tenga un solo elemento
    for i in range(len(v)-1):               # Imprime todos los elementos del vector menos el último en una sola línea
        print('{} '.format(v[i]),end = '')
        j = i                               # Me guardo el valor de la última i
    print(v[j+1])                           # Imprime el último elemento y un salto de línea  

n = int(input())    
m = int(input())
escribir(vectorMin(leer(),leerMatriz(m)))