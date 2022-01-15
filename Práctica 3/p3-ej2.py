"""
Escribe un programa que abra un archivo de texto cuyo nombre
será pasado por línea de comandos e imprima por pantalla el
número de líneas, el número de palabras y el número de caracteres
(incluidos espacios y cambios de línea) de dicho archivo en el formato:

lineas: <número de líneas>
palabras: <número de palabras>
caracteres: <número de caracteres>
"""

from sys import argv

lineas,palabras,caracteres,fail = 0,0,1,False

if len(argv) == 2:
    try:
        archivo = open(argv[1],'r')
        for fila in archivo:
            palabras += len(fila.split())
            caracteres += len(str(fila))
            lineas += 1
        archivo.close()
    except IOError:
        print('Error: no se puede abrir el archivo',argv[1])
else:
    print('Uso: python3',argv[0],'archivo')
    fail = True

if not(fail):
    print('lineas:',lineas)
    print('palabras:',palabras)
    print('caracteres:',caracteres)

# Solución que utiliza la salida del comando wc

""" from sys import argv
from subprocess import check_output
array = []

if len(argv) == 2:
    try:
        archivo = argv[1]
        sol = check_output("wc "+archivo, shell=True)
        sol = list(sol.decode())
        for _ in range(len(archivo)+2):
            sol.pop()
        for char in sol:
            if char == ' ':
                sol.pop(0)
            if char != ' ':
                break
        print(sol)
        while(len(sol) != 0):
            i = 0
            for char in sol:
                i += 1
                if i > 1 and char == ' ':
                    break
                if char != ' ':
                    array.append(char)
            for _ in range(i):
                sol.pop(0)
            print(int(''.join(map(str,array))))
            array.clear()

    except IOError:
        print('Error: no se puede abrir el archivo',argv[1])
else:
    print('Uso: python3',argv[0],'archivo') """