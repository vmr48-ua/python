def fila(n,lim): # Calcula cada fila de la matriz
    v = []          # inicializo 
    a = 1           # a es el número que va aumentando por debajo de la diagonal
    cont = 1       # cuantas veces he hecho el bucle, para llevar la cuenta de cada fila
    
    for _ in range(lim+1):      # hasta el límite (columna)
        for _ in range(len(v)): # Vacío v
            v.pop()
        for i in range(count):  # Añado a v el 'a' correspondiente
            v.append(a)
            a+=1                # actualizo a
        for _ in range(cont,n): # relleno el resto de v con 0
            v.append(0)
        cont += 1
    return v     

def triangular(n):  # Calcula la matriz triangular de tamaño nxn
    A = []              # inicializo 
    for i in range(n):  # Append de cada fila en el rango n ( la matriz es cuadrada )
        A.append(fila(n,i))
    return A

def imprimirMatriz(M): # Imprime la matriz por pantalla separada por espacios
    for i in range(len(M)):             # filas
        for j in range(len(M[0])-1):    # imprime la columna de la fila i, menos la última posición
            print(M[i][j],end=' ')      # separados por espacios
        print(M[i][len(M)-1])           # imprime la última columna de cada fila y un salto de línea
        

imprimirMatriz(triangular(int(input())))
