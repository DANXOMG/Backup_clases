#Solucion profe
def quitar_repes(lista_nombres):
    listaSR = []
    for i in range(len(lista_nombres)):
        if lista_nombres[i] not in listaSR:
            listaSR.append(lista_nombres[i])
    return listaSR

def solo_nombres(lista_nombres):
    listaON = []
    for i in range(len(lista_nombres)):
        listaON.append(lista_nombres[i].split(" ")[0])
    return listaON
    

def lista_nombres(ListaSR):
    """Lista con nombres ordenadas alfabeticamente, sin repetidos"""
    listaordenada = []
    for i in range(len(ListaSR)):
        listaordenada.append(ListaSR[i])
        listaordenada.sort()
    return listaordenada

    
    
def apellidos_desc(nombres):
    """Lista con apellidos de actores ordenados de mayor a menos"""



def nombre_mas_corto(nombres):
    """Nombre mas corto de la lista"""




# Programa principal
nombres = ["arnold schwarzenegger", "alec baldwin", "antonio banderas", "julián sequeira", "sandra bullock", "keanu reeves", "julbob pybites", "antonio banderas", "julián sequeira"]


ListaSR = quitar_repes(nombres)
LSRN = solo_nombres(ListaSR)


print(nombres)
#print(quitar_repes(nombres))
#print(solo_nombres(nombres))
#print(LSRN)
print(lista_nombres(ListaSR))

