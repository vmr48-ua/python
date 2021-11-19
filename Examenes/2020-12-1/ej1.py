def pares(n):
    a = []
    for i in range (n+1):
        if i%2 == 0:
            a.append(i)
    return a

def impares(n):
    a = []
    for i in range (n+1):
        if (i+1)%2 == 0:
            a.append(i)
    return a[::-1]

def intercalar(even,odd):
    a = []
    for i in range (0,max(len(odd),len(even))):
        if i < len(even):
            a.append(even[i])
        if i < len(odd):
            a.append(odd[i])
    return a

n = int(input())

print(intercalar(pares(n),impares(n)))