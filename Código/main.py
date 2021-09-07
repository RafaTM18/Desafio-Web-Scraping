# Importação para entrada de params
import sys

# Importação para criação e verificação de pastas
from os import path
from os import mkdir

# Importação de utilitários
import pandas as pd

# Importação para requests
from urllib.request import urlopen, Request
# Importação de tratamento de erros
from urllib.error import URLError, HTTPError

# Importação para realização de operações no HTML
from bs4 import BeautifulSoup
# Importação para automatizar o site
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def tratando_html(input):
    return " ".join(input.split()).replace('> <', '><')

def get_soup_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}

    req = Request(url, headers = headers)
    response = urlopen(req).read()
    
    html = response.decode('utf-8')
    html = tratando_html(html)
    
    soup = BeautifulSoup(html,'html.parser')

    return soup

def remove_subpath(url):
    index = url.rfind('/', 0, url.rfind('/'))
    return url[:index]

def get_top_acoes():
    url = 'https://br.investing.com/'

    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")

    driver = webdriver.Chrome(options=options, executable_path='../chromedriver.exe')

    driver.get(url)

    accept_btn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
    )

    accept_btn.click()
    
    input_pesquisa = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.TAG_NAME, "input"))
    )
    input_pesquisa.click()
    
    list_pesquisa = driver.find_element_by_css_selector('.js-group-template.textBox')
    html = list_pesquisa.get_attribute('innerHTML')
    driver.quit()

    acoes_populares = BeautifulSoup(html, 'html.parser')
    list_acoes = acoes_populares.find_all('a')

    list_urls = []
    for acao in list_acoes:
        list_urls.append(url[:-1] + acao.get('href'))

    return list_urls

def main():
    if(len(sys.argv) < 2):
        print('Númeroos de parâmetros inválidos.\nUtilize o formato: py main.py <lista de links>\nOu esse formato: py main.py top')
        return
    elif(sys.argv[1] == 'top' and len(sys.argv) == 2):
        list_urls = get_top_acoes()
    else:
        list_urls = sys.argv[1:]

    for url in list_urls:
        try:
            if(not url.endswith('historical-data')):
                pag_inicial = get_soup_html(url)

                link_hist = pag_inicial.find('a', text="Dados Históricos")
                url_hist = link_hist.get('href')

                pag_hist = get_soup_html(remove_subpath(url) + url_hist)
            else:
                pag_hist = get_soup_html(url)

            nome_table = pag_hist.find('h2')
            nome_table = nome_table.get_text().split(' ')[0]

            table_hist = pag_hist.find('table', {'id': 'curr_table'})
            df = pd.read_html(table_hist.prettify(), decimal='.', thousands='')[0]

            print(f'{nome_table}\n{df}\n')

            if(not path.exists('../output')):
                mkdir('../output')

            df.to_csv(f'../output/{nome_table}.csv', sep=';', index=False, encoding='utf-8')
            
        except HTTPError as e:
            print(f'Houve um erro!\nCódigo do erro: {e.status} - Motivo do erro: {e.reason}')
            
        except URLError as e:
            print(f'Houve um erro!\nMotivo do erro: {e.reason}')

        except Exception as e:
            print(f'Houve um erro desconhecido! {e}')

if __name__ == "__main__":
    main()