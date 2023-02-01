import re

def convertir_slug(texto):
    texto_ordenado = texto.lower().strip().replace(" ", "-")

    texto_slug = re.sub("[^\W\-]", "", texto_ordenado)

    print(texto_slug)

convertir_slug("Hola")