# Contar el número de vocales de una cadena

def contar_vocales():
    cadena = input("Introduce una cadena: ").lower()
    vocales = "aeiou"
    total_vocales = sum(1 for caracter in cadena if caracter in vocales)
    print (f"En número de vocales es: {total_vocales}")    
    
contar_vocales()