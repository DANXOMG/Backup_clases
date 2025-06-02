import random
import os
import numpy as np
import platform


# Crea una lista con los números del 1 al 10 y devuelve una nueva lista con los cuadrados de los números pares

def numeros_pares(lst):
    lista_vacia = []
    for i in lst:
        if i**2 % 2 == 0:
            lista_vacia.append(i)
    print(lista_vacia)

numeros_pares([1,2,3,4,5,6,7,8,9,10,11])

print("**" * 50)


# Dado un diccionario con nombres y edades, muestra solo los mayores de edad

diccionario = {"Ana": 20, "Pedro": 30, "Mario": 23, "Gimena": 25, "Antonio": 16, "Sara": 15, "Diego": 17}

def mayores_edad(diccionario):
    for nombre, edad in diccionario.items():
        if edad > 18:
            print(nombre, " : ",  edad)

mayores_edad(diccionario)
print("**" * 50)


# Dada una lista de tuplas (nombre, edad), imprime los nombres de los mayores de edad

datos = [("Ana", 17), ("Luis", 22), ("Marta", 19)]

for nombre, edad in datos:
    if edad > 18:
        print(nombre, edad)

print("**" * 50)


# # Usa el módulo random para imprimir un número aleatorio entre 1 y 100

print("Dime un rango de numeros en el que quieras moverte")
print("Te daré un numero aleatorio dentro de ese rango")

rango = int(input("Dame el rango de inicio: "))
rangomax = int(input("Dame el rango del final: "))
print(f"Selecionaste el rango para iniciar: {rango}")
print("..." * 50)
print(f"Selecionaste el rango para terminar: {rangomax}")
print("..." * 50)
print("Ahora te dare tu numero aleatorio: ")
print("..." * 50)
print(random.randint(rango, rangomax))
print("**" * 50)


# Usa un bucle for para sumar los números del 1 al 10

suma = 0
for i in range(1,11):
    suma =+ i
    print(suma)
    
# Dado un número, indica si es positivo, negativo o cero

n = int(input("Dame un numero y te diré si es positivo, negativo o cero: "))
if n > 0:
    print("El numero es positivo")
elif n < 0: 
    print("El numero es negativo")
else:
    print("El numero es cero")








