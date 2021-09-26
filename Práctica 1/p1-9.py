num = int(input('Introduce un número: '))
a = 0
b = 1
if num == 1:
    print('0.')
elif num == 2:
    print('0, 1.')
elif num > 0:
    print('0, 1, ', end='')
    while num-2 > 1:
        print('{}, '.format(a+b), end='')
        c = a   # guarda temporalmente el valor de a
        a = b        
        b = c+b
        num -= 1
    print('{}.'.format(a+b))