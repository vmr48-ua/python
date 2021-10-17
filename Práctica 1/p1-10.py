""" 
# Esta es la primera forma que se me ocurrió de hacerlo, pero tiene el problema
# de que para x muy grandes, hay overflow, por lo que pensé la solución final

x = float(input())

n = -1
total = 0
div = 1

while div > 10**(-6):
    fact = 1
    n += 1
    sq = x**n
    for j in range (n, 0, -1):
        fact *= j
    div = sq/fact
    total += div
print(round(total,6)) """

x = float(input())

n = 0
total = 1
div = 1

while abs(div) > 10**(-6):
    n += 1
    div *= x/n
    total += div
print(round(total,6))
