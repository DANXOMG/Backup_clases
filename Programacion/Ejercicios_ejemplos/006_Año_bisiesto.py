def año_bisiesto():
    
    año = int(input('Ingresa un año: '))

    #chatgpt
    #if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    #   print(f'El año {año} es bisiesto.')
    #else:
    #    print(f'El año {año} no es bisiesto.')

    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print('El año introducido es bisiesto')
    else:
        print('El año introducido NO es bisiesto')
        



año_bisiesto()