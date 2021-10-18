def leer():
    lista = list(map(int,input().split()))
    return lista

def media(lista):
    suma = 0
    tamaño = 1
    if len(lista) > 0:
        tamaño = len(lista)
    for num in lista:
        suma += num
    return (suma/tamaño)

def desviación(lista):
    suma = 0
    med = media(lista)
    div = 1
    for i in range (len(lista)):
        suma += (lista[i] - med)**2
    if len(lista)-1 > 0:
        div = (len(lista)-1)
    return (suma/div)**0.5

def moda(lista):
    mod = 0
    if len(lista) > 0:
        mod = max(lista, key = lista.count)
    return mod

entrada = leer()
print(round(media(entrada),5))
print(round(desviación(entrada),5))
print(round(moda(entrada),5))