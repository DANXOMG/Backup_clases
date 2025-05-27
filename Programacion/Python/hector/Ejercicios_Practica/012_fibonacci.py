iniciales = [0,1]

def añadir():
    rango = (int(input("Introduce el largo de la secuencia: "))-2)
    for i in range(rango):
        iniciales.append(iniciales[i] + iniciales[i+1])
    print(iniciales[::1])
añadir()