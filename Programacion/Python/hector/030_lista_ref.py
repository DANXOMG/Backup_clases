def listaref(lista):
    lref = []
    for i in range(len(lista)):
        lref.insert(0,lista[i])
        lista[i] = 0
    return lref

milista = [1,2,3]
print(listaref(milista))
print(milista)