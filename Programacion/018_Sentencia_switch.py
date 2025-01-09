# Uso de switch

def usar_switch(numero):
    match numero:
        case 1:
            print("Esta es la opcion UNO")
        case 2:
            print("Esta es la opcion DOS")
        case 3:
            print("Esta es la opcion TRES")
        case 4:
            print("Esta es la opcion CUATRO")
        case _:
            print("Esta opcion no es valida")

#USO DE LA FUNCION USAR_SWITCH

usar_switch(2)
usar_switch(4)
usar_switch(8)