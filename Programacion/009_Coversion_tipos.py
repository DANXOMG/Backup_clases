#Ejemplo1: Covertir de cadena/string a entero

cadena = "123"
entero = int(cadena)

print("Cadena: ", cadena)
print("Entero: ", entero)

#Verificacion de como se pasa de cadena a entero
print(entero + 32) #El resultado sera 155


#Ejemplo2: convertir entero a cadena

numero = 546
cadena = str(numero)

print("Entero: ", numero)
print("Cadena: ", cadena)


#Ejemplo3: Convertir de flotante a entero

flotante= 45.67
entero = int(flotante)

print("Flotante: ", flotante)
print("Entero: ", entero)


#Ejemplo4: Convertir  de lista a conjunto

lista = [1, 2, 3, 4, 5]
conjunto = set(lista)
print("lista: ", lista)
print("conjunto: ", conjunto)

#Eejmplo5: Convertir diccionario a lista de claves

diccionario = {"a":1, "b":2, "c":3}
lclaves = list(diccionario.keys())
lvalores = list(diccionario.values())

print("Diccionario. ", diccionario)
print("Lista claves: ", lclaves)
print("Lista valores: ", lvalores)
print(diccionario["a"])