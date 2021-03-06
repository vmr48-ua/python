"""
Diseña un programa que lea una lista de números enteros 
separados por espacios en blanco y calcule:

a) La media de los números leídos
b) La desviación típica muestral
c) La moda (el valor que más veces aparece). Si hay dos 
   o más que se repiten el mismo número de veces tu función
   debe devolver el primero que aparezca en el vector
   
   !! '1 7 6 3 3 6 1 7' !! stdout=1 or stdout=3

Debes utilizar una función para leer el vector de números, 
y otra por cada apartado. Se deben imprimir los valores 
redondeados a 5 cifras decimales si fuera necesario.

Ejemplo:
stdin=1 2 3 2 4
stdout=2.4
1.14018
2
"""

def leer():             # Lee un vector números separados por espacios del teclado 
    return list(map(int,input().split()))

def media(v):           # Calcula la media de las componentes de un vector
    suma = 0                   # inicialización
    tamaño = 1                 # el mínimo tamaño tiene que ser 1 y no 0, ver return

    if len(v) > 0:             # si el vector no está vacío, tamaño es el tamaño del vector
        tamaño = len(v)
    for num in v:
        suma += num            # suma todas las componentes

    return (suma/tamaño)       # si tamaño es 0 dividiría entre 0 

def desviación(v):      # Calcula la desviación típica muestral de un vector
    suma = 0                        # inicialización
    med = media(v)                  # cálculo de la media
    div = 1                         # empieza por 1 para no dividir por 0
    for i in range (len(v)):    
        suma += (v[i] - med)**2     # cálculo del numerador
    if len(v)-1 > 0:
        div = (len(v)-1)            # cálculo del denominador
    return (suma/div)**0.5          # división y raíz

def moda(v):            # Calcula la moda típica muestral de un vector
    m = v[0]                        # Asumo que la moda es el primer valor
    count = v.count(m)              # Guardo cuantas veces se repite la moda
    for i in range(1,len(v)):       # Empieza en 1 para saltarse el que ya he supuesto ([0])
        if v.count(v[i]) > count:   # Si el valor nuevo se repite más veces que el anterior
            m = v[i]                # Actualizo a el nuevo valor de la moda
            count = v.count(v[i])   # Actualizo
    return m

entrada = leer()
print(round(media(entrada),5))
print(round(desviación(entrada),5))
print(round(moda(entrada),5))