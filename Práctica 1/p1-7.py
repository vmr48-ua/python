num = 1
i = 0
mult = 1

while num != 0:
    num = float(input('Introduce un número: '))
    if num <= 100 and num > 0:
        i += 1
        mult *= num

if i > 0:
    print(round(mult**(1/(i)),3))
