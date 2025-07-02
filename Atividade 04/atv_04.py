def verificar_pares_impares():
    
    contador_pares = 0
    contador_impares = 0

    print("Digite números inteiros. Digite 'fim' para encerrar.")

    while True:
        entrada = input("Digite um número inteiro: ").lower()

        if entrada == 'fim':
            break 

        try:
            numero = int(entrada)

            if numero % 2 == 0:
                print(f"O número {numero} é PAR.")
                contador_pares += 1
            else:
                print(f"O número {numero} é ÍMPAR.")
                contador_impares += 1
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")

    print(f"Total de números pares inseridos: {contador_pares}")
    print(f"Total de números ímpares inseridos: {contador_impares}")

verificar_pares_impares()