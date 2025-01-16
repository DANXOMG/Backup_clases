def evaluar_numero():
    num = float(input("Ingrese un numero: "))

    if num >0:
        print('El numero es mayor que cero')
    elif num <0:
        print('El numero es menor que cero')
    else:
        print("El numero es cero")


evaluar_numero()