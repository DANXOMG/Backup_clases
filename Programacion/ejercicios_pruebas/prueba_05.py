#Sentencia While

#contador = 0
#while contador <= 5: 
#    print(contador)
#    contador += 1
 

limite= int(input("Hasta que numero quieres contar? "))
def contar_hasta(limite):
    contador = 1
    print(f"contando hasta {limite}")
    while contador <= limite:
        print(contador)
        contador += 1

contar_hasta(limite)

        
