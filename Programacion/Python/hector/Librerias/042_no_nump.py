import numpy as np

print("Creación de arrays y propiedades")

# Crear un array (es un tipo de datos complejos, colección de datos simples)

a = np.array([1,2,3])
b = np.array([[1,2],[3,4]])

print("a=", a)
print("b=", b)
print(" ")

#Propiedades de los arrays
print("a.shape = ", a.shape) #(3,)
print("b.shape = ", b.shape) #(2,2)
print("a.ndim = ", a.ndim) #1 Saber dimensión
print("b.ndim = ", b.ndim) #2 Saber dimensión
print("-" * 50)

# Arrays especiales
print("Arrays especiales")
print("np.zeros((2,3)) = ", np.zeros((2,3)))