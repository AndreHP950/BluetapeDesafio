import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains, ScrollOrigin
from lxml import html

# Configuração do WebDriver
service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service)


# Acessar a página inicial do Reclame Aqui e navegar até a seção de Moda
navegador.get("https://www.reclameaqui.com.br/")

# Define tela cheia
navegador.maximize_window()

# Rola a página 700u para carregar os elementos dinâmicos da página
scroll_origin = ScrollOrigin.from_viewport(10, 10)

ActionChains(navegador)\
    .scroll_from_origin(scroll_origin, 0, 700)\
    .perform()
        
# Encontra botao moda e clica
def clicaBotaoModa():
    """
    Encontra o botão "Moda" na página e clica nele.

    Esta função utiliza o Selenium WebDriver para localizar o botão "Moda" 
    com base no XPath fornecido. Se o botão não for encontrado dentro do tempo 
    de espera especificado, uma exceção será lançada.

    Args:
        Nenhum.

    Returns:
        None.
    """

    botao_moda = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/section[2]/div/astro-island/div/nav/div[2]/button[4]")))
    
    # Clicar no botão
    botao_moda.click()
    
clicaBotaoModa()

# Função para extrair dados de uma empresa da página atual
def extrair_dados_empresa():
    """Extrai os dados de uma empresa da página atual do navegador.

    Retorna:
        tuple: Uma tupla contendo o nome da empresa, número de reclamações respondidas,
               porcentagem de clientes que voltariam a fazer negócio, índice de solução
               e a nota do consumidor.
    """
    html_content = navegador.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    tree = html.fromstring(html_content)

    # Extrair o nome da empresa
    empresa_nome = soup.find("h1").text.strip()

    # Extrair outros dados da empresa
    elements = tree.xpath('//span[@class="go2549335548"]')
    if len(elements) >= 2:
        reclamacoes_respondidas = elements[1].text_content().strip()
        voltariam_a_fazer_negocio = elements[4].text_content().strip()
        indice_de_solucao = elements[5].text_content().strip()
    else:
        # Se os dados não forem encontrados, atribui valores padrão
        reclamacoes_respondidas = "Não encontrado"
        voltariam_a_fazer_negocio = "Não encontrado"
        indice_de_solucao = "Não encontrado"
    nota_do_consumidor = soup.find("span", class_="go1306724026").text.strip()

    return empresa_nome, reclamacoes_respondidas, voltariam_a_fazer_negocio, indice_de_solucao, nota_do_consumidor

# Lista de XPath's das melhores empresas
melhores_empresas_xpath = [
    "/html/body/section[2]/div/astro-island/div/div[3]/div/div[1]/a[1]",
    "/html/body/section[2]/div/astro-island/div/div[3]/div/div[1]/a[2]",
    "/html/body/section[2]/div/astro-island/div/div[3]/div/div[1]/a[3]"
]

# Lista de XPath's das piores empresas
piores_empresas_xpath = [
    "/html/body/section[2]/div/astro-island/div/div[3]/div/div[2]/a[1]",
    "/html/body/section[2]/div/astro-island/div/div[3]/div/div[2]/a[2]",
    "/html/body/section[2]/div/astro-island/div/div[3]/div/div[2]/a[3]"
]

# Função para formatar a classificação da empresa
def formatar_classificacao(i, lista):
    """Formata a classificação da empresa como 'nº Melhor' ou 'nº Pior'.

    Args:
        i: Índice da empresa na lista.
        lista: Lista das melhores e piores empresas.

    Returns:
        str: Classificação formatada.
    """
    if i < len(lista):
        return f"{i+1}º Melhor"
    else:
        return f"{i+1-len(lista)}º Pior"

# Extrair dados de cada empresa e adicionar ao DataFrame 
dados = []
for i, xpath in enumerate(melhores_empresas_xpath + piores_empresas_xpath):
    # Clicar no botao moda para garantir a exibição da lista correta
    clicaBotaoModa()
    
    # Navegar para a página da empresa
    empresa = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    empresa.click()
    
    # Extrair dados da empresa e formatar a classificação
    dados_empresa = extrair_dados_empresa()
    classificacao = formatar_classificacao(i, melhores_empresas_xpath)
    dados_empresa = (*dados_empresa, classificacao)
    dados.append(dados_empresa)

    # Voltar para a página anterior
    navegador.back()

# Criar o DataFrame e salvar em um arquivo Excel
df = pd.DataFrame(dados, columns=["Empresa", "Reclamações Respondidas", "Voltariam a Fazer Negócio", "Índice de Solução", "Nota do Consumidor", "Classificação"])
df.to_excel("resultados.xlsx", index=False)