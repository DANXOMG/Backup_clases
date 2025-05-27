def dividir_texto(texto):
    """El objetivo es dividir el texto en en frases divididas por |"""
    versos = texto.split("\n")
    """versos2 = texto.split(";")"""
    salida = ""
    for i in range(len(versos)):
        salida += versos[i]
        """if versos2:
            salida = salida + "\n"""
        if i < len(versos) - 1:
            salida = salida + "|"
        
    return salida    

poema = """Con diez cañones por banda
viento en popa a toda vela
no corta el mar, sino vuela
un velero bergantín;
bajel pirata que llaman,
por su bravura, el Temido,
en todo mar conocido
del uno al otro confín."""

print(dividir_texto(poema))