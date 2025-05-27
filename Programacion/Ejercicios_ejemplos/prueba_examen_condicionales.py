# Condicionales

#Ejercicio chatgpt
# Clasificador de edades 

#edad = int(input("Dame tu edad: "))

#if edad < 13:
#    print("Eres un niño")
#elif edad >= 13 and edad <=17:
#    print("Eres un adolescente")
#elif edad >= 18 and edad <=64:
#    print("Eres un adulto")
#else:
#    print("Eres un abuelo")


#Ejercicio con while


#while True:
#    edad = int(input("Dime tu edad: "))
#    if edad < 0 or edad > 120:
#        print("Parametros no validos")
#    elif edad <=13:
#        print("Eres un niño")
#        break
#    elif edad <=17:
#        print("Eres un adolescente")
#        break
#    elif edad <= 64:
#        print("Eres un adulto")
#        break
#    else:
#        print("Eres una persona adulta mayor")
#        break


#Ejercicio while contador

#def contador_hasta():
#    limite = int(input("Hasta que número quieres contar: "))
#    contador = 1
#    while True:
#        print(contador)
#        contador +=1 
        

#        if contador >= limite:
#            print(int(limite))
#            break

#contador_hasta()

#SENTENCIA FOR

#Ejercicio chatgpt tabla de multiplicar personalizada

usuario_num = int(input("Dame un numero del 1-10: "))

if 1 <= usuario_num <= 10:
    print("Número correcto")
    print("Procesando...")
    print("----" * 50)
    for usuario_num in range(1, 11):
        print(f"{usuario_num}")
else:
    print("Utilice un numero dentro del rango. Parametro no válido")





