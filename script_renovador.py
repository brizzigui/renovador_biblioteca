from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

import time
from time import gmtime, strftime

import os
import getpass

usuario = os.environ['USER']
senha = os.environ['SENHA']


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-setuid-sandbox')
chrome_options.add_argument('--remote-debugging-port=9222')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('start-maximized')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://portal.ufsm.br/biblioteca/login.html")

campo_usuario = driver.find_element(By.XPATH, '//*[@id="login"]')
campo_senha = driver.find_element(By.XPATH, '//*[@id="senha"]')

campo_usuario.send_keys(f"{usuario}")
campo_senha.send_keys(f"{senha}")
campo_senha.send_keys(Keys.RETURN)

pagina_renovacao = driver.find_element(By.XPATH, '//*[@id="app_top"]/nav/div/ul/li[4]/a')
pagina_renovacao.click()

data_atual = strftime("%d/%m/%Y", time.localtime())


numero_de_livros = 0
try:
    while True:
        data_limite = driver.find_element(By.XPATH, f'//*[@id="emprestimos"]/tbody/tr[{numero_de_livros+1}]/td[6]').text
        numero_de_livros += 1

except NoSuchElementException:
    print(f"Número de livros: {numero_de_livros}")


for i in range(numero_de_livros):



    titulo = driver.find_element(By.XPATH, f'//*[@id="emprestimos"]/tbody/tr[{i+1}]/td[3]').text
    qnt_renovacoes = int(driver.find_element(By.XPATH, f'//*[@id="emprestimos"]/tbody/tr[{i+1}]/td[7]').text)
    data_limite = driver.find_element(By.XPATH, f'//*[@id="emprestimos"]/tbody/tr[{i+1}]/td[6]').text
      
    print("")
    print(f"Livro: {titulo}")
    print(f"Data limite: {data_limite}")
    print(f"Data atual: {data_atual}")
    print(f"Quantidade de renovações: {qnt_renovacoes}")

    if qnt_renovacoes >= 13:
        raise Exception(f'Impossível renovar livro "{titulo}": surpassa quantia máxima de renovações')

    elif data_atual == data_limite:
        botao_renovacao = driver.find_element(By.XPATH, f'//*[@id="emprestimos"]/tbody/tr[{i+1}]/td[1]/button')
        botao_renovacao.click()
        print(f'Livro "{titulo}" renovado')

    else:
        print(f'Livro "{titulo}" não foi renovado (está antes ou depois do prazo)')

driver.quit()
