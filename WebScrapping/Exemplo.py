import requests
from bs4 import BeautifulSoup


url = "https://www.python.org/"
response = requests.get(url)
html= response.text
soup = BeautifulSoup(html, 'html.parser')

texto = soup.find_all('body')

for txt in texto:
    if txt.text.strip() == "Python Events":
        print(txt.text.strip())


