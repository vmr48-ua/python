"""
Diseña un programa que lea un entero n, y una matriz cuadrada de n×n 
componentes enteras, y a continuación calcule lo siguiente:

    a)  La media de los elementos de la diagonal de la matriz

    b)  El máximo de los elementos de la diagonal opuesta

    c)  Considerando las dos filas centrales como vectores, la distancia
        euclídea entre ambos vectores. Si n es par, las filas centrales 
        son fáciles de calcular; si n es impar, sólo hay una fila central,
        luego se tomará la fila anterior como el otro vector.

Por ejemplo, si M fuese:

        1  2  3  4
        5  6  7  8
        9  10 11 12
        13 14 15 16

habría que calcular la media de 1,6,11 y 16, el máximo de 4,7,10 y 13,
y la distancia entre (5,6,7,8) y (9,10,11,12)

Debes hacer una función para leer la matriz, otra para calcular la media
de la diagonal, otra para el máximo de la otra diagonal y finalmente otra
función que calcule la distancia euclídea entre dos vectores.

Ejemplo:
stdin=4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
stdout=8.5
13
8

stdin=3
1 4 7
2 5 8
3 6 9
stdout=5
7
1.73205
"""

def leer():             # Lee un vector números separados por espacios del teclado 
    return list(map(int,input().split()))

def leerMatriz(n):      # Lee una matriz de números separados por espacios y saltos de línea
    m = []                  # inicializo
    for _ in range(n):      # de 0 a n-1
        m.append(leer())    # añado a m un vector
    return m

def mediaDiagonal(m,n): # Devuelve la media de la diagonal de una matriz de tamaño n
    suma = 0                # inicializo
    for i in range(n):      # sumo todos los elementos de la diagonal en suma
        suma += m[i][i]     
    return (suma/n)         # divido la suma entre el número de elementos, 
                            # que será el tamaño n ya que las matrices serán cuadradas nxn

def maximus(v):         # Devuelve el máximo de un vector, hace lo mismo que max() pero no se puede usar en la práctica
    if len(v) != 0:             # si el vector no está vacío
        m = v[0]                # asumo que el máximo es el primer valor
    for i in range (1,len(v)):  # desde el segundo valor compruebo si hay alguno mayor que la suposición
        if m < v[i]:            # si lo hay actualizo
            m = v[i]
    return m                    

def maximoDiagInv(m,n): # Devuelve el valor máximo de la diagonal inversa de una matriz de tamaño n
    v = []                      # inicializo
    j = 0                       # voy de abajo hacia arriba
    for i in range(n-1,-1,-1):  # desde n-1 porque los vectores empiezan en 0, hasta -1 porque el bucle acabará en el anterior a -1 (0)
        v.append(m[i][j])       # añade el término a v
        j += 1                  # actualizo la j
    return maximus(v)           # devuelve el máximo del vector v, que es la diagonal inversa

def distanciaEuclidea(v,w): # Devuelve la distancia euclídea entre dos vectores
    suma = 0                    # inicializo
    for i in range(len(v)):     # len de v pero podría ser len de w porque len(v) = len (w)
        suma += (w[i]-v[i])**2  # guardo el sumatorio
    return suma**(0.5)          # devuelvo la raíz cuadrada del sumatorio

def imprimir(m,n):      # Imprime la mediaDiagonal, el máxDiagInv y la distEuclidea de los vectores centrales de una matriz m nxn
    media = mediaDiagonal(m, n)
    if media - int(media) == 0:         # Compruebo si es un float con .0 al final, si es así, imprimo el número suelto
        media = int(media)
    print(media)

    maximo = maximoDiagInv(m, n)
    if maximo - int(maximo) == 0:       # Compruebo si es un float con .0 al final, si es así, imprimo el número suelto
        maximo = int(maximo)
    print(maximo)

    distancia = round(distanciaEuclidea(m[int((n/2))-1],m[int(n/2)]),5) # m[int(n/2)] será el vector central si n es impar, y el vector central con índice mayor si n es par
    if distancia - int(distancia) == 0: # Compruebo si es un float con .0 al final, si es así, imprimo el número suelto
        distancia = int(distancia)
    print(distancia)

n = int(input())
imprimir(leerMatriz(n),n)