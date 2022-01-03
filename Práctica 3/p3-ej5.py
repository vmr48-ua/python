from scipy.integrate import quad 
import numpy as np

def decimales(err):    # Devuelve a cuantos decimales hay que 
    cont = 0           # redondear el valor en función a un error ya ajustado
    if err >= 1:
        while 10*(err-int(err)) == 0:
            err /= 10
            cont -= 1
        cont += 1
    else:
        while int(err) == 0:
            err *= 10
            cont += 1
        if int(err) == 1 and int((err-1)*10) != 0:
            cont += 1
    return cont

def roundBien(a, n=0): # Redondea al entero más cercano, 
    if n == 0:         # el caso del 5 al mayor
        return int(a + 0.5)
    else:
        valor = 10 ** n
        return int(a * valor + 0.5) / valor

def ajustar(a):        # Ajusta a la primera cifra significativa
    b = a
    cont = 0
    if a < 1:
        while int(a) == 0:
            a *= 10
            cont += 1
        if int(a) == 1 and int((a-int(a))*10) < 5:
            cont+=1   
        return roundBien(b,cont)     
    else:
        if a >= 100:
            a = int(a)
            while a > 1:
                a /= 10
                cont -= 1
            cont += 1
            if int(a*10) == 1 and int(((a*10)-int(a*10))*10) < 5:
                cont += 1
            return int(roundBien(b,cont))
        elif a >= 10:
            if (int(a)-int(10*(a/10-int(a/10))))/10 == 1 and int(a-10) < 4:
                cont = 0
            else:
                cont = -1
            return roundBien(b,cont)
        else:
            if int(a) - 1 == 0 and int((a-int(a))*10) < 5:
                cont = 1
            else:
                cont = 0
            return roundBien(b,cont)

def cifrasSignificativas(valor,err):
    print(f"{roundBien(valor,decimales(ajustar(err))):.{decimales(ajustar(err))}f}",\
    '\xB1',ajustar(err),end='')

def funcion(x):
    return ((1/(1+x)) - np.exp(-x))/x

integral = quad(funcion, 0, np.inf)[0]
error =    quad(funcion, 0, np.inf)[1]

#print(quad(funcion, 0, np.inf))
cifrasSignificativas(integral,error)
print(' u')