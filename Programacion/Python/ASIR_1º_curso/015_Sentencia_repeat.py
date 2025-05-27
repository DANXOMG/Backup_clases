# Funcion Repetir


def repetir_hasta():
    contador = 1
    limite = 5
    while True:
        print(f"Contador: {contador}")
        contador += 1
        #condicion de salida
        if contador >= limite:
            print(f"Este es el limite {limite}")
            print("Fin del bucle...")
            break


# llamada a la funcion

repetir_hasta()



