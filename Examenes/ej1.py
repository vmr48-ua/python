def cuenta(s,c):    # Cuenta cuantos caracteres c hay en la cadena s
    count = 0   # empiezo en 0
    for i in range(len(s)):
        if c == s[i]: # si el carácter está en la cadena, aumento su contador
            count += 1
    return count    # siempre va a estar almenos una vez ya que es el propio carácter

def primerCaracterNoRepetido(s): # Imprime el primer caracter no repetido de una cadena
    s = s.lower()               # convierto a minúscula todos los elementos en mayúscula
    caracter = ""               # valor por defecto
    for i in range(len(s)):     
        if cuenta(s,s[i]) == 1: # voy recorriendo la cadena y me guardo el primero que se 
            caracter = s[i]     # repite una única vez
            break               # acabo el bucle
    return caracter

if (primerCaracterNoRepetido(input('Introduce una cadena: ')) != ''):
    print('La cadena tiene carácteres no repetidos')
else:
    print('Todos los carácteres de la cadena están repetidos')
