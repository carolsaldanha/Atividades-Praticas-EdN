import random

def gerar_senha(tamanho):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{};:,.<>?/|"
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

quantidade = int(input("Quantos caracteres a senha deve ter? "))
print("Senha gerada:", gerar_senha(quantidade))
