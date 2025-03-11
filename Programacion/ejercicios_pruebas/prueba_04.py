#condicionales

def verificar_numero(numero):
    if numero > 0:
        print(f"el numero es mayor que 0")

    if numero == 0:
        print(f"el numero es igual a 0")
    else:
        if numero < 0:
            print(f"el numero no es menor a 0")
        


# parte elif

def verificar_numero2(numero):
    if numero < 10:
        print(f"el {numero} es menor que 10")
    elif numero > 10:
        print(f"el {numero} es mayor que 10")
    else:
        if numero == 10:
            print(f"el {numero} es igual a 10")

verificar_numero(11)
verificar_numero(0)
verificar_numero(-1)

verificar_numero2(10)
verificar_numero2(9)
verificar_numero2(11)