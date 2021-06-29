#################################################################
#               - Cotação Dolar com Selenium -                  #
#                   Arquivo robot.py                            #
#                   Lucas Arneiro Vieira                        #
#                       29/06/2021                              #
#################################################################

#################################################################
#                                                               #
#                           Bibliotecas                         #
#                                                               #
#################################################################

import time
import os
import re
import datetime
import pandas as pd
import sys
from pathlib import Path
import numpy as np

from calendar import monthrange

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException, ElementClickInterceptedException, StaleElementReferenceException

#################################################################
#                                                               #
#                         Configurações                         #
#                                                               #
#################################################################

# Locating webdriver
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
# Configuracoes basicas do robo
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')

# Data de hoje
hoje = datetime.date.today()
# Mes atual
mes = hoje.month
# Ano atual
ano = hoje.year
# Mes passado
mes_passado = mes - 1
# Se o mes atual for Janeiro é preciso pegar dezembro do ano passado
if mes == 1:
    ano = ano -1
# Metodo monthrange() serve para pegar o dia da semana do primeiro dia do mês daquele ano + o numero de dias do mes especificado    
# Ex: print(calendar.monthrange(2016,5)) - (6, 31), ou seja (sexta, com 31 dias no mes)
mes_curr, dias_curr = monthrange(ano, mes_passado)
# Criar uma lista de valores com os dias do mes. Do dia 1 ao 31
dias_ = np.arange(1, dias_curr+1)

#################################################################
#                                                               #
#                         Execução                              #
#                                                               #
#################################################################

def Cotacao_dolar():
    '''Função responsável por entrar no site do Banco Central, abrir o Conversor de Moedas, coletar todas as cotações de todos os dias do mês anterior e armazenar em um arquivo excel .xlsx'''
    driver.get('https://www.bcb.gov.br/')

    # Instanciar a classe que irá esperar até 5 segundos
    wait = WebDriverWait(driver, 15)

    # Abrir "Ver todas as moedas"
    element = driver.find_element_by_xpath('//*[@id="home"]/div/div[1]/div[2]/div/conversormoedas/div[2]/a')
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)

    # Clicar no icone das setas
    setas = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-root/main/dynamic-comp/div/bcb-pagina-tipo0/div/bcb-pagina-tipo4/div[2]/div/dynamic-comp/div/div/bcb-detalhesconversor/div/div[1]/form/div[2]/div[3]/div/button')))
    setas = driver.find_element_by_xpath('/html/body/app-root/app-root/main/dynamic-comp/div/bcb-pagina-tipo0/div/bcb-pagina-tipo4/div[2]/div/dynamic-comp/div/div/bcb-detalhesconversor/div/div[1]/form/div[2]/div[3]/div/button').click()

    conv = []
    for i in range(len(dias_)):
        #print(dias_[i])
        
    # Selecionar datas
        try:
            sel_datas = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-root/main/dynamic-comp/div/bcb-pagina-tipo0/div/bcb-pagina-tipo4/div[2]/div/dynamic-comp/div/div/bcb-detalhesconversor/div/div[1]/form/div[1]/div/input[2]')))
            #Apagar a data presente
            apagar_data = driver.find_element_by_name('inputDate').send_keys(Keys.CONTROL, 'a')
            apagar_data = driver.find_element_by_name('inputDate').send_keys(Keys.BACKSPACE)

            enviar_data = driver.find_element_by_name('inputDate').send_keys(int(dias_[i]))
            enviar_mes = driver.find_element_by_name('inputDate').send_keys(mes_curr)
            enviar_ano = driver.find_element_by_name('inputDate').send_keys(ano)

            time.sleep(2)

            # Clicar no icone das setas
            setas = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-root/main/dynamic-comp/div/bcb-pagina-tipo0/div/bcb-pagina-tipo4/div[2]/div/dynamic-comp/div/div/bcb-detalhesconversor/div/div[1]/form/div[2]/div[3]/div/button')))
            setas = driver.find_element_by_xpath('/html/body/app-root/app-root/main/dynamic-comp/div/bcb-pagina-tipo0/div/bcb-pagina-tipo4/div[2]/div/dynamic-comp/div/div/bcb-detalhesconversor/div/div[1]/form/div[2]/div[3]/div/button').click()
            setas = driver.find_element_by_xpath('/html/body/app-root/app-root/main/dynamic-comp/div/bcb-pagina-tipo0/div/bcb-pagina-tipo4/div[2]/div/dynamic-comp/div/div/bcb-detalhesconversor/div/div[1]/form/div[2]/div[3]/div/button').click()

            # Pegar a conversao
            conversao = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-root/main/dynamic-comp/div/bcb-pagina-tipo0/div/bcb-pagina-tipo4/div[2]/div/dynamic-comp/div/div/bcb-detalhesconversor/div/div[2]/div/div[1]/div[2]/div')))
            conversao = driver.find_element_by_xpath('/html/body/app-root/app-root/main/dynamic-comp/div/bcb-pagina-tipo0/div/bcb-pagina-tipo4/div[2]/div/dynamic-comp/div/div/bcb-detalhesconversor/div/div[2]/div/div[1]/div[2]/div')
            enviar_ano = driver.find_element_by_name('inputDate').send_keys(ano)
            conversa_total = re.search(r"conversão: (\d+,\d+)?", conversao.text).group(1)  # Nome do aluno
            conv.append([str(int(dias_[i]))+ '/' + str(mes_curr)+ '/' + str(ano), conversa_total])

            # clicar no 'reload'
            reload = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-root/main/dynamic-comp/div/bcb-pagina-tipo0/div/bcb-pagina-tipo4/div[2]/div/dynamic-comp/div/div/bcb-detalhesconversor/div/div[1]/form/div[2]/div[5]/div/button')))
            reload = driver.find_element_by_xpath('/html/body/app-root/app-root/main/dynamic-comp/div/bcb-pagina-tipo0/div/bcb-pagina-tipo4/div[2]/div/dynamic-comp/div/div/bcb-detalhesconversor/div/div[1]/form/div[2]/div[5]/div/button').click()

        except (WebDriverException, NoSuchElementException, TimeoutException, ElementClickInterceptedException, StaleElementReferenceException)  as e :
            driver.quit()
            sys.exit("Error message")

    driver.close()

    # Lista de datas e valores
    datas = [conv[i][0] for i in range(len(conv))]
    valores = [conv[i][1] for i in range(len(conv))]

    # Dataframe das Datas e Valores
    df = pd.DataFrame(list(zip(datas,valores)), columns=['DATAS', 'VALORES'])
    df.to_excel('Valores.xlsx', index=False, header=True)