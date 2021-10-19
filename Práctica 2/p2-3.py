import sys

def leer():
    return list(map(int,input().split()))

def imprimir(v):
    j = -1                                  # Empieza en -1 para que -1+1 = 0 en el último print en el caso de que el vector tenga un solo elemento
    for i in range(len(v)-1):               # Imprime todos los elementos del vector menos el último en una sola línea
        print('{} '.format(v[i]),end = '')
        j = i
    print(v[j+1])                           # Imprime el último elemento y un salto de línea
    return 0

# Funciona pero no sigue las directrices del enunciado al 100%
""" def desplazar(v,num):
    pos = -1                      # Debug value, siempre se sustituirá
    for i in range(0,len(v)):     # Guarda la posición de num en pos
        if v[i] == num:
            pos = i
    for j in range(pos,len(v)-1): # Copia el vector en la posición anterior a partir de pos
        v[j] = v[j+1]
    v.pop()                       # Borra el último elemento del vector
    return v

u = leer()  # Vector leído
v = list()  # Voy guardando en v los valores de u ordenados

for i in range(len(u)): 
    v.append(min(u))         # El mínimo valor de u se añade a v
    u = desplazar(u,min(u))  # en u se elimina el mínimo valor
imprimir(v) """

def desplazar(v):
    w = v
    for i in range(len(v)):
        for j in range(0,len(v)):  # Guarda la posición del min en pos
            if v[j] == min(w):
                vpos = j
        first = v[i]
        print('i:',i,'first:',first,'min:',v[vpos])
        v[i] = v[vpos]
        v[vpos] = first
        print('v: ',end='')
        imprimir(v)

        print('w: ',end='')
        imprimir(w)
        for l in range(0,len(w)):
            if w[l] == min(w):
                w.pop(l)
                break                       # Borra el último elemento del vector
    return v

imprimir(desplazar(leer()))
