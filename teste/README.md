# Desafio Técnico de Automação Site Saucedemo

## Descrição

Este projeto realiza a automação de testes para o site de demonstração do Sauce Labs utilizando Python, Behave, Selenium e BDD.

### Pré-requisitos

- Python 3.x
- WebDriver
- Selenium
- Behave 


- Instalação das dependências:
    criando e ativando o ambiente virtual  
            1. python -m venv .env (cria o diretorio .env)
            2. .env\Scripts\activate (ativa o ambiente virtual)
            3. pip install -r requirements.txt (instala as dependencias no projeto)
            4. pip freeze > requirements.txt (atualiza a lista de dependencias)
            5. pip list (mostra a lista das dependencias instaladas)





    ## Descrição da estrutura
•  features/pages: Contém classes que representam cada página da aplicação
•  features/steps: Contém os arquivos que mapeiam os steps dos cenários de BDD para métodos das páginas.
•  features/specs: Contém os arquivos .feature com os cenários de teste em Gherkin.
•  features/elements.py: Armazena os seletores de elementos, como XPaths e IDs.
•  features/environment.py: Configura o ambiente do teste, como inicialização do navegador.
•  features/browser.py : configuracao de codigo para abrir o navegador - edge
•  features/pages/base_page.py: contem classe com os metodos reutilizaveis
•  evidencias: Diretório onde serão armazenados os screenshots e relatórios.
•  requirements.txt: Arquivo para definir as dependências do projeto.

 ## Comando para rodar fluxo completo
   behave
   ou
   behave features/specs
   ou
   behave features/specs/login.feature; behave features/specs/checkout.feature; behave features/specs/adicionar_ao_carrinho.feature; behave features/specs/filtro_produtos.feature


 ## comando para rodar fluxo por unidade
   behave features/specs/login.feature
   behave features/specs/checkout.feature
   behave features/specs/filtro_produtos.feature
   behave features/specs/adicionar_ao_carrinho.feature

## para o login ele faz o acesso automatico, quando rodar o teste por unidade , nao tem a necessidade de realizar o teste do login. 
   
  




