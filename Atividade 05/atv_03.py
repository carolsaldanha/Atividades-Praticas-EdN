def calcular_idade_em_dias(ano_nascimento):
    ano_atual = 2025 
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365 
    return idade_dias

ano = int(input("Digite seu ano de nascimento: "))
print("Sua idade aproximada em dias é:", calcular_idade_em_dias(ano))
