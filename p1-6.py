num = int(input('Introduce la cantidad de números a leer: '))
aux = 0
suma = 0
array = []

for i in range(0,num):
    aux += 1
    elemento = int(input('Introduce el número {}: '.format(aux)))
    array.append(elemento)

for elemento in array:
    suma = suma + (elemento**2)

resultado = suma / num
print(resultado)