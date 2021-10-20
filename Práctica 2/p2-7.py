def leerVector():
    return list(map(float,input().split()))

def leerMatriz(n):
    m = []
    for i in range(n):
        m.append(leerVector())
    return m

def distanciaEuclidea(v,w):
    suma = 0
    for i in range(len(v)):
        suma += (w[i]-v[i])**2
    return suma**(0.5)

def vectorMin(v,A):
    w = A[0]
    for i in range(len(A)):
        if distanciaEuclidea(v,A[i]) < distanciaEuclidea(v, w):
            w = A[i]
    return w

def escribir(v):
    j = -1                                  # Empieza en -1 para que -1+1 = 0 en el último print en el caso de que el vector tenga un solo elemento
    for i in range(len(v)-1):               # Imprime todos los elementos del vector menos el último en una sola línea
        print('{} '.format(v[i]),end = '')
        j = i
    print(v[j+1])                           # Imprime el último elemento y un salto de línea
    return 0

n = int(input())
m = int(input())
escribir(vectorMin(leerVector(),leerMatriz(m)))