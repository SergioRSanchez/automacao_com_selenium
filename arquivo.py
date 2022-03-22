from selenium import webdriver
from selenium.webdriver.common.keys import Keys

""" Abre o Chrome """
nav = webdriver.Chrome()

""" Entra no site do Google """
nav.get("https://www.google.com/")

""" Agora devemos digitar cotação dólar no campo de pesquisa. Usando o
Inspecionar do Chrome, podemos achar o código HTML que representa o campo de
busca, clicamos nele e selecionamos o código, botão direito -> Copy -> Copy
Full XPath. Agora temos o código que indica onde fica nosso campo de pesquisa
do Google.
Agora que temos o código para a posição do campo de busca no site, devemos
explicar para o Selenium que ele irá buscar pelo XPATH e não por outro método,
através do comando find_element_by_xpath. Depois disso, devemos digitar o texto
desejado através do comando .send_keys """
nav.find_element_by_xpath(
    "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("cotação dólar")

""" Depois disso devemos apertar o ENTER no mesmo caminho da busca, para isso
devemos importar from selenium.webdriver.common.keys import Keys """
nav.find_element_by_xpath(
    "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(Keys.ENTER)

""" Após o carregamento da página, usaremos o Inspecionar novamente, para
localizar o valor indicado na imagem da cotação, e copiar o XPATH dele. Depois
colocamos esse valor em uma variável com o comando .get_attribute("data_value")
que nos permite coletar informações. """
cotacao = nav.find_element_by_xpath(
    "/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[3]/div[1]/div[1]/div[2]/span[1]").get_attribute("data-value")

""" "Imprimimos" a variável com o valor da cotação atual """
print(cotacao)
