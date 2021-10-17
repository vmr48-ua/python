num = int(input())
i = 1

while num != 0: 
    # Asignaciones
    ends_in_seven = 0
    j = i-1
    primo = 1

    # Detectar si el número i es primo
    for j in range((j**0.5)+1,1,-1):
        if i % j == 0:
            primo = 0
            break

    # Detectar si el número primo acaba en 7
    if primo and ((i-7) % 10 == 0):
        ends_in_seven = 1

    # Imprime
    if primo and num != 1 and i != 1 and not ends_in_seven:
        print('{}, '.format(i), end='')
        num -= 1
    elif primo and num == 1 and not ends_in_seven:
        print('{}.'.format(i))
        num -= 1

    i += 1      