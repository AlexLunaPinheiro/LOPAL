import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook


titulos = []
links = []
chaves =['titulo', 'link']
valores = [titulos,links]
tabela ={}



url = "https://www.cnnbrasil.com.br/"
response = requests.get(url)
html= response.text
soup = BeautifulSoup(html, 'html.parser')

noticias = soup.find_all('li', class_="block__news__item block__news__item--manchetes")

for noticia in noticias:

    link = noticia.figcaption.a['href']
    links.append(link)
    titulo = noticia.figcaption.a.h3.text
    titulos.append(titulo)


for i in range(len(chaves)):
    tabela[chaves[i]] = valores[i]

print(tabela)

workbook = Workbook()
sheet = workbook.active
sheet.append(["titulo","link"])
for chave, valor in tabela.items():

    for i in valor:
        sheet.append([i])



workbook.save("tabela.xlsx")



