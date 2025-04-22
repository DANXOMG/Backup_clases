#Lista vacia
lista_vacia = []
lista_vacia2 = list()

#Rellenar listas

motocicletas = ["honda", "suzuki", "honda", "yamaha"]
print(motocicletas)
motocicletas.append('ducati')
print(motocicletas)
motocicletas.insert(0, 'derbi')
print(motocicletas)
motocicletas[2] = "bmw"
print(motocicletas)


### Borrados

elemento_cero = motocicletas.pop(0)
print(motocicletas)
print(elemento_cero)

ultimo_elemento = motocicletas.pop()
print(motocicletas)
print(ultimo_elemento)


motocicletas.remove("bmw")
print(motocicletas)


while 'honda' in motocicletas:
    motocicletas.remove('honda')

print(motocicletas)

motocicletas.clear()
print(motocicletas)

motocicletas = ["honda", "suzuki", "honda", "yamaha"]
print(motocicletas)


### Ordenacion

motocicletas.sort()
print(motocicletas)

motocicletas.sort(reverse=True)
print(motocicletas)


### Accesos a una lista

numero=[1,2,3,4,5,6,7,8]

primer_elemento = numero [0]
print(primer_elemento)

dos_elementos= numero[0:1]
print(dos_elementos)

dos_ultimos_numeros = numero [-2:]
print(dos_ultimos_numeros)

todos_elementos = numero[::1]

numeros_impares = numero[::2]

numeros_pares = numero[1::2]

lista_reversa = numero [::-1]

print(todos_elementos)
print(numeros_impares)
print(numeros_pares)
print(lista_reversa)

### Otros métodos

comida = ["pizza", "lentejas", "tacos", "pizza", "escalope"]

print(comida)


copia_comida = comida[:]
print(copia_comida)

otra_copia_comida = comida.copy()
print(otra_copia_comida)

cuenta_pizza = comida.count("pizza")
print(cuenta_pizza)


comida.extend(["ensalada", "manzana"])
print(comida)


posicion_tacos = comida.index("tacos")
print(posicion_tacos)

posicion_pizza = comida.index("pizza")
print(posicion_pizza)


### Metodos generales
numeros = [1,2,3,4,5,6,7,8,9,10]

print(min(numeros))
print(max(numeros))
print(sum(numeros))
print(len(numeros))
