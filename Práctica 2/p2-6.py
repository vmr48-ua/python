"""
Escribe un programa que lea dos números enteros n y m, y a continuación lea
una matriz M de n×m valores enteros. Una vez leida la matriz M, debe obtener
la matriz traspuesta T y escribirla, calcular el producto de M por su traspuesta,
y escribir el resultado de dicho producto.

Ejemplo:
stdin=3
4
1 4 7 10
2 5 8 11
3 6 9 12
stdout=1 2 3
4 5 6
7 8 9
10 11 12

166 188 210
188 214 240
210 240 270
"""

def leer():                 # Lee un vector números separados por espacios del teclado 
    return list(map(int,input().split()))

def leerMatriz(n):          # Lee una matriz de números separados por espacios y saltos de línea
    m = []                  # inicializo
    for _ in range(n):      # de 0 a n-1
        m.append(leer())    # añado a m un vector
    return m

def imprimirMatriz(A):      # Imprime una matriz A separada por espacios
    for i in range(len(A)):          # imprime cada fila
        for j in range(len(A[0])-1): # imprime todas las componentes de la fila separadas por espacios menos la última
            print(A[i][j],end=' ')
        print(A[i][len(A[0])-1])     # imprime la última componente de la fila y un salto de línea

def transpuesta(A):         # Devuelve la matriz transpuesta de A
    B = []                      # inicializo
    m = len(A)                  # nº de filas
    n = len(A[0])               # nº de columnas
    for i in range(n):          # leo por columnas
        v = []                  # reseteo
        for j in range(m):      # guardo la columna en v
            v.append(A[j][i])
        B.append(v)             # añado a B la columna v como una fila
    return B

def mult(A,B):              # Devuelve la matriz Multiplicación de A*B
    n = len(A)                      # filas de A
    m = len(B[0])                   # columnas de B
    C = []                          # inicializo

    for _ in range(n):              # crea una matriz resultado C de nxm dimensiones llena de 0
        v = []
        for _ in range(m):
            v.append(0)
        C.append(v)

    for i in range(n):              # filas de A
        for j in range(m):          # col de B
            for k in range(len(B)): # Calcula la posición ij de C
                C[i][j] += A[i][k] * B[k][j]
    return C                        

n = int(input())
m = int(input())
A = leerMatriz(n)
T = transpuesta(A)
imprimirMatriz(T)
print()                     # meto un salto de línea
imprimirMatriz(mult(A,T))