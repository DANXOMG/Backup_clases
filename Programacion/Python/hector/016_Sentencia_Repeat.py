# Función Repetir Esta función no existe como tal, la hacemos con un while y con bucle infinito y le decimos cuando acabar

def repetir_hasta():
    contador = 1
    limite = 5
    while True:
        print(f"Contador: {contador}")
        contador += 1
        # Condición de salida
        if contador > limite: break
    print(f"Fin del bucle....")
    
#Llamada a la función repetir_hasta

repetir_hasta()