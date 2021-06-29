# CotacaoDolar
## Este projeto consiste em:

1- Abrir o site https://www.bcb.gov.br/

2- Ir para a seção de Conversão de Moedas

3-Recuperar o valor da cotação de Dolar (“Resultado da conversão”) para todos os dias do mês anterior

4- Salvar datas e valores em um arquivo Excel .xlsx

5- Criar, abrir, escrever e fechar um arquivo log.txt com "Inicio de Execução" + Hora e Data Atual + Valor mínimo, médio e máximo das cotações +  "Final da Execução" + Hora e Data Atual


## Este projeto foi feito com:

- Python 3 -- versão 3.9.5;

- Sistema Operacional Windows 10;

- Com IDE Visual Code Studio;

- Bibliotecas Python do pacote requirements.txt;


## Arquivos do Projeto:

1- Arquivo **robot.py** que fará todos os passos de automação do site até exportação do arquivo;

2- Arquivo **main.py** onde importamos as principais bibliotecas que iremos trabalhar e nosso modulo **robot.py**;

3- Planilha **Valores.xlsx** com coluna de DATA E VALORES das cotações;

4- Arquivo **log.txt** com dados data e hora do Inicio e Final do projeto;

5- Arquivo **chromedriver.exe** para executar o selenium no navegador Chrome



*OBS:
Este código ainda não está completo. Faltam :

- Coletar as cotações de forma completa, algumas estão buscando os valores de proporção;
- Calcular a media do pandas.core.series.Series
