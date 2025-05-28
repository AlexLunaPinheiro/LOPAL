with open("meu_arquivo.txt","w",encoding="utf-8")as arquivo:
        arquivo.write("Olá, mundo!\n")
        arquivo.write("Aprendendo Python\n")
texto = "python"
textoFinal =""
with open("meu_arquivo.txt","r",encoding="utf-8")as arquivo:
        for letra in arquivo.read():
                for n in range(len(texto)):
                        if letra.lower() == texto[n]:
                                textoFinal += letra
contador = 0

while textoFinal.lower() != texto:
        textoFinal.replace(textoFinal[contador],"")
        contador += 1
print(textoFinal)