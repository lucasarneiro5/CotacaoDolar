#################################################################
#               - Cotação Dolar com Selenium -                  #
#                   Lucas Arneiro Vieira                        #
#                       25/06/2021                              #
#################################################################


import numpy as np
import pandas as pd
import sys
import datetime
import time
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

# Instanciar a classe que irá esperar até 5 segundos
wait = WebDriverWait(driver, 15)

# Data de hoje
hoje = datetime.date.today()
# Data atual e hora
#data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
# Mes atual
mes = hoje.month
# Ano atual
ano = hoje.year
# Mes passado
mes_passado = mes - 1
# Se o mes atual for Janeiro é preciso pegar dezembro do ano passado
if mes == 1:
    ano = ano -1
mes_curr, dias_curr = monthrange(ano, mes_passado)
dias_ = np.arange(1, dias_curr+1)

#################################################################
#                                                               #
#                         Execução                               #
#                                                               #
#################################################################

# Inicio da execução
print('\nInicio da execução: \n')
driver.get('https://www.bcb.gov.br/')
time.sleep(3)
element = driver.find_element_by_xpath('//*[@id="home"]/div/div[1]/div[2]/div/conversormoedas/div[2]/a')
driver.execute_script("arguments[0].click();", element)
time.sleep(1)

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

        # Pegar a conversao
        conversao = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-root/main/dynamic-comp/div/bcb-pagina-tipo0/div/bcb-pagina-tipo4/div[2]/div/dynamic-comp/div/div/bcb-detalhesconversor/div/div[2]/div/div[1]/div[2]/div')))
        conversao = driver.find_element_by_xpath('/html/body/app-root/app-root/main/dynamic-comp/div/bcb-pagina-tipo0/div/bcb-pagina-tipo4/div[2]/div/dynamic-comp/div/div/bcb-detalhesconversor/div/div[2]/div/div[1]/div[2]/div')
        conv.append(conversao.text)

        # clicar no 'reload'
        reload = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-root/main/dynamic-comp/div/bcb-pagina-tipo0/div/bcb-pagina-tipo4/div[2]/div/dynamic-comp/div/div/bcb-detalhesconversor/div/div[1]/form/div[2]/div[5]/div/button')))
        reload = driver.find_element_by_xpath('/html/body/app-root/app-root/main/dynamic-comp/div/bcb-pagina-tipo0/div/bcb-pagina-tipo4/div[2]/div/dynamic-comp/div/div/bcb-detalhesconversor/div/div[1]/form/div[2]/div[5]/div/button').click()

    except (WebDriverException, NoSuchElementException, TimeoutException, ElementClickInterceptedException, StaleElementReferenceException)  as e :
        driver.quit()
        sys.exit("Error message")



# Fim da Execução
print('\n**Lista com data e cotação: ', conv)
print('\nFim da Execução - ')




