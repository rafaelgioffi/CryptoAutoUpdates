import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd
import os

bcoin_d = 0.0
bcoin_r = 0.0
ccar_d = 0.0
ccar_r = 0.0
step_d = 0.0
step_r = 0.0

# Opções para não exibir o navegador...
chrome_options = Options()
chrome_options.add_argument("--headless")

inter = int(input('Qual tempo de atualização (em minutos): '))


def cotacao():
    navegador = webdriver.Chrome(executable_path=r'C:\Users\Rafael\chromedriver.exe', chrome_options=chrome_options,
                                 service_log_path='NUL')
    os.system('cls') or None

    navegador.get("https://coinmarketcap.com/currencies/bombcrypto/")
    os.system('cls') or None
    bcoin_d = navegador.find_element(By.XPATH,
                                     '//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[3]/div/div/div/div/div[2]/div[2]/input').get_attribute(
        'value')
    os.system('cls') or None

    navegador.get("https://coinmarketcap.com/pt-br/currencies/bombcrypto/")
    os.system('cls') or None
    bcoin_r = navegador.find_element(By.XPATH,
                                     '//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[3]/div/div/div/div/div[2]/div[2]/input').get_attribute(
        'value')
    # print(f'Valor do BCOIN ==> R${bcoin_r}')
    os.system('cls') or None

    navegador.get('https://coinmarketcap.com/currencies/cryptocars/')
    os.system('cls') or None
    ccar_d = navegador.find_element(By.XPATH,
                                    '//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[3]/div/div/div/div/div[2]/div[2]/input').get_attribute(
        'value')
    # print(f'Valor do CCAR ==> R${ccar_d}')
    os.system('cls') or None

    navegador.get('https://coinmarketcap.com/pt-br/currencies/cryptocars/')
    os.system('cls') or None
    ccar_r = navegador.find_element(By.XPATH,
                                    '//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[3]/div/div/div/div/div[2]/div[2]/input').get_attribute(
        'value')
    # print(f'Valor do CCAR ==> R${ccar_r}')
    os.system('cls') or None

    navegador.get('https://google.com.br')
    os.system('cls') or None
    navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(
        'cotação dólar')
    navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()
    dolar = navegador.find_element(By.XPATH,
                                   '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute(
        'data-value')

    # navegador.get('https://coinmarketcap.com/pt-br/currencies/step-hero/')
    # os.system('cls') or None
    # step_r = navegador.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[3]/div/div/div/div/div[2]/div[2]/input').get_attribute('value')
    # # print(f'Valor do STEP HERO ==> R${step_r}')
    # os.system('cls') or None

    bomb = 'PLANILHA BOMB CRYPTO 2022 Teste.xlsm'
    ccar = 'PLANILHA CCAR 2022.xlsm'

    bcoin_d.replace('.', ',')
    bcoin_d = float(bcoin_d)
    bcoin_r.replace('.', ',')
    bcoin_r = float(bcoin_r)
    ccar_d.replace('.', ',')
    ccar_d = float(ccar_d)
    ccar_r.replace('.', ',')
    ccar_r = float(ccar_r)
    dolar = float(dolar)
    dolar = '{:.2f}'.format(dolar)
    dolar = dolar.replace('.', ',')

    # tabela = pd.read_excel(bomb)
    # tabela = tabela.drop(['Unnamed: 0'], axis=1)
    tabela = {'': ['BCOIN', 'CCAR', 'Dólar'],
              'US$': [bcoin_d, ccar_d, dolar],
              'R$': [bcoin_r, ccar_r, '']}
    dataframe = pd.DataFrame(tabela)
    dataframe.to_excel('Valores.xlsx', index=False)

    for cont in range(inter * 60, -1, -1):
        os.system('cls') or None
        bcoin_d = str(bcoin_d)
        bcoin_d = bcoin_d.replace('.', ',')
        bcoin_r = str(bcoin_r)
        bcoin_r = bcoin_r.replace('.', ',')
        ccar_d = str(ccar_d)
        ccar_d = ccar_d.replace('.', ',')
        ccar_r = str(ccar_r)
        ccar_r = ccar_r.replace('.', ',')
        dolar = str(dolar)
        dolar = dolar.replace('.', ',')
        print('Valores atualizados! Aperte Control + C para interromper o script...')
        print()
        print('########################################################################## ')
        print(f'# BCOIN: US${bcoin_d} (R${bcoin_r})  |  CCAR: US${ccar_d} (R${ccar_r})  |  Dólar: R${dolar}) #')
        print('##########################################################################')
        print()
        print()
        # msg = f'Aguarde {inter} minuto(s)'
        msg = ''
        msg = msg + ('▒' * cont)
        if cont > 60:
            m = int(round(cont / 60, 2))
            s = cont % 60
            print(f'{m}m:{s}s {msg}')
        else:
            print(f'{cont}s {msg}')
        pyautogui.sleep(1)
    os.system('cls') or None
    # navegador.quit()


# msg = f'Aguarde {inter} minuto(s)'

os.system('cls') or None

while True:
    cotacao()
else:
    navegador.quit()

for count in range(t * 60, 1, -1):
    if count > 60:
        m = int(round(count / 60, 2))
        s = count % 60
        print(f'{m}m:{s}s')
    else:
        print(count, 's')
