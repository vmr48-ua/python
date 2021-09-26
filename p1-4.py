num = int(input('Introduce un número: '))
suma = 0
counter = 0

# Calculo cuantos divisores primos hay en total y los guardo en counter
for i in range(2, num): # empiezo por 2 porque el 1 no es primo
    if num % i == 0:
        primo = 1
        for j in range(2, i):
            if i % j == 0: # el divisor no es primo
                primo = 0
        if primo == 1:
            counter += 1   # cuento el numero de divisores primos totales

for i in range(2, num): # empiezo por 2 porque el 1 no es primo
    if num % i == 0:    # el número es divisor
        suma = suma + i  
        primo = 1
        for j in range(2, i):
            if i % j == 0: # el divisor no es primo
                primo = 0
        if primo == 1 and counter == 1: # imprime el último divisor primo
            print('{}.'.format(i))
        if primo == 1 and counter > 1:  # imprime todos los divisores primos menos el último
            print('{}, '.format(i), end='')
            counter -= 1
        
if suma == 0:
    print('El número {} es primo'.format(num))       