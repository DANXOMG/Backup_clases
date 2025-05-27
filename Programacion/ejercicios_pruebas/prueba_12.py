# Ejemplo numpy
import numpy as np
import pandas as pd

#EJEMPLO CON NUMPY

# crear un array que es como una lista pero mejor
miarray = np.array([1, 2, 3, 4, 5])
print(miarray)

# crear una tabla con numpy
tablavalores = np.array([[1, 2], [0, 0]]) # importante meter los valores en ["[]"]
print(tablavalores)

#jugar con los valores de un array
valores = np.array([1, 2, 3])
print(np.sum(valores)) #Suma todos los valores del array

# Media con numpy de un array
media = np.array([10, 20, 40]) #vamos a hacer la media de estos valores del array
print(np.mean(media))
# tambien podemos jugar con los valores como resultado
print(media)
print(media * 2)




# EJEMPLO CON PANDAS

#Crear una tabla con pandas 

datos = pd.DataFrame({
    "Nombre": ["Antonio", "Jose", "Mariola"],
    "Apellido": ["Del Pino", "Garcia", "De la Rosa"],
    "Curso": ["1º", "2º", "2º"],
    "Edad": [24, 36, 26]
})

print(datos)
print(datos.head()) #Con pandas esto te muestra las primeras 5 filas de la tabla
print(f"La media de las edades es: ", datos["Edad"].mean()) #De esta manera nos daría la media de las edades
# Ahora para sumar valores dentro de una columna en este caso edad
print(f"La suma de las edades: ", datos["Edad"].sum()) # con esto sumariamos los valores de "Edad"
# Ahora vamos a filtrar datos con mas exatitud
# Vamos a coger de la columna "Edad" y le vamos a poner una condicion
menores = datos[datos["Edad"] < 25]
print("Te voy a mostrar el alumno con menor edad: ")
print(menores)


# Ahora para leer un archivo CSV o excell

archivocsv = pd.read_csv("Archivo.csv") #Don esto leería el documento CSV
print(archivocsv.head()) # Con esto mostraría las primeras filas del documento
