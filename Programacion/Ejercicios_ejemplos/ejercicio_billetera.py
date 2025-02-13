### 1.- Crea una variable dinero_inicial con el dinero que tienes en tu billetera (por ejemplo 50)
### 2.- Crea una variable compra con el precio del producto que deseas comprar (por ejemplo 20)
### 3.- Usando un bucle "While" realiza las siguientes acciones:
    ### si el dinero en tu billetera es suficiente para comprar el producto (dinero_inicial >= compra), resta el precio del producto al dinero inicial e imprime el mensaje
    ### "Producto comprado, dinero restante: "dinero restante en tu billetera"
    ### Si el dinero en tu biletera no es suficiente para comprar el producto imprime: "No tienes suficiente dinero para comprar este producto" fuera del bucle.


dinero_inicial = 50
compra = 20

while dinero_inicial >= compra:
    dinero_inicial = dinero_inicial - compra
    print("Producto comprado")
    print("Dinero restante: ", dinero_inicial)

if dinero_inicial < compra:
    print("No tienes suficiente dinero")
