from urllib.parse import urlencode
import requests
import json
import time
import random

from bs4 import BeautifulSoup


base_url = 'http://www.geracaoimoveis.com.br'
url = base_url+'/pesquisa-de-imoveis/locacao_venda=L&id_cidade[]=1&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=&&pag='
page = 1
content = []

site = requests.get(url+str(page))
soup = BeautifulSoup(site.content, features="html.parser")
total_tag = soup.find('p', {'class': 'titulo_res_busca'})
total_label = total_tag.text.strip().replace(' imóveis encontrados', '')
total = int(total_label)/16
if int(total_label)%16 > 1:
    total += 1
print('Total de páginas: ', int(total))
while page <= int(total):
    itens = soup.find_all('div', {'class': 'item'})
    print(url+str(page))
    for i in itens:
        j_dump = {}
        caracteristicas = {}

        infos = i.find('div', {'class': 'info'})
        bairro = infos.find('small')
        link = infos.find('a')
        price = i.find('div', {'class': 'price'})
        valor = price.find('span')
        descricao = infos.find('p', {'class': 'corta_desc'})
        if descricao:
            desc = descricao.text.strip()
        else:
            desc = ''
        amenities = infos.find('ul', {'class': 'amenities'})

        if amenities:
            for a in amenities.find_all('li'):
                area = a.find('i', {'class': 'icon-area'})
                if area:
                    caracteristicas['area'] = a.text
                bedrooms = a.find('i', {'class': 'icon-bedrooms'})
                if bedrooms:
                    caracteristicas['quartos'] = a.text
                bathrooms = a.find('i', {'class': 'icon-bathrooms'})
                if bathrooms:
                    caracteristicas['banheiros'] = a.text

        j_dump['bairro'] = bairro.text.strip()
        j_dump['valor'] = valor.text.strip()
        j_dump['titulo'] = link['title']
        j_dump['descricao'] = desc
        j_dump['link'] = base_url+'/'+link['href']
        j_dump['caracteristicas'] = caracteristicas
        content.append(j_dump)
    with open("geracaoimoveis.json", "w", encoding='utf8') as outfile:
        outfile.write(json.dumps(content,indent=4, ensure_ascii=False))

    delay = random.randint(1,8)
    time.sleep(delay)
    page += 1
    site = requests.get(url+str(page))
    soup = BeautifulSoup(site.content, features="html.parser")
