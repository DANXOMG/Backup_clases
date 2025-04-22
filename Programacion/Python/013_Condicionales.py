#Funcion para demostrar el uso de condicionales

def verificar_numero(numero):

    # condicional simple
    if numero > 0:
        print(f"El numero es mayor que cero.")
        # la f de formato da igual si la quitas

        #condicional con oarte else

        if numero == 0:
            print("El numero es igual a cero.")
        else:
            print("El numero no es igual a cero.")


    #Condicional con parte elif

    if numero < 0:
        print(f"El numero {numero} es negativo.")
    elif numero > 10:
        print(f"El numero es mayor que 10·")
    else: 
        print(f"El numero {numero} está entre 1 y 10.")

    
#llamadas a la funcion verificar_numero

verificar_numero(15)
verificar_numero(-5)
verificar_numero(0)
verificar_numero(7)