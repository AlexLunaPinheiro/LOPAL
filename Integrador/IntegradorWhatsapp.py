import csv
import pandas as pd
import pywhatkit as kit
from datetime import date
import phonenumbers

#IMPORTAÇÕES DE BIBLIOTECAS

while True:
    codigoPais = input("Digite o código de telefone do país: +")
    if len(codigoPais) == 2:
        ddd = input("Digite o DDD: ")
        if len(ddd) == 2:
            numero = input("Digite o seu número de telefone: (somente números)")
            if len(numero) == 9 and numero.isnumeric():
                break
            else:
                print("Digite um número válido! (ex: 982222134)")
        else:
            print("Digite um ddd válido! (ex: 19)")
    else:
        print("Digite um código de país válido! (ex: 55)")


numeroTelefone = f"+{codigoPais}{ddd}{numero}"
parsed_number = phonenumbers.parse(numeroTelefone, "BR")
numeroConvertido = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)




dataAtual = date.today()#Recebe o dia atual
dataTexto = dataAtual.strftime('%Y-%m-%d')#Converte a data na formatação que quero
contador = 0 #inica o contador de linhas do documento csv
linhas = [] #Cria um array vazio que posteriormente vai receber os índices das linhas com datas iguais a de hoje
mensagemFinal="" #inica a váriavel que irá receber a mensagem final

reader = pd.read_csv('Esp32_Receiver - Sheet1.csv')#Lê o documento csv com o pandas e o atribui na variável reader

#Percorre as linhas na coluna "Date" e adiciona no array caso o valor da linha seja igual ao do dia atual
for item in reader['Data']:
    contador +=1
    dataRelatorio = str(item)

    if dataRelatorio == dataTexto:
        linhas.append(contador)


for linhaComDataAtual in linhas:
    esteiraValores = []
    with open('Esp32_Receiver - Sheet1.csv', 'r') as arquivoCsv:
        leitorCsv = csv.reader(arquivoCsv)
        linhaEspecifica = linhaComDataAtual


        for _ in range(linhaEspecifica):
            next(leitorCsv)


        linha = next(leitorCsv)

        for i in range (2,5):
            esteiraValores.append(linha[i])

        horario = linha[1]


    textos = []
    contador =0

    for valor in esteiraValores:
        contador += 1
        if valor == "1":
            textos.append(f"Esteira {contador}: 🔴")
        elif valor == "2":
            textos.append(f"Esteira {contador}: 🟡")
        else:
            textos.append(f"Esteira {contador}: 🟢")



    juncaoTextos = ""
    for texto in textos:
        juncaoTextos += texto

    mensagem = f"Estoque em {dataRelatorio} às {horario} - {juncaoTextos}"
    mensagemFinal += f"\n{mensagem}"






try :
    kit.sendwhatmsg_instantly(numeroConvertido, mensagemFinal)
    print ( "Mensagem agendada com sucesso!" )
except Exception as e:
    print ( f"Ocorreu um erro: {e} " )
