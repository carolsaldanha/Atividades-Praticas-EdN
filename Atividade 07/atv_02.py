import pandas as pd

data = {'Nome': ['Ana', 'Bruno'], 'Idade': [28, 35], 'Cidade': ['São Paulo', 'Rio']}

pd.DataFrame(data).to_csv('pessoas.csv', index=False)

print("Arquivo 'pessoas.csv' criado!")