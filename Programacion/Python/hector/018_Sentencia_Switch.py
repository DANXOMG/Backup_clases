# Uso de switch -> Se llama match en python

def usar_switch(numero):
    match numero:
        case 1:
            print("\nEsta es la opción UNO.")
        case 2:
            print("\nEsta es la opción DOS.")
        case 3:
            print("\nEsta es la opción TRES.")
        case 4:
            print("\nEsta es la opción CUATRO.")
        case _:
            print("\nEsta opción no es válida.")
            
# Uso de la función usar_switch
usar_switch(2)
usar_switch(4)
usar_switch(8)