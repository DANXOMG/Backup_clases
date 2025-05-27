def quitar_repetidos(listanombres):
    listasinrepetidos = []
    for i in range(len(listanombres)):
        if listanombres[i] not in listasinrepetidos:
            listasinrepetidos.append(listanombres[i])
    return listasinrepetidos

nombres = ["Ana", "Pedro", "Rosa", "Patri", "Georgina", "Roman", "Ana"]
print(quitar_repetidos(nombres))
print(nombres)