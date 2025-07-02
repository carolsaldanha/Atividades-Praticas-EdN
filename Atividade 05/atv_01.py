def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float):
    
    if valor_conta < 0 or porcentagem_gorjeta < 0:
        raise ValueError("O valor da conta e a porcentagem da gorjeta não podem ser negativos.")
        
    valor_gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return valor_gorjeta

if __name__ == "__main__":
    try:
        total_da_conta = 75.50
        porcentagem_desejada = 10

        gorjeta_calculada = calcular_gorjeta(total_da_conta, porcentagem_desejada)

        print(f"O valor da gorjeta a ser deixada é: R${gorjeta_calculada:.2f}")

    except ValueError as e:
        print(f"Erro: {e}")