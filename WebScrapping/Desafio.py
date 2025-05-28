import requests
from bs4 import BeautifulSoup



url = "https://www.bbc.com/"
response = requests.get(url)
html= response.text
soup = BeautifulSoup(html, 'html.parser')

noticias = soup.find_all('a', class_="sc-8a623a54-0 hMvGwj")

for noticia in noticias:
    link = noticia.get('href')

    print(link)
    titulo = soup.find('h2', class_= "sc-9d830f2a-3 fWzToZ")
    print(titulo.text.strip())





