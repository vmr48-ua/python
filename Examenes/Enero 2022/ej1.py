from sys import argv


##############
"""
Este ejercicio no está bien al 100% porque calera dijo en el examen
que en el fichero podrían haber intros al final de la matriz, cosa que 
no escuché y el programa no hace. Debe no fallar aunque haya un cambio
de línea (o múltiples) al final de la matriz.
"""
##############


#Crea una matriz dispersa dada una en formato python
def aDispersa(M):
    A,fila = [],[]
    
    #Creo la primera fila en función del tamaño de M
    fila.append(0)
    fila.append(len(M))
    fila.append(len(M[0]))
    A.append(fila.copy())
    fila.clear()
    
    #Recorre toda la matriz M
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] != 0: #si el elemento no es nulo añade a la dispersa
                fila.append(i+1)
                fila.append(j+1)
                fila.append(M[i][j])
                A.append(fila.copy())
                fila.clear()
    return A

#Crea una matriz en formato python dada una dispersa
def deDispersa(M):
    A,fila = [],[]
    
    #Creo una matriz llena de 0 con dimensiones según la primera fila de la dispersa
    for i in range(M[0][2]):
            fila.append(0)
    for i in range(M[0][1]):
        A.append(fila.copy())

    #Actualizo los valores que son no nulos según la dispersa
    for i in range(1,len(M)):
        A[M[i][0]-1] [M[i][1]-1] = M[i][2]
        
    return A

#Arregla la entrada de un fichero para transformarla en una matriz formato python
def leer(m):
    matrix,linea = [],[]
    for cadena in m:
        cadena = cadena.split()
        i = 0
        for x in cadena:
            linea.append(int(cadena[i]))
            i += 1
        matrix.append(linea.copy())
        linea.clear()
    return matrix

#Escribe una matriz dada en un archivo dado según el formato estipulado
def escribirEn(m,archivo):
    for i in range(len(m)-1):
        archivo.write(str(m[i][0]) + ' ' + str(m[i][1]) + ' ' + str(m[i][2]) + '\n')
    archivo.write(str(m[len(m)-1][0])+' '+str(m[len(m)-1][1])+' '+str(m[len(m)-1][2]))
    
if len(argv) == 3: # Comprueba que todos los argumentos han sido introducidos
    try: # Comprueba que los archivos se pueden abrir 
        entrada = open(argv[1],"r")
        salida = open(argv[2],"w")
                
        escribirEn(aDispersa(leer(entrada.read().splitlines())),salida)
        
        entrada.close()
        salida.close()
    except(IOError):
        print('Problema con el archivo de entrada o salida')
else:
    print('Uso incorrecto, falta archivo de entrada y/o salida')
