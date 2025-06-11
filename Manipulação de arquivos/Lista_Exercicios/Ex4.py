import pandas as pd

df = pd.read_csv("Criptografado.txt",encoding="utf-8")
texto = ""
for r in df:
    texto += r
alfabeto = ["abcdefghijklmnopqrstuvwxyz"]

def descriptografar(texto):


        resultado = ""

        for letra in texto:
            if letra.lower() in alfabeto:
                letraMinuscula = letra.lower()
                posicao = alfabeto.index(letraMinuscula)
                novaPosicao = (posicao - 3) % 26 #Encontra a posição da letra mas volta à primeira letra do alfabeto caso saia do indice da lista
                novaLetra = alfabeto[novaPosicao]


                if letra.isupper():
                    resultado += novaLetra.upper()
                else:
                    resultado += novaLetra
            else:
                resultado += letra

        return resultado

print(descriptografar(texto))