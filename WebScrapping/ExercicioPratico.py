import requests
from bs4 import BeautifulSoup


url = 'http://books.toscrape.com'
agent = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers = agent)
soup = BeautifulSoup(response.text, 'html.parser')

livros = soup.find_all('article', class_="product_pod")



for livro in livros:

        titulo = livro.h3.a['title']
        preco = livro.find('p', class_='p-ice_color').text
        print(f"Título: {titulo} || Preço: {preco}")