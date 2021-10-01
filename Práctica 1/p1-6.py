num = int(input('Introduce la cantidad de números a leer: '))
aux = 0
suma = 0

for i in range(num,0,-1):
    aux += 1
    elemento = int(input('Introduce el número {}: '.format(aux)))
    suma = suma + (elemento**2)

resultado = suma / num
print(resultado)