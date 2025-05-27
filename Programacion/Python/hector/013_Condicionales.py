# Función para demostrar el uso de condicionales

def verificar_numero(num):
    # Condicional simple
    if num > 0:
        print(f"El número es mayor que cero.")
        
    # Condicional con parte else
    if num == 0:
        print(f"El número es igual a cero.")
    else:
        print(f"El número no es igual a cero.")
        
    # condicional con parte elif
    
    if num < 0:
        print(f"El número {num} es negativo.")
    elif num > 10:
        print(f"El número {num} es mayor que diez.")
    else:
        print(f"El número {num} esta entre 0 y 10")
        
    # Llamadas a la función verificar_numero
    
verificar_numero(15)
verificar_numero(-5)
verificar_numero(0)
verificar_numero(7)