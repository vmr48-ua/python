i = 1
suma = 0
while True:
    try:
        a = input('Introduce el número {} (s para acabar): '.format(i))
        b = float(a)
        i += 1
        suma += b**2
    except:
        if a == 's':
            break
        print('Número incorrecto')
print(suma/(i-1))