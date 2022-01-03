"""
Escribir un programa que guarde en un diccionario los precios 
de las frutas de la tabla, pregunte al usuario por una fruta y 
un número de kilos y muestre por pantalla el precio de ese número
de kilos de fruta. Si la fruta no está en el diccionario debe
mostrar un mensaje informando de ello.
"""
tabla = {'Fruta' : ['Plátano', 'Manzana', 'Pera', 'Naranja'],\
        'Precio' : [1.35,       0.8,       0.85,   0.7]}

existe = False

fruta = input('Introduce una fruta: ')
kilos = float(input('Introduce los kilos: '))

for i in range(len(tabla['Fruta'])):
    if tabla['Fruta'][i] == fruta:
        print(round(kilos * tabla['Precio'][i],2))
        existe = True
        break

if not(existe):
    print('La fruta introducida no está almacenada en el diccionario')