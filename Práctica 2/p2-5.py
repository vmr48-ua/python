""" def modulo(v):
    suma = 0
    for i in range(0,len(v)):
        suma += v[i]**2
    return suma**(0.5) 
    
    def vectoresCentrales(m,n):
    v = m[int((n/2)-1)]       
    w = m[int(n/2)]
    return v,w"""

def leerMatriz(n):
    m = []
    for i in range(n):
        m.append(leerVector())
    return m

def leerVector():
    return list(map(int,input().split()))

def mediaDiagonal(m,n):
    suma = 0
    for i in range(n):
        suma += m[i][i]
    return (suma/n)

def maximoDiagInv(m,n):
    v = []
    j = 0
    for i in range(n-1,-1,-1):
        v.append(m[i][j])
        j += 1
    return max(v)

def distanciaEuclidea(v,w):
    suma = 0
    for i in range(len(v)):
        suma += (w[i]-v[i])**2
    return suma**(0.5)

def imprimir(m,n):
    media = mediaDiagonal(m, n)
    if media - int(media) == 0:
        media = int(media)
    print(media)

    maximo = maximoDiagInv(m, n)
    if maximo - int(maximo) == 0:
        maximo = int(maximo)
    print(maximo)

    distancia = round(m[int((n/2)-1)],m[int(n/2)],5)
    if distancia - int(distancia) == 0:
        distancia = int(distancia)
    print(distancia)

    return 0

n = int(input())
m = leerMatriz(n)
imprimir(m,n)