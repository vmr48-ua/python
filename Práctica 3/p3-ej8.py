"""
Nos pasan el siguiente código que define la clase Conjunto
"""
class Conjunto(object):
    def __init__(self, lista):   # Constructor de la clase
        self.elementos = []      # atributo de instancia
        for x in lista:
            if x not in self.elementos:
                self.elementos.append(x)

    def union(self, A):     # métodos
        return Conjunto(self.elementos+A.elementos)
    
    def interseccion(self, A):
        aux = []
        for x in self.elementos:
            if x in A.elementos:
                aux.append(x)
        return Conjunto(aux)
    
    def cardinal(self):
        return len(self.elementos)

    def diferencia(self, A):
        final = []
        aux = self.elementos
        for x in aux:
            if x not in A.elementos:
                final.append(x)
        final.sort()
        return Conjunto(final)

    def difSimetrica(self, A):
        final = []
        aux = self.union(A).elementos
        for elem in aux:
            if aux.count(elem) == 1:
                final.append(elem)
        final.sort()
        return Conjunto(final)

    def __str__(self):
        # Este método especial define como se imprimirá un Conjunto en una
        # llamada a la función print
        cad = '{'
        for x in self.elementos[:-1]:
            cad += str(x) + ', '
        return cad + str(self.elementos[-1]) + '}'

A = Conjunto({1,2,3,4})
B = Conjunto({0,2,3,5,6})
print(A.diferencia(B))
print(A.difSimetrica(B))

"""
Añade a esta clase dos métodos diferencia y difSimetrica que 
realice estas operaciones entre el conjunto desde el que se 
las llama y el conjunto que se le pasa por parámetro. En el 
programa principal se deben crear los conjuntos A = {1,2,3,4}
y B = {0,2,3,5,6}, imprimiendo a continuación por pantalla A-B y AΔB
"""