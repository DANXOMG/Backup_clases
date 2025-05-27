#El siguiente programa maneja una variable de tipo string que contiene el texto de un poema. Escribir el código necesario para dividir su contenido en líneas.

def dividir_texto(texto):
    versos = texto.split('\n')
    salida=''
    for i in range(len(versos)):
        salida += versos[i]
        if i < len(versos) - 1:
            salida = salida + '|'
    return salida

poema = "" "aaaa bbbb cccc dddd eeee ffff gggg hhhh iiiii jjjjj kkkkk lllll mmmmm nnnnn ooooo ppppp qqqqq rrrrr sssss ttttt uuuuu vvvvv wwww xxxxx yyyyy zzzzz" ""



texto = "En viento en popa a toda vela, no corta el mar, sino vuela. Un velero bergantil" 
print(dividir_texto(poema))

