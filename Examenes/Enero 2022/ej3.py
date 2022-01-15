from numpy import exp,linspace,inf
import matplotlib.pyplot as plt
from scipy.integrate import quad

#Creo la función
def f(t,x):
    return (1/t) * exp(-t)

#Escribo en un archivo el resultado que quad me da para la función
def escribir():
    file = open("datos.txt","w")

    #Creo un espacio en el límite estipulado con 100 puntos
    a = linspace(0.1,2,100)
    #resultados contendrá 100 resultados de la integral en el rango estipulado
    resultados = []
    for i in a:
        resultados.append(quad(f,i,inf,args=i)[0])

    #Escribo todos los resultados en el archivo en el formato estipulado
    for i in range(len(resultados)-1):
        file.write('Ie(x{}) '.format(i+1) + str(resultados[i]) + '\n')
    file.write('Ie(x100) ' + str(resultados[99]))

    file.close()

#Grafica los resultados que lee de un archivo de datos
def graficar():
    archivo = open("datos.txt","r")
    datos = []
    grafica = []
    a = linspace(0.1,2,100)
    
    #Separo el texto de los datos y me guardo los datos en una lista
    for fila in archivo:
        fila = [str(x) for x in fila.split()]
        fila.pop(0)
        datos.append(str(fila))
    
    #Guardo en la lista grafica los datos con el formato correcto
    for linea in datos:
        dato = ''
        for caracter in linea:
            if caracter != '[' and caracter != ']' and caracter != '\'':
                dato += caracter
        grafica.append(float(dato))

    #Grafico los datos y los guardo en la foto correspondiente
    
    plt.plot(a,grafica)
    plt.savefig("ej3.png")
    archivo.close()

escribir()
graficar()
