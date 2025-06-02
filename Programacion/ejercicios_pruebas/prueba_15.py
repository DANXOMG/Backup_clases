import numpy as np
import pandas
import os
# ejemplo sencillo de array

numeros = [10,20,30,40,50]

print(numeros[1])
print(numeros[4])
print(numeros)

#modificar valor 
numeros[2] = 25

print(numeros)

#Otro ejemplo con numpy

numeros1 = np.array([1,2,3,4,5])
print(numeros1[1])
print(numeros1)

numeros1[1] = 0
print(numeros1)

#Sumar arrays
a = np.array([10,20,30])
b = np.array([40,50, 60])

resulto= a + b
print(resulto)

#EJEMPLO DE PANDAS

datos = {
    "Nombre" : ["Ana", "Pedro", "Antonio"],
    "Edad" : [23, 20, 18]
}

data = pandas.DataFrame(datos)
print(data["Edad"])

#calcular la media de edad
media = data["Edad"].mean()