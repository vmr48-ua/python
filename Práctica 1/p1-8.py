num = int(input())
# i = Contador para líneas
# j Contador para columnas

# Triángulo superior
for j in range (num,0,-1):
    i = j
    aux = num # Auxiliar para los espacios
    while aux-j > 0 and aux > 0:
        print(' ', end='')
        aux -= 1 
    for i in range (i,0,-1):
        print(i, end='')
    i += 1 # Me quita el 0 y el 1 repetidos
    while i < (j+1): # llega hasta num
        print(i, end='')
        i += 1
    print('') # cambio de línea entre líneas       

aux = num
# Triángulo inferior
for k in range (2,num+1):
    for l in range (k,num):
        print(' ', end='')
    l = k
    while (aux-l) < aux:
        print(l, end='')
        l -= 1
    for l in range (2,k+1):
        print(l, end='')
    print('')