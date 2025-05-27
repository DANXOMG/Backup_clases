# Crea una variable dinero inicial con lo que tienes en la cartera
dinero_inicial = 100

# Crea una variable compra con el precio de un producto que deseas comprar
compra = 33

### Usa un bucle while y realiza las siguientes acciones
while dinero_inicial >= compra:
    # Si el dinero es suficiente para comprar el producto, resta a dinero inicial e imprime mensaje
    dinero_inicial -= compra
    # Producto comprado
    print("Producto comprado, dinero restante: ", dinero_inicial)
    
# Si no hay dinero suficiente imprimir no tuenes dinero para comprar este prodcuto
if dinero_inicial < compra:
    print("No tienes suficiente dinero en tu billetera para comprar este producto.")
    
# O se podría usar, aunque no muy correctoi
print("No tienes suficiente dinero en tu billetera para comprar este producto.")
