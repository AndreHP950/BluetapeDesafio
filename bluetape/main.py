import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

# Acessar a página inicial do Reclame Aqui
navegador.get("https://www.reclameaqui.com.br/")

# Encontrar o botão "Moda" (ajuste o seletor CSS conforme a estrutura da página)
botao_moda = navegador.find_element(By.CSS_SELECTOR, "button.botao-moda")  

# Clicar no botão
botao_moda.click()

"""
# Encontrar os elementos das listas (ajuste os seletores CSS conforme a estrutura da página)
melhores_empresas = driver.find_elements_by_css_selector("seletor_css_para_as_melhores_empresas")
piores_empresas = driver.find_elements_by_css_selector("seletor_css_para_as_piores_empresas")

# Criar um DataFrame para armazenar os dados
dados = []

# Iterar sobre as empresas e extrair os dados
for empresa in melhores_empresas + piores_empresas:
    # Clicar na empresa para acessar a página de detalhes
    empresa.click()

    # Obter o código fonte da página
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extrair os dados (ajuste os seletores CSS conforme a estrutura da página)
    nota = soup.find("seletor_css_para_a_nota").text
    reclamacoes_respondidas = soup.find("seletor_css_para_reclamacoes_respondidas").text
    voltariam_a_fazer_negocio = soup.find("seletor_css_para_voltariam_a_fazer_negocio").text
    indice_de_solucao = soup.find("seletor_css_para_indice_de_solucao").text
    nota_do_consumidor = soup.find("seletor_css_para_nota_do_consumidor").text

    # Adicionar os dados ao DataFrame
    dados.append([nota, reclamacoes_respondidas, voltariam_a_fazer_negocio, indice_de_solucao, nota_do_consumidor])

    # Voltar para a página inicial
    driver.back()

# Criar o DataFrame
df = pd.DataFrame(dados, columns=["Nota", "Reclamações Respondidas", "Voltariam a Fazer Negócio", "Índice de Solução", "Nota do Consumidor"])

# Salvar os dados em um arquivo Excel
df.to_excel("resultados.xlsx", index=False)

# Fechar o navegador
driver.quit()
"""