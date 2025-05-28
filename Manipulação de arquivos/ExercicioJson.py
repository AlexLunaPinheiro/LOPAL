import json

dados = {"nome": "João",
         "idade":25
         }

with open("dados.json", "w",encoding="utf-8") as arquivo:
    json.dump(dados, arquivo)

with open("dados.json", "r") as arquivo:
    data = json.load(arquivo)
    for chave, valor in data.items():
        print(f"{chave}: {valor}")
