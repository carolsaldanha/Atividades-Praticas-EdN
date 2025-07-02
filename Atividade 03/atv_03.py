def converter_temperatura(valor, origem, destino):
    if origem == "C":
        if destino == "F":
            return (valor * 9/5) + 32
        elif destino == "K":
            return valor + 273.15
    elif origem == "F":
        if destino == "C":
            return (valor - 32) * 5/9
        elif destino == "K":
            return (valor - 32) * 5/9 + 273.15
    elif origem == "K":
        if destino == "C":
            return valor - 273.15
        elif destino == "F":
            return (valor - 273.15) * 9/5 + 32
    return valor  

valor = float(input("Digite o valor da temperatura: "))
origem = input("Unidade de origem (C, F ou K): ").upper()
destino = input("Unidade de destino (C, F ou K): ").upper()

resultado = converter_temperatura(valor, origem, destino)
print(f"{valor}°{origem} é igual a {resultado:.2f}°{destino}")
