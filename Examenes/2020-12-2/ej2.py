def leer():
    lista = list(map(int,input().split()))
    return lista

def anyadirNElementos(v,w,n):
    if (len(w) > 0):
        if n > len(w)-1:
            n = len(w)-1
        for i in range(n):
            v.append(w[i])
        for i in range(n):
            w.pop(0)

v = leer()
w = leer()
n = int(input())

anyadirNElementos(v,w,n)

print(v)
print(w)