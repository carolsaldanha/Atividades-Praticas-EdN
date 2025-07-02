import requests

def consultar_cotacao(moeda):
    moeda = moeda.upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url).json()
    
    chave = moeda + "BRL"
    if chave not in resposta:
        print("Moeda não encontrada.")
        return

    dados = resposta[chave]
    print("Cotação atual:", dados['bid'])
    print("Valor máximo do dia:", dados['high'])
    print("Valor mínimo do dia:", dados['low'])
    print("Data:", dados['create_date'])

moeda_usuario = input("Digite o código da moeda (ex: USD, EUR, GBP): ")
consultar_cotacao(moeda_usuario)
