def imprimirMatriz(A):
    for i in range(len(A)):
        for j in range(len(A[0])-1):
            print(A[i][j],end=' ')
        print(A[i][len(A[0])-1])
    return 0

def matrizVacia(M,n):
    for i in range(n):
        M.append([])
        for _ in range(n):
            M[i].append(0)
    return M

def triangular(M,n):
    M = matrizVacia(M,n)
    k = 1
    for i in range(len(M)):
        for j in range(len(M)):
            if i <= j:
                M[i][j] = k
                k += 1            
    return M

#INTRODUCIR DIMENSIÓN DE LA MATRIZ
n = int(input(''))
M = []
M = triangular(M,n)
imprimirMatriz(M)