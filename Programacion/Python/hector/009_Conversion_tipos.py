# Ejemplo de conversión de tipos

# Ejemplo 1: covertir de cadena a entero
cadena = "123"
entero = int(cadena)

print("Cadena: ", cadena, "--> Entero: ", entero)
#print(entero + 32)


# Ejemplo 2: convertir de entero a cadena
numero = 456
cadena2 = str(numero)

print("Entero: ", numero, "--> Cadena: ", cadena2)
#print(cadena2 + 32)


# Ejemplo 3: Convertir de flotante a entero
flotante = 45.67
entero2 = int(flotante)# Lo trunca no lo redondea

print("Flotante: ", flotante, "--> Entero: ", entero2)


# Ejemplo 4: Convertir de lista a conjunto
lista = [1,2,3,4,5]
conjunto = set(lista)

print("Lista: ", lista, "--> Conjunto: ", conjunto)


# Ejemplo 5: Convertir un diccionario a lista de claves También llamados arrays asociativos.
diccionario = {"Enero":1, "Febrero":2, "Marzo":3} # Los diccionarios tienen una clave y un valor
lclaves = list(diccionario.keys())
lvalores = list(diccionario.values())

print("Diccionario: ", diccionario, "--> Lista claves: ", lclaves)
print("Diccionario: ", diccionario, "--> Lista valores: ", lvalores)
print(diccionario["Enero"])# Para sacar un valor concreto llamamos al indice, en este caso una letra o palabra

