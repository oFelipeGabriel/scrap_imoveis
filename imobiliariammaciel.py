from urllib.parse import urlencode
import requests
import json
import time
import random

from bs4 import BeautifulSoup

query_string = {
    "action":"pesquisar",
    "contrato":"locacao",
    "tipo":"todos",
    "cidade":"sao-jose-dos-campos",
    "regiao":"todos",
    "regiao_layout":"combo",
    "bairro_layout":"combo",
    "valor_de":0,
    "valor_ate":0,
    "pagina":2
}

base_url = 'https://www.imobiliariamaciel.com.br'
url = base_url+'''/resultado-de-busca/?q='''+urlencode(query_string)
page = 1
query_string['pagina'] = None
header_url = base_url+'''/resultado-de-busca/?q='''+urlencode(query_string)
HEADERS = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 OPR/68.0.3618.63',
    'path': url,
    'referer': header_url,
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1'
}
site = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(site.content, features="html.parser")

elements = soup.find_all('div', {'class': 'elementor-top-column'})
for elm in elements:
    sections = elm.find_all('section')
    if len(sections)>0:
        t = sections[0].find('div', {'class': 'cidade-imovel'})
        if t:
            print (t.find('div').text)
