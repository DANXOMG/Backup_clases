# Escribe un código que verifique si una palabra ingresada es un palíndromo.
"""
---------------------------------------------------------------------------------------------
Un palíndromo es una palabra o frase que se lee igual de izq a der, y de der a izq.

Para ello realizaré una función en la que pediré una palabra al usuario, la almacenaré en una
lista, para poder darle la vuelta y veríficar si es igual.
---------------------------------------------------------------------------------------------
"""
def verifica_palindromo():
    palabra = input("Indica un palabra: ")
    palabra_sep = list(map(str, palabra.lower()))
    alreves = palabra_sep[::-1]
    # Con join vuelvo a unir los elementos para después compararlos
    #palabra_jun_1 = "".join(palabra_sep)
    #palabra_jun_2 = "".join(alreves)
    if palabra_sep == alreves:
        print(f"La plabra {palabra} es un palíndromo")
    else:
        print(f"La plabra {palabra} no es un palíndromo")
verifica_palindromo()