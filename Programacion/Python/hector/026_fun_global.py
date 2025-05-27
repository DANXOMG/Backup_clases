def miFuncion():
    # Variable local
    var1 = 4
    # Variable global
    global var2
    print("La variable var3 tiene el valor: ", var3)
    var2 = var2 * 2
    
var1 = 1
var2 = 2
var3 = 3
print("valores de la variables", var1, var2, var3)
miFuncion()
print("valores de la variables", var1, var2, var3)
miFuncion()
print("valores de la variables", var1, var2, var3)
