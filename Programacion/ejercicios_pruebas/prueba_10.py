def listavacia(lista):
    listavacia = []
    for i in range(len(lista)):
        listavacia.insert(0, lista[i])
        lista[i] = 0
    return listavacia

milista= [1, 2, 3, 4, 5 ]
print(listavacia(milista))
print(milista)

otralista = [10, 9, 8, 7, 6]
print(listavacia(otralista))
print(otralista)