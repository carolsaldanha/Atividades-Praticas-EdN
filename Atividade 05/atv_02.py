def palindromo(texto):
    texto = texto.lower()
    texto = ''.join(c for c in texto if c.isalnum())
    if texto == texto[::-1]:
        return "Sim"
    else:
        return "Não"

frase = input("Digite uma palavra ou frase: ")
print(palindromo(frase))