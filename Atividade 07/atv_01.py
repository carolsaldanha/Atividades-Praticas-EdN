import pandas as pd

df_log = pd.read_csv('log_treinamento.csv')

print(f"Média do tempo: {df_log['tempo_execucao'].mean():.2f}s")
print(f"Desvio padrão do tempo: {df_log['tempo_execucao'].std():.2f}s")