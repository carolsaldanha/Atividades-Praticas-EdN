import json

pessoa = {'nome': 'Fernanda', 'idade': 30, 'cidade': 'Curitiba'}

with open('pessoa.json', 'w', encoding='utf-8') as f:
    json.dump(pessoa, f, indent=4) # indent para formatar bonito

print("Arquivo 'pessoa.json' criado!")

with open('pessoa.json', 'r', encoding='utf-8') as f:
    dados_lidos = json.load(f)

print("\nDados lidos do JSON:")
print(dados_lidos)