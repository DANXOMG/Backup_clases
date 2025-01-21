def contar_vocales():

    cadena = input('Ingresa una cadena/palabra: ').lower() #.lower sirve para ponerlo en minusculas de forma automatica
    vocales = "aeiou"
    total_vocales = sum(1 for caracter in cadena if caracter in vocales)
    
    print(f'La cantidad de vocales es {total_vocales}')
contar_vocales()