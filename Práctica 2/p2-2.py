def leer():
    v = list(map(int,input().split()))
    w = list(map(int,input().split()))
    return v, w

def compare(v,w):
    if len(v) == len(w):
        equal = 0
        for i in range(len(v)):
            if v[i] > w[i]:
                ans = 1
                equal = 1
                break
            if w[i] > v[i]:
                ans = -1
                equal = 1
                break
        if equal == 0:
            ans = 0
    elif len(v) > len(w):
        ans = 1
    else:
        ans = -1
    return ans

input()
v = list(map(int,input().split()))
w = list(map(int,input().split()))

print(compare(v, w))