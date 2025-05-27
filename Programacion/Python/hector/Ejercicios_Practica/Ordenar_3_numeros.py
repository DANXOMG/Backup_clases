# 15.- Ordenar tres números en orden ascendente.
# Solicita tres números al usuario y ordénalos en orden ascendente.

# Solicitamos números al usuario.
def pedir_numeros():
    global list_num
    list_num = [] 
    for i in range(0,3):
        numero = float(input("Indica un número: "))                
        list_num.append(numero)

# Voy a crear una segunda función que lo muestre, para poder aprovechar la primera en la siguiente tarea
def ordenar_numeros(): 
    list_num.sort(reverse=True)   
    print(list_num[::1])
ordenar_numeros()