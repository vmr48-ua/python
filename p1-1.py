
a = input('Introduce un número: ')
b = input('Introduce un número: ')
c = input('Introduce un número: ')

if a > b:
    maxi = a
    mini = b
else:
    maxi = b
    mini = a

if c > maxi:
    maxi = c
elif c < b:
    mini = c

print('El mayor es', maxi)
print('El menor es', mini)
