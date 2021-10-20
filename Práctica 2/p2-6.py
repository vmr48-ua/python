def leerMatriz(n):
    m = []
    for i in range(n):
        m.append(leerVector())
    return m

def leerVector():
    return list(map(int,input().split()))

def imprimirMatriz(A):
    for i in range(len(A)):
        for j in range(len(A[0])-1):
            print(A[i][j],end=' ')
        print(A[i][len(A[0])-1])
    return 0

def transpuesta(A):
    B = []
    m = len(A)
    n = len(A[0])
    for i in range(n):
        v = []
        for j in range(m):
            v.append(A[j][i])
        B.append(v)
    return B

def mult(A,B):
    n = len(A)    #filas
    m = len(B[0]) #columnas
    C = []

    for a in range(n):  #crea una matriz resultado c de nxm dimensiones llena de 0
        v = []
        for b in range(m):
            v.append(0)
        C.append(v)

    for i in range(n):
        for j in range(m):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C

n = int(input())
m = int(input())
A = leerMatriz(n)
T = transpuesta(A)
imprimirMatriz(T)
print()
imprimirMatriz(mult(A,T))