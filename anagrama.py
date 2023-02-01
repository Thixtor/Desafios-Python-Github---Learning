def esAnagrama(texto1, texto2):

    texto1_sorted = sorted(texto1.lower())
    texto2_sorted = sorted(texto2.lower())

    if texto1_sorted == texto2_sorted:
        return True
    else:
        return False
       
print(esAnagrama("alto", "bajo"))