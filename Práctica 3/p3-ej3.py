"""
Escribe un programa que lea carácter a carácter un archivo
de texto cuyo nombre será leído del teclado con el mensaje
’Nombre del archivo:’. El programa sustituirá cada carácter
leído, excepto si es un espacio en blanco de cualquier tipo,
por el siguiente carácter en orden ASCII. El carácter 
transformado será enviado a otro archivo con el nombre obtenido
añadiendo al de lectura (antes de la extensión) la palabra
’_cod’. Se debe tener en cuenta la posibilidad de que el 
archivo de entrada o el de salida no se puedan abrir emitiendo
en este caso el mensaje: 
'Problema con el fichero de entrada o de salida.'

Ejemplo:
stdin=entrada.txt
El otro día 24 de septiembre
tuvimos clase de
    Fundamentos de la Programación
stdout=entrada_cod.txt
Fm pusp eîb 35 ef tfqujfncsf
uvwjnpt dmbtf ef
    Gvoebnfoupt ef mb Qsphsbndbjôo
"""

def extension(a):
    ext = ''
    for i in range(len(a)-1,0,-1):
        ext+=a[i]
        if a[i] == '.':
            ext = ext[::-1]
            break
    return ext

symbol = [' ','\n',',','.','¿','?','!','¡','\\','(',')',':',';','[',']','{','}']
archivo = input('Nombre del archivo: ')
try:
    file = open(archivo,'r')
    cod = open(archivo[:-(len(extension(archivo)))]+'_cod'+extension(archivo),'w')
    for fila in file:
        for caracter in fila:
            if caracter not in symbol:
                cod.write(chr(ord(caracter)+1))    
            else:
                cod.write(caracter)
    file.close()
    cod.close()
except IOError:
    print('Problema con el fichero de entrada o de salida')