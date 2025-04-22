def mifuncion():
    #variable local
    var1= 4
    global var2
    print("La variable var3 tienen el valor: ",var3)
    var2= var2 * 2

var1 = 1
var2= 2
var3= 3
print("Valores de las variables", var1, var2, var3)
mifuncion()
print("Valores de las variables", var1, var2, var3)
mifuncion()
print("Valores de las variables", var1, var2, var3)