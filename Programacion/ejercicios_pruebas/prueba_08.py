#def pedir_num():
#    numero = int(input("Dame un numero: "))
#    return numero
#
# a= pedir_num()
# b= pedir_num()
# c= pedir_num()
# d= pedir_num()
# print(a, b, c, d)



# Tomar como valor

#def tomar_como_valor(valor):
#    if valor == 0:
#        print("ok")
#        return valor

#salida1 = tomar_como_valor(0)
#print("Salida1: ", salida1)
#salida2 = tomar_como_valor(1)
#print("Salida2: ", salida2)

# Esta funcion lo unico que hace es coger valor como parametro y si es == 0 imprime "ok" 
# y devuelve ese valor 
# si el valor tiene otra condicion que no sea == 0 no hará nada por (None)

def var_global():
    var1 = 1 #variable local "desaparece al salir de la funcion"
    global var2
    print("la var1 es: ", var1)

    print("la var3 es: ", var3)
    var2 = var2 + 2
    var1 = var1 + 1

var1 = 1
var2 = 2
var3 = 3

print("Valores de las variables: ", var1, var2, var3)
var_global()
print("Valores de las variables: ", var1, var2, var3)
var_global()
print("Valores de las variables: ", var1, var2, var3)







