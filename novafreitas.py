from urllib.parse import urlencode
import requests
import json
import time
import random

from bs4 import BeautifulSoup

url = 'https://www.novafreitas.com.br/imoveis/para-alugar/sao-jose-dos-campos?pagina='
page = 1

site = requests.get(url)
soup = BeautifulSoup(site.content, features="html.parser")

print (soup)
