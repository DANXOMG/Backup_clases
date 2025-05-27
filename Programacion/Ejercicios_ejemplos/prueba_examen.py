#variable booleana

es_fruta=True
print(es_fruta)

#variable lista

coches = ["audi", "toyota", "ford", "mclaren"]
print(coches)

#variable tupla
coordenadas = (10, 20)  
print(coordenadas)

#ejemplo tupla 2

madrid=(456213, 789456)
barcelona=(123456, 789456) 

ciudades = [("Madrid", madrid) , ("Barcelona", barcelona)]
for nombre, coordenadas in ciudades:
    print(f"{nombre} tiene las coordenadas {coordenadas}")

# Variable diccionario

diccionario = {"a": 1, "b": 2, "c": 3}
print(diccionario)

for nombre, num in diccionario.items():
    print(f"{nombre} tiene el valor: {num}")
    print(f"La posicion de {nombre} es: {diccionario[nombre]}")

# Pasar de numeros enteros a cadenas y viceversa
#pasar numero entero a cadena
num =123
cadena = str(num)
print(f"El numero sería: {num}")
print(f"La cadena sería: {cadena}")
print(f"El numero {num} + 10 es: {num + 10}")
print(f"La cadena {cadena} se convirtiria en str + 456: {cadena + "456"}")


#Convertir numero flotante a entero y viceversa
num = 50.5
entero = int(num)
print(f"Numero flotante: {num}")
print(f"Numero entero: {entero}")

#Convertir de lista a conjunto

lista = [1, 2, 3, 4 , 5, 5, 6]
conjunto = set(lista)
print(f"Lista: {lista}")
print(f"Conjunto: {conjunto}")
print("Las diferencias principales son: que en la lista se pueden repetir los elementos y en el conjunto no")


#Convertir diccionario a lista de claves y valores (coger claves "nombres" y valores por separado)
diccionario = {"Ana": 1, "Alberto": 2, "Juan Carlos": 3}
nombres = list(diccionario.keys())
valores = list(diccionario.values())
print(f"Aqui te muestro el diccionario: {diccionario}")
print("La conversion del diccionaria a lista de claves/nombres y valores sería: ")
print(f"Aqui te muestro la lista de nombres: {nombres}")
print(f"Aqui te muestro la lista de valores: {valores}")
print(f"Aqui te muestro la posicion que ocuparía Ana en el diccionario: {diccionario['Ana']}")




