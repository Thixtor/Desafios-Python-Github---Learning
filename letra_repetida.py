def letraRepetida(texto):
    texto_limpio = texto.lower().replace(" ", "")
    letras_repetidas = []
    for letra in texto_limpio:
        if letra in letras_repetidas:
            print(letra)
            break
        else:
            letras_repetidas.append(letra)

    if len(letras_repetidas) == len(texto_limpio):
        print(None)

prueba1 = "fdtg"

letraRepetida(prueba1)
