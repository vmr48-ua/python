op = ''
a = float(input())

while op != '=':
    op = input()
    if op != '=':
        b = float(input())
        if op == '+':
            a = a+b
        elif op == '-':
            a = a-b
        elif op == '/':
            a = a/b
        elif op == '*':
            a = a*b
        print(a)
