def suma(M,i):
    suma = 0
    for j in range(0,len(M[0])-1):
        for k in range(0,len(M)+1):
            if j <= i and k <= i:
                suma += M[j][k]
    return suma

def sumaSubMatrices(M):
    ans = []
    n = max(len(M[0]),len(M))
    for i in range (0,n):
        ans.append(suma(M,i))
    return ans

def leeFila():
    return [int(x) for x in input().split()]

def leeMatriz(n):
    M = []
    for _ in range(n):
        M.append(leeFila())
    return M

def imprime(a):
    for i in range (len(a)):
        print('i = {}:'.format(i), a[i])

imprime(sumaSubMatrices(leeMatriz(int(input()))))