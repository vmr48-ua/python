"""
Diseña un programa que lea una lista de números enteros separados 
por espacios en blanco de un archivo, cuyo nombre se pasará por 
línea de comandos, los transforme en un array de enteros de numpy
e imprima por pantalla:

    a)  La suma de todos los números leídos.
    b)  El mínimo de todos ellos.
    c)  El resultado de sumar el cuadrado de todos ellos.
    
Debes utilizar funciones de numpy para realizar los cálculos.

Ejemplo:
stdin=1 2 3 1 4
stdout=11
1
31
"""
from sys import argv
import numpy as np

fail = False
sol = []
if len(argv) == 2:
    try:
        original = open(argv[1],'r')
        for linea in original:
            sol = list(map(int,linea.split()))
        a = np.array(sol,dtype = 'float')
        original.close()
    except IOError:
        print('Error: no se puede abrir el archivo',argv[1])
else:
    print('Uso: python3',argv[0],'archivo')
    fail = True

if not(fail):
    print(int(np.sum(a)))
    print(int(np.amin(a)))
    print(int(np.sum(a**2)))