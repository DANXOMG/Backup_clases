# Lista vacia

lista_vacia_1 = []
lista_vacia_2 = list()

# Rellenar listas

motocicletas = ["honda", "suzuki", 'honda', 'yamaha']
print(motocicletas)
motocicletas.append("ducati")
print(motocicletas)
motocicletas.insert(0, 'derbi')
print(motocicletas)
motocicletas[2] = "bmw"
print(motocicletas)
motocicletas.insert(2, 'suzuki')
print(motocicletas)

### Borraos

elmento_cero = motocicletas.pop(0)
print(motocicletas)
print(elmento_cero)

ultimo_elemento = motocicletas.pop()
print(motocicletas)
print(ultimo_elemento)

motocicletas.remove("bmw")
print(motocicletas)

while "honda" in motocicletas:
    motocicletas.remove("honda")
    
print(motocicletas)

motocicletas.clear() #Borra todos los elemento de una lista
print(motocicletas)

# Regeneramos la lista
motocicletas = ["honda", "suzuki", 'honda', 'yamaha']
print(motocicletas)

### Ordenación

motocicletas.sort() # Ordena alfabeticamente
print(motocicletas)

motocicletas.sort(reverse=True) # Ordena empezando por la Z
print(motocicletas)

### Accesos a una lista

numeros = [1,2,3,4,5,6,7,8]

primer_elemento = numeros[0]
print(primer_elemento)

dos_elementos = numeros[0:2]
print(dos_elementos)

dos_ultimos = numeros[-2:]
print(dos_ultimos)

todos_elementos = numeros[::1]
print(todos_elementos)

impares = numeros[::2]
print(impares)

pares = numeros[1::2]
print(pares)

lista_reversa = numeros[::-1]
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
#comida.extend(motocicletas)
print(comida)

posicion_tacos = comida.index("tacos")
print(posicion_tacos)

posicion_pizza = comida.index("pizza")
print(posicion_pizza)

### Métodos generales

numeros = [1,2,3,4,5,6,7,8]
print(min(numeros))
print(max(numeros))
print(sum(numeros))
print(len(numeros))
# Ver como se calcula la media
print(sum(numeros)/len(numeros))