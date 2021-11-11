def leerVector():
    return list(map(int,input().split()))

def check(v,p,l):
    err = 0
    if (p < 0 or p > (len(v)-1)) or (p+l > len(v)):
        err = 1
    return err

def create(v,p,l):
    if(check(v,p,l) == 0):
        w = []
        for i in range(p,p+l):
            w.append(v[i])
        escribir(w)
    else:
        print('error')
    return 0

def escribir(v):
    j = -1                                  # Empieza en -1 para que -1+1 = 0 en el último print en el caso de que el vector tenga un solo elemento
    for i in range(len(v)-1):               # Imprime todos los elementos del vector menos el último en una sola línea
        print('{} '.format(v[i]),end = '')
        j = i
    print(v[j+1])                           # Imprime el último elemento y un salto de línea
    return 0

v = leerVector()
p = int(input())
l = int(input())
create(v,p,l)
