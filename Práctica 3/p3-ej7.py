"""
Sin utilizar bucles (for o while) implementa la función:

f(x) = sum[i=1,N-1](100(xi+1 - xi-1^2)^2 + (1-xi)^2)

donde x = (x0,x1,x2,...,xN)
Ayuda: debes usar cortes en arrays de numpy y funciones
y operadores asociados a esa librería
"""
import numpy as np

""" x = list(map(int,input().split()))
suma = 0

for i in range(1,len(x)-1):
    suma += 100*((x[i+1]-(x[i-1]**2))**(2)) + ((1-x[i])**(2))

print(suma) """

entrada = list(map(float,input().split()))
x = np.array(entrada)

entrada.pop(0)
entrada.append(0)
y = np.array(entrada)

entrada.pop(0)
entrada.append(0)
z = np.array(entrada)

ans = 100*((z-(x**2))**(2)) + ((1-y)**(2))

print(ans[0])
