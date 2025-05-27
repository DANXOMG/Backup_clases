# Función para contar números hasta un limite.

def contar_hasta(limite):
    contador = 1
    print(f"\nContando hasta: {limite} \n")
    while contador < limite:
        print(f"Contador: {contador}")
        contador += 1
        
# Llamda a la función contar_hasta
contar_hasta(26)