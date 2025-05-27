import random

def elegir_palabra():
    palabras = ["python"]
    return random.choice(palabras)

def mostrar_palabra_oculta(palabra, letras_adivinadas):
    return " ".join(if letra in letras_adivinadas else "_" for letra in palabra)

def 