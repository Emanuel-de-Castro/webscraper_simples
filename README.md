# Web Scraper Vagas Python 🚀

Scraper que extrai vagas de Python do site https://realpython.github.io/fake-jobs/


# Como funciona o site fake-jobs

- **Página principal**:  
  - Contém uma seção `<div id="ResultsContainer">` com vários cards de vagas.  
  - Cada card possui:
    - Título da vaga (`<h2 class="title">`).  
    - Nome da empresa (`<h3 class="company">`).  
    - Localização (`<p class="location">`).  
    - Dois links no rodapé: "Learn" e "Apply".  

- **Páginas de detalhe**:  
  - Cada vaga tem um link "Apply" que aponta para `/jobs/...html`.  
  - Nessa página, aparece o texto completo da vaga para fins de exercício.  

O scraper extrai apenas os dados da página principal (título, empresa, local e link "Apply") e exporta para CSV.



# Funcionalidades
  - Filtra apenas vagas com "Python" no título
  - Extrai: Título, Empresa, Local, Data (MM/YYYY), Descrição (máx 200 caracteres)
  - Salva automaticamente em `vagas_python.csv`
  - Headers com `User-Agent` (Para evitar bloqueio)

# Estrutura do Projeto

    📁 webscraper_simples/

    ├── 📄 main.py
    
    ├── 📄 README.md
    
    ├── 📄 requirements.txt
    
    ├── 📄 .gitignore
    
    └── 📄 vagas_python.csvpython.csv



## Como usar 

1. Clone o repositório
  git clone https://github.com/Emanuel-de-Castro/webscraper_simples.git

    cd webscraper_simples

3. Instale dependências
   
      pip install requests
    
      pip install beautifulsoup4
    
    
