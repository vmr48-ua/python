def montaña(nlist):
    es = False
    if (len(nlist) == 5) and nlist[0] < nlist[1] and nlist[2] > nlist[1] and nlist[2] > nlist[3] and nlist[3] > nlist[4]:
        es = True
    return es
        
def capicua(nlist):
    es = False
    if (len(nlist) == 5):
        if nlist[0] == nlist[4] and nlist[1] == nlist[3]:
            es = True
    return es

def divPropios(n):
    a = []
    for i in range (1,int(n/2)+1):
        if n%i == 0:
            a.append(i)
    return a

def suma(a):
    s = 0
    for i in range(len(a)):
        s += a[i]
    return s

def check(n,a,nlist):
    if not(montaña(nlist)):
        return False
    if not(capicua(nlist)):
        return False
    if not(suma(divPropios(n)) == a):
        return False
    return True

nohay = True
j = suma(divPropios(1184))
for i in range (999,100000):
    nlist = [int(x) for x in str(i)]
    if check(i,j,nlist):
        print(i)
        nohay = False

if nohay:
    print('No hay')
