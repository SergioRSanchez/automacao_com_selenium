""" Vamos importar as bibliotecas que serão necessárias para o projeto """

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

""" Abre o Chrome """

nav = webdriver.Chrome()

""" Entra no site do Google """

nav.get("https://www.google.com/")

"""
Agora devemos digitar cotação Dólar no campo de pesquisa. Usando o
Inspecionar do Chrome, podemos achar o código HTML que representa o campo de
busca, clicamos nele e selecionamos o código, botão direito -> Copy -> Copy
Full XPath. Agora temos o código que indica onde fica nosso campo de pesquisa
do Google.
Agora que temos o código para a posição do campo de busca no site, devemos
explicar para o Selenium que ele irá buscar pelo XPATH e não por outro método,
através do comando find_element_by_xpath. Depois disso, devemos digitar o texto
desejado através do comando .send_keys
"""

nav.find_element_by_xpath(
    "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("cotação dólar")

"""
Depois disso devemos apertar o ENTER no mesmo caminho da busca, para isso
devemos importar from selenium.webdriver.common.keys import Keys
"""

nav.find_element_by_xpath(
    "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(Keys.ENTER)

"""
Após o carregamento da página, usaremos o Inspecionar novamente, para
localizar o valor indicado na imagem da cotação, e copiar o XPATH dele. Depois
colocamos esse valor em uma variável com o comando .get_attribute("data_value")
que nos permite coletar informações.
"""

cotacao_dolar = nav.find_element_by_xpath(
    "//*[@id='knowledge-currency__updatable-data-column']/div[1]/div[2]/span[1]").get_attribute("data-value")


""" Agora vamos pegar a cotação do Euro """

nav.get("https://www.google.com/")
nav.find_element_by_xpath(
    "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("cotação euro")
nav.find_element_by_xpath(
    "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(Keys.ENTER)
cotacao_euro = nav.find_element_by_xpath(
    "//*[@id='knowledge-currency__updatable-data-column']/div[1]/div[2]/span[1]").get_attribute("data-value")


""" E agora a cotação do Ouro """

nav.get('https://www.melhorcambio.com/')

"""
Os comandos abaixo eram para o caso de abrir uma nova guia, o que não foi
necessário
aba_original = nav.window_handless[0]
aba_nova = nav.window_handless[1]
nav.switch_to.window(aba_nova)
"""

nav.find_element_by_xpath(
    '//*[@id="contato"]/div/div[2]/div[2]/div[2]/a[1]').click()


cotacao_ouro = nav.find_element_by_xpath(
    '//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(",", ".")

""" Fechamos o navegador """

nav.quit()

"""
Imprimimos todas as cotações para checar se os valores foram obtidos
corretamente
"""

print(f"\nA cotação do Dólar hoje é R$ {cotacao_dolar}.")
print(f"A cotação do Euro hoje é R$ {cotacao_euro}.")
print(f"A cotação da grama de Ouro hoje é R$ {cotacao_ouro}.")
