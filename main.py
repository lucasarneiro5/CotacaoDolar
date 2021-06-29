#################################################################
#               - Cotação Dolar com Selenium -                  #
#                   Arquivo main.py                            #
#                   Lucas Arneiro Vieira                        #
#                       25/06/2021                              #
#################################################################

#################################################################
#                                                               #
#                           Bibliotecas                         #
#                                                               #
#################################################################

import numpy as np
import pandas as pd
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
    minimo = dataset['VALORES'].min()
    maximo = dataset['VALORES'].max()
    #media = dataset['VALORES'].mean()

    # Convertendo variaveis em string
    str_data_hora = repr(data_hora)
    str_min = repr(minimo)
    str_max = repr(maximo)
    # Escrevendo no arquivo log.txt
    arquivo = open("log.txt", "w")
    arquivo.write("Inicio da Execucao: "+ str_data_hora + "\n")
    arquivo.write("Valor minimo: " + str_min + "\nValor maximo: "+ str_max + "\n")
    arquivo.write("Fim da Execucao: "+ str_data_hora + "\n")
    arquivo.close()


    # Fim da Execução
    print('\nFim da Execução: ', data_hora)




