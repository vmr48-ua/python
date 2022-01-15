def compara(cad1, cad2):
    list1,list2,linea,A = [],[],[],[]
    
    #Creo listas con los valores ascii de cada palabra
    for caracter in cad1:
        list1.append(ord(caracter))
    for caracter in cad2:
        list2.append(ord(caracter))

    #Creo una matriz con los números estipulados en función de comparaciones
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] < list2[j]:
                linea.append(-1)
            if list1[i] > list2[j]:
                linea.append(1)
            if list1[i] == list2[j]:
                linea.append(0)
        A.append(linea.copy())
        linea.clear()
    
    #Arreglo la matriz para añadirle las palabras y la imprimo
    imprime(arregla(list1,list2,A))

#Devuelve una matriz A con las palabras añadidas correctamente a cada fila y/o columna
def arregla(l1,l2,A):
    lista1,lista2,dummie = [],[],[]
    
    #Transforma una lista con los valores ascii de las palabras 
    #en una lista con los caracteres ascii
    for caracter in l1:
        lista1.append(chr(caracter))
    for caracter in l2:
        lista2.append(chr(caracter))
    
    #Añado un espacio al principio de la segunda palabra
    lista2 = lista2[::-1]
    lista2.append(' ')
    lista2 = lista2[::-1]

    #Añado la segunda palabra al principio de la matriz
    A = A[::-1]
    A.append(lista2)
    A = A[::-1]

    #Añado cada letra de la primera palabra al principio de cada fila
    for i in range(1,len(A)):
        dummie = A[i]
        dummie = dummie[::-1]
        dummie.append(lista1[i-1])
        dummie = dummie[::-1]
        A[i] = dummie.copy()
        dummie.clear()

    return A

#Imprime una matriz según el formato estipulado
def imprime(A):
    for i in range(len(A)):
        first = True
        for j in range(len(A[0])):
            if first:
                print(str(A[i][j]), end='')
                first = False
            elif A[i][j] != -1:
                print('  ' + str(A[i][j]), end='')
            else:
                print(' ' + str(A[i][j]), end='')
        print()
    
compara(input('Introduce la cadena 1: '),input('Introduce la cadena 2: '))
