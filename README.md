# Web Scraper Vagas Python 🚀

Scraper que extrai vagas de Python do site https://realpython.github.io/fake-jobs/

#Funcionalidades
  - Filtra apenas vagas com "Python" no título
  - Extrai: Título, Empresa, Local, Data (MM/YYYY), Descrição (máx 200 caracteres)
  - Salva automaticamente em `vagas_python.csv`
  - Headers com `User-Agent` (Para evitar bloqueio)

    📁 webscraper_simples/

    ├── 📄 main.py
    ├── 📄 README.md
    ├── 📄 requirements.txt  ✅
    ├── 📄 .gitignore
    └── 📄 vagas_python.csvpython.csv



## Como usar 

1. Clone o repositório
  git clone https://github.com/Emanuel-de-Castro/webscraper_simples.git
  cd webscraper_simples

2. Ambiente virtual
      # Windows
      python -m venv .venv
      .venv\Scripts\activate
    
    # Linux/Mac
      python3 -m venv .venv
      source .venv/bin/activate

3. Instale dependências
  pip install requests
  pip install beautifulsoup4


