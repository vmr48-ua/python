def recorta(M,i,j):
    i = i-1
    j = j-1
    if check(M,i,j) == 0: 
        A = cutCol(cutRow(M,i),j)
    else:
        A = []
    return A 

def check(M,i,j):
    valid = 0
    if i > len(M) or len(M) == 0 or j > len(M[0]):
        valid = 1
    return valid

def cutRow(M,i):
    M = M[::-1]
    for _ in range(0,i):
        M.pop()
    return M[::-1]

def cutCol(M,j):
    for i in range(len(M)):
        M[i] = M[i][::-1]
        for _ in range(j):
            M[i].pop()
        M[i] = M[i][::-1]
    return M

M = [[1,2,3,4],[5,6,7,8]]
i = 3
j = 0

print(recorta(M,i,j))
print(M)