import csv
import pandas as pd
import pywhatkit as kit
from datetime import date
#IMPORTAÇÕES DE BIBLIOTECAS


dataAtual = date.today()#Recebe o dia atual
dataTexto = dataAtual.strftime('%Y/%m/%d')#Converte a data na formatação que quero
contador = 0 #inica o contador de linhas do documento csv
linhas = [] #Cria um array vazio que posteriormente vai receber os índices das linhas com datas iguais a de hoje
mensagemFinal="" #inica a váriavel que irá receber a mensagem final

reader = pd.read_csv('LOPAL-ProjetoIntegrador-Esp8266_Receiver (1).csv')#Lê o documento csv com o pandas e o atribui na variável reader

#Percorre as linhas na coluna "Date" e adiciona no array caso o valor da linha seja igual ao do dia atual
for item in reader['Date']:
    contador +=1
    dataRelatorio = str(item)
    if dataRelatorio == dataTexto:
        linhas.append(contador)

#
for linhaComDataAtual in linhas:
    esteiraValores = []
    with open('LOPAL-ProjetoIntegrador-Esp8266_Receiver (1).csv', 'r') as arquivoCsv:
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



phoneNumber = "+55 19 99972-0938"
try :
    kit.sendwhatmsg_instantly(phoneNumber, mensagemFinal)
    print ( "Mensagem agendada com sucesso!" )
except Exception as e:
    print ( f"Ocorreu um erro: {e} " )
