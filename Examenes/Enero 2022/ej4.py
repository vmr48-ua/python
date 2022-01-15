class Cuenta(object):
    def __init__(self,titular,cantidad=0):
            self.titular=titular
            self.cantidad=cantidad
                
    def __str__(self):
            return "Cuenta\n"+"Titular: " + self.titular+ " - Cantidad: "+str(self.cantidad)

    def ingresar(self,cantidad):
            #si la cantidad a ingresar no es 0 y es positiva la añade a cantidad
            if cantidad >= 0:
                    self.cantidad += cantidad
            else:
                    print("Error: estás tratando de ingresar una cantidad no válida")
            return self

    def retirar(self,cantidad):
    	    #si la cantidad a ingresar no es 0 y es positiva la sustrae de cantidad
            if cantidad >= 0:
                    self.cantidad -= cantidad
            else:
                    print("Error: estás tratando de ingresar una cantidad no válida")
            return self
        
cuenta1 = Cuenta("Pepe Botero",1000)
cuenta1.ingresar(500)
cuenta1.retirar(800)
print(cuenta1)
