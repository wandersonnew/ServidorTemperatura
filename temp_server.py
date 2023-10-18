import requests
from bs4 import BeautifulSoup

# retorna a temperatura
def getTemp():
    # url do site que se deseja fazer scraping
    url = 'http://10.10.10.201:8080/index.html'

    # pegar o agente do browser (forma genérica)
    agent = requests.get('https://www.google.com/')

    site = requests.get(url, headers=agent.request.headers)

    soup = BeautifulSoup(site.content, 'html.parser')

    items = soup.find_all('tr')[2]

    dados = []

    # Para acessar os dados dentro das tags <font>
    for td in items.find_all('td'):
        font = td.find('font')
        if font is not None:
            dados.append(font.get_text())
    
    return dados