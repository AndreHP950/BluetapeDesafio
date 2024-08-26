## Web Scraping de Dados do Reclame Aqui: Moda

Este projeto é uma aplicação de scraping que coleta dados de empresas da seção de Moda do site Reclame Aqui. Utiliza Selenium e BeautifulSoup para extrair informações como reclamações respondidas, índice de solução e nota do consumidor.

### Requisitos

Para executar este script, você precisará do Python e das seguintes bibliotecas:

* **pandas:** Para manipulação e salvamento dos dados em formato Excel.
* **beautifulsoup4:** Para análise do HTML da página.
* **selenium:** Para automação da navegação na web e interação com o site.
* **lxml:** Para análise do HTML usando XPath.
* **webdriver-manager:** Para gerenciar o download do WebDriver do Chrome.

### Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/AndreHP950/BluetapeDesafio/
   cd bluetape
   ```
2. **Instale as dependências**
   * Python: Instale a versão mais recente do Python (https://www.python.org/downloads/).
   * Bibliotecas: Utilize o gerenciador de pacotes pip para instalar as seguintes bibliotecas:
   * Instalação do ChromeDriver: 
   * * **Baixar o ChromeDriver:** Faça o download do ChromeDriver compatível com a sua versão do Google Chrome em https://chromedriver.chromium.org/.
   * * **Configurar o caminho:** Coloque o arquivo do ChromeDriver em um diretório que esteja incluído na sua variável de ambiente PATH ou configure a variável de ambiente webdriver.chrome.driver para apontar para o caminho completo do arquivo.
   ```bash
     pip install pandas beautifulsoup4 selenium webdriver-manager lxml
   ```

   ## Como Executar

   ### Salve o código
   Salve o código Python em um arquivo (por exemplo, `reclameaqui_scraper.py`).

   ### Execute o script
   Abra um terminal, navegue até o diretório onde salvou o arquivo e execute o comando:

```bash
python reclameaqui_scraper.py
```

