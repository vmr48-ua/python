import math
num = float(input())

i = 0
total = 1
diff = 1
fact = 1

while diff > 0.000001:
    i += 1
    sq = num**i
    fact = math.factorial(i)
    div = sq/fact
    anterior = total
    total = total + div
    diff = abs(total-anterior)
    if anterior == 0:
        diff = 1
    #print('diff: {}, total: {}, anterior: {}, fact: {}, sq: {}, div: {}'.format(diff,total,anterior,fact,sq,div))
print(round(total,6))
#print(round(math.e**num,6))
#print((round(math.e**num,6)-round(total,6)))
