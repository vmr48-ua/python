"""
def Catalan(n):
    if n <= 1:
        return 1
    else:
        ans = 0
        for i in range(n):
            ans += (Catalan(i) * Catalan(n-(i+1)))
        return ans

print(Catalan(15))
"""
# Este código funciona bien hasta Catalan(15), a partir de donde
# resulta muy costoso calcular todos los Catalan anteriores cuando se calcula
# si conseguimos almacenar los valores previamente calculados en una lista,
# nos ahorraremos tiempo de ejecución

def Catalan(n,cat=[]):
    if n <= 1:
        return 1
    else:
        ans = 0
        for i in range(n):
            if len(cat) <= i: # si el elemento no está en la lista lo calcula
                ans += (Catalan(i,cat) * Catalan(n-(i+1),cat))
            else:             # si el elemento ya está en la lista lo coge de la lista
                ans += (cat[i] * cat[n-(i+1)])
            if i == len(cat): # si el elemento no estaba en la lista lo añade
                cat.append(Catalan(i,cat))
        return ans
    
print(Catalan(50))
