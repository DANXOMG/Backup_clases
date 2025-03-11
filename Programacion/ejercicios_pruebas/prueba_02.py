import math #importamos la libretia math para poder meter el numero pi

radio = float(input("Dame el radio de tu cilindro: ")) #IMPORTANTE meter en la variable que sea float (para que el numero sea flotante) y despues con input un mensaje para que el usuario meta un valor
altura = float(input("Dame la altura de tu cilindro: ")) #IMPORTANTE meter en la variable que sea float (para que el numero sea flotante) y despues con input un mensaje para que el usuario meta un valor
volumen = math.pi * (radio ** 2) * altura


def volumen_cilindro(radio, altura):

    if radio <= 0 or altura <= 0:
        return "El radio y la altura debe ser mayor que 0"
    return volumen

resultado = volumen_cilindro(radio, altura)

print("Dame la altura y el radio de tu cilindro para que lo pueda calcular")
print(radio)
print(altura)
print("Este es el volumen de tu cilindro: ", resultado)