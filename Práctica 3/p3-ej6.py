"""
Diseña un programa que lea un vector de componentes enteras,
un entero p que llamaremos posición, un entero l que llamaremos
longitud y construya un nuevo vector con el trozo del vector 
original que empieza en la posición p y tiene longitud l. Antes,
el programa debe comprobar 0≤p≤n−1, (n es el tamaño del vector
introducido), y que p+l≤n. Si no se cumple alguna de estas dos
condiciones el programa debe escribir “error”. La entrada y la
salida se leerán/escribirán en sendos archivos cuyos nombres 
serán pasados por línea de comandos. Se puede suponer que ambos
archivos estarán siempre disponibles y, en el caso del de entrada,
en formato correcto.

Ejemplo:
stdin=5 7 8 2 4 3 1
7
1
stdout=error

stdin=5 7 8 2 4 3 1
6
2
stdout=error

stdin=5 7 8 2 4 3 1
2
3
stdout=8 2 4

stdin=5 7 8 2 4 3 1
0
6
stdout=5 7 8 2 4 3
"""
from sys import argv

def leer():             # Lee un vector números separados por espacios del teclado 
    return list(map(int,input().split()))

def check(v,p,l):       # Comprueba si el vector cumple las condiciones propuestas
    err = True          # Asumo que sí
    if (p < 0 or p > (len(v)-1)) or (p+l > len(v)):
        err = False     # Si no es válido lo cambio a False
    return err

def escribir(v):        # Imprime las componentes de un vector por pantalla separadas por espacios
    j = -1                                  # Empieza en -1 para que -1+1 = 0 en el último print en el caso de que el vector tenga un solo elemento
    for i in range(len(v)-1):               # Imprime todos los elementos del vector menos el último en una sola línea
        file.write(str(v[i])+' '.rstrip('\n'))
        j = i                               # Me guardo el valor de la última i
    file.write(str(v[j+1]))                           # Imprime el último elemento y un salto de línea    

def create(v,p,l):      # Crea el vector nuevo, w
    if(check(v,p,l)):           # Comprueba si v es válido
        w = []                  # inicializo
        for i in range(p,p+l):  # len(w) = l = l+p-p
            w.append(v[i])      # añado el valor de v[i] al final de w
        escribir(w)             # imprime w
    else:
        file.write('error')

contenido = []
fail = False

if len(argv) == 3:
    try:
        archivo = open(argv[1],'r')
        for fila in archivo:
            contenido.append(fila)
        archivo.close()
    except IOError:
        print('Error: no se puede abrir el archivo',argv[1])
else:
    print('Uso: python3',argv[0],'archivo entrada','archivo salida')
    fail = True

if not(fail):
    file = open(argv[2],'w')
    create(list(map(int,contenido[0].split())),int(contenido[1]),int(contenido[2]))
    file.close()