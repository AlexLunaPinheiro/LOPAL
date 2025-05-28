import requests
from bs4 import BeautifulSoup


url = "https://www.python.org/"
response = requests.get(url)
html= response.text
soup = BeautifulSoup(html, 'html.parser')

texto = soup.getText()


for txt in texto:
    print(txt.text.strip() )

with open('texto.txt','w',encoding='utf-8') as f:

    for txt in texto:
        f.write(txt.text.strip() + '\n')



