from bs4 import BeautifulSoup
import requests
import json
import time
import random

base_url = 'https://www.grupokaza.com.br'
url = base_url+'''/pesquisa-de-imoveis/busca_free=alugar+s%E3o+jos%E9+dos+campos&&pag='''
page = 1
site = requests.get(url+str(page))
content = []
BANHEIRO = 'fa-shower'
GARAGEM = 'fa-car'
QUARTO = 'fa-bed'
AREA = 'fa-compress'
soup = BeautifulSoup(site.content, features="html.parser")
total_tag = soup.find('h2', {'class': 'title-res-busca'})
total_label = total_tag.text.strip().replace(' imóveis encontrados', '')
total = int(total_label)/16
if int(total_label)%16 > 1:
    total += 1
print('Total de páginas: ', int(total))
while page <= int(total):
    conteudo = soup.find_all('div', {'class': 'single_properties'})
    print(url+str(page))
    for cont in conteudo:
        j_dump = {}
        caracteristicas = {}

        link = cont.find('a', {'class': 'link-imov'})
        
        div = cont.find('div', {'class': "property_details"})
        descricao = cont.find('div', {'class': 'property_details_desc'})
        thumbs = cont.find('ul', {'class':'itens-imo-thumb'})
        
        if descricao:
            desc = descricao.find('p').text.replace('\n', ' ')
        else:
            desc = '(Sem descrição)'
        valor = div.find('h4')
        div.find('span').find('strong').decompose()
        if '(V)' in valor.text and '(L)' not in valor.text:            
            continue
        for br in div:
            br.extract()

        banho = thumbs.find('i', {'class': BANHEIRO})        
        if banho:
            caracteristicas['banheiros'] = banho.next_sibling
        quartos = thumbs.find('i', {'class': QUARTO})
        if quartos:
            caracteristicas['quartos'] = quartos.next_sibling
        garagem = thumbs.find('i', {'class': GARAGEM})
        if garagem:
            caracteristicas['garagem'] = garagem.next_sibling
        area = thumbs.find('i', {'class': AREA})
        if area:
            caracteristicas['area'] = area.next_sibling
        
        j_dump['titulo'] = link['title']
        j_dump['descricao'] = desc
        j_dump['valor'] = valor.text.strip()
        j_dump['bairro'] = div.find('span').text.strip()
        j_dump['link'] = base_url+'/'+link['href']
        j_dump['caracteristicas'] = caracteristicas
        content.append(j_dump)
    with open("grupokaza.json", "w", encoding='utf8') as outfile:
        outfile.write(json.dumps(content,indent=4, ensure_ascii=False))

    delay = random.randint(1,8)
    time.sleep(delay)   
    page += 1
    site = requests.get(url+str(page))
    soup = BeautifulSoup(site.content, features="html.parser")
    
            
