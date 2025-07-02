def calculadora():
    
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))

            num2 = float(input("Digite o segundo número: "))

            operacao = input("Digite a operação (+, -, *, /): ")

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Divisão por zero não é permitida.")
                resultado = num1 / num2
            else:
                raise ValueError("Operação inválida. Use +, -, * ou /.")

            print(f"Resultado: {resultado}")
            break 

        except ValueError as ve:
            print(f"Erro de entrada: {ve}. Por favor, insira números válidos e uma operação válida.")
        except ZeroDivisionError as zde:
            print(zde)
        except Exception as e:

            print(f"Ocorreu um erro inesperado: {e}")

calculadora()