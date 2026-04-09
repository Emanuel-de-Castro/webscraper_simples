import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

dados_vagas = []

pagina = requests.get('https://realpython.github.io/fake-jobs/', headers=headers, verify=False)
dados_pagina = BeautifulSoup(pagina.text, 'html.parser')


todas_vagas = dados_pagina.find(id="ResultsContainer")
vagas_python = todas_vagas.find_all('div', class_="card-content")

# Apenas seleciona os cartões que são referentes a vagas de Python
vagas_filtradas = [
                card
                for card in vagas_python
                if "python" in card.find('h2', class_="title is-5").text.lower()]

for div in vagas_filtradas:
    nome_vaga = div.find('h2', class_="title is-5").text.strip()
    nome_empresa = div.find('h3', class_="subtitle is-6 company").text.strip()
    local = div.find('p', class_="location").text.strip()

    data_str = div.find('time')['datetime']
    data = datetime.strptime(data_str, '%Y-%m-%d').strftime('%m/%Y')

    
    links = div.find_all("a")
    if len(links) > 1:  
            link_apply = links[1]["href"]
            url = link_apply
            response_vaga = requests.get(url, headers=headers, verify=False)
            desc_vaga = BeautifulSoup(response_vaga.text, 'html.parser')
            descricao = desc_vaga.find("div", class_="content").find("p").get_text(strip=True)
            descricao = descricao[:200] + "..." if len(descricao) > 200 else descricao
    
    dados_vagas.append({
        'VAGA': nome_vaga,
        'EMPRESA': nome_empresa,
        'LOCAL': local,
        'DATA': data,
        'DESCRICAO': descricao
    })


with open('vagas_python.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
    writer = csv.DictWriter(arquivo_csv, fieldnames=['VAGA', 'EMPRESA', 'LOCAL', 'DATA', 'DESCRICAO'])
    writer.writeheader()
    writer.writerows(dados_vagas)

print(f"✅ Arquivo 'vagas_python.csv' criado com {len(dados_vagas)} vagas!")


