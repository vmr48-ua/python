def leer():
    return list(map(int,input().split()))

def escribir(v):
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

u = leer()                        # Vector leído
v = list()                        # Voy guardando en v los valores de u ordenados

for i in range(len(u)): 
    v.append(min(u))              # El mínimo valor de u se añade a v
    u = desplazar(u,min(u))       # en u se elimina el mínimo valor
escribir(v) """

def ordenar(v):
    w = v.copy()
    for i in range(len(v)):
        for j in range(len(v)):     
            if v[j] == min(w):
                posiciónMin = j

        primero = v[i]
        v[i] = v[posiciónMin]
        v[posiciónMin] = primero

        for k in range(len(w)):
            if w[k] == min(w):
                posiciónW = k
        w.pop(posiciónW)
    return v

escribir(ordenar(leer()))