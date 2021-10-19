def leer():
    v = list(map(int,input().split()))
    return v

def compare(n,v,w):
    equal = 0
    ans = 2 # debug vaule
    sameLen = 1
    if len(v) == len(w) == n:
        sameLen = 0
    if sameLen == 0:
        for i in range(len(v)):
            if v[i] > w[i]:
                ans = 1
                equal = 1
                break
            elif v[i] < w[i]:
                ans = -1
                equal = 1
                break
        if equal == 0:
            ans = 0
    return ans

n = int(input())

output = compare(n,leer(),leer())
if output != 2:
    print(output)