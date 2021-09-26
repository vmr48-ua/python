num = input('Introduce un número: ')
num = int(num)
if num > 0:
    suma = 0

    for i in range(1, num):
        if num % i == 0:
            suma = suma + i
    if suma == num:
        print(num, 'es un número perfecto')
    else:
        print(num, 'no es un número perfecto')

else:
    print('El número es menor que 0')