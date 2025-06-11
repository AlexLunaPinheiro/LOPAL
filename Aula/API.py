import requests


def pegar_cotacao_dolar():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

    try:
        resposta = requests.get(url)
        dados = resposta.json()

        cotacao = float(dados['USDBRL']['bid'])
        print(f"Cotação atual do dólar: R$ {cotacao:.2f}")

    except Exception as e:
        print("Erro ao buscar cotação:", e)


# Executa a função
pegar_cotacao_dolar()
