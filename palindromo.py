def esPalindromo(texto):
    texto_limpio = texto.lower().replace(" ", "")
    print(texto_limpio == texto_limpio[::-1])
   
esPalindromo(input("¿Es palindromo? "))