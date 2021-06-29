#################################################################
#               - Cotação Dolar com Selenium -                  #
#                   Arquivo main.py                            #
#                   Lucas Arneiro Vieira                        #
#                       29/06/2021                              #
#################################################################

#################################################################
#                                                               #
#                           Bibliotecas                         #
#                                                               #
#################################################################

import numpy as np
import pandas as pd
from statistics import mean
import sys
import re
from datetime import datetime
import time

# Importar robo
import robot

#################################################################
#                                                               #
#                         Configurações                         #
#                                                               #
#################################################################

# Data atual e hora
data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")

#################################################################
#                                                               #
#                         Execução                              #
#                                                               #
#################################################################

# Inicio da execução
if __name__ == '__main__':
    print('\nInicio da execução: ', data_hora)
    robot.Cotacao_dolar()

    # Lendo dataset e calculando valores
    dataset = pd.read_excel('Valores.xlsx')

    # Transformando a coluna 'VALORES' em lista, numerica, para calculo
    a = dataset['VALORES'].str.replace(',', '.')
    Valores_list = a.tolist()
    cotacao = list(np.float_(a))

    minimo = min(cotacao)
    maximo = max(cotacao)
    media = mean(cotacao)

    # Convertendo variaveis em string
    str_data_hora = repr(data_hora)
    str_min = repr(minimo)
    str_max = repr(maximo)
    str_media = repr(media)
 
    # Escrevendo no arquivo log.txt
    arquivo = open("log.txt", "w")
    arquivo.write("\nInicio da Execucao: "+ str_data_hora + "\n")
    arquivo.write("Valor minimo: " + str_min + "\nValor maximo: "+ str_max + "\nValor Medio: "+ str_media)

    # Marcando Tempo Final
    data_hora_fim = datetime.now().strftime("%d/%m/%Y %H:%M")
    str_data_hora_fim = repr(data_hora_fim)
    arquivo.write("\nFim da Execucao: "+ str_data_hora_fim + "\n")
    str_data_hora_fim = repr(data_hora_fim)
    arquivo.close()


    # Fim da Execução
    print('\nFim da Execução: ', data_hora_fim)




