import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url).json()
    
    if "erro" in resposta:
        print("CEP não encontrado.")
        return

    print("Logradouro:", resposta.get("logradouro"))
    print("Bairro:", resposta.get("bairro"))
    print("Cidade:", resposta.get("localidade"))
    print("Estado:", resposta.get("uf"))

cep_usuario = input("Digite o CEP (somente números): ")
consultar_cep(cep_usuario)
