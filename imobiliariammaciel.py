from bs4 import BeautifulSoup
import requests
import json
import time
import random

HEADERS = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 OPR/68.0.3618.63',
    'referer': 'https://www.imobiliariamaciel.com.br/resultado-de-busca/?q=%%7B%22action%22%3A%22pesquisar%22%2C%22contrato%22%3A%22locacao%22%2C%22tipo%22%3A%22todos%22%2C%22cidade%22%3A%22sao-jose-dos-campos%22%2C%22regiao%22%3A%22todos%22%2C%22regiao_layout%22%3A%22combo%22%2C%22bairro_layout%22%3A%22combo%22%2C%22valor_de%22%3A0%2C%22valor_ate%22%3A0%2C%22pagina%22%3A1%7D',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1'
}
base_url = 'https://www.imobiliariamaciel.com.br'
url = base_url+'''/resultado-de-busca/?q=%%7B%%22action%%22%%3A%%22pesquisar%%22%%2C%%22contrato%%22%%3A%%22locacao%%22%%2C%%22tipo%%22%%3A%%22todos%%22%%2C%%22cidade%%22%%3A%%22sao-jose-dos-campos%%22%%2C%%22regiao%%22%%3A%%22todos%%22%%2C%%22regiao_layout%%22%%3A%%22combo%%22%%2C%%22bairro_layout%%22%%3A%%22combo%%22%%2C%%22valor_de%%22%%3A0%%2C%%22valor_ate%%22%%3A0%%2C%%22pagina%%22%%3A1%%7D'''
page = 1
site = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(site.content, features="html.parser")

elements = soup.find_all('div', {'class': 'elementor-top-column'})
for elm in elements:
    sections = elm.find_all('section')
    if len(sections)>0:
        t = sections[0].find('div', {'class': 'cidade-imovel'})
        if t:
            print (t.find('div').text)