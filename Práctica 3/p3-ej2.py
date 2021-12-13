from sys import argv
from subprocess import check_output
array = []

if len(argv) == 2:
    try:
        archivo = argv[1]
        sol = check_output("wc "+archivo, shell=True)
        sol = list(sol.decode())
        for _ in range(len(archivo)+2):
            sol.pop()
        for char in sol:
            if char == ' ':
                sol.pop(0)
            if char != ' ':
                break
        print(sol)
        while(len(sol) != 0):
            i = 0
            for char in sol:
                i += 1
                if i > 1 and char == ' ':
                    break
                if char != ' ':
                    array.append(char)
            for _ in range(i):
                sol.pop(0)
            print(int(''.join(map(str,array))))
            array.clear()

    except IOError:
        print('Error: no se puede abrir el archivo',argv[1])
else:
    print('Uso: python3',argv[0],'archivo')