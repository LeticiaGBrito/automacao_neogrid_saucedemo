from selenium import webdriver
from features.browser import Browser
from features.pages.login_page import LoginPage
import os
import shutil

def before_all(context):
    context.browser = Browser()
    context.driver = context.browser.driver
    #context.screenshot_dir = 'C:\\GIT_AUTOMACAO\\PYTHON\\projeto_ neogrid\\saucedemo_automation\\evidencias'
    context.screenshot_dir = 'C:\\GIT_AUTOMACAO\\automacao_neogrid_saucedemo\\automacao_neogrid_saucedemo\\teste\\evidencias'
    
    # # # Limpa o diretório de screenshots se existir
    # if os.path.exists(context.screenshot_dir):
    #     shutil.rmtree(context.screenshot_dir)
    # os.makedirs(context.screenshot_dir, exist_ok=True)
  
 
    login_feature_dir = os.path.join(context.screenshot_dir, 'loginpage')

    # Remove todos os arquivos no diretório de login.feature, se existir
    if os.path.exists(login_feature_dir):
        for filename in os.listdir(login_feature_dir):
            file_path = os.path.join(login_feature_dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)

    # # Inicializa a página de login e realiza o login
    context.login_page = LoginPage(context.driver)
    context.login_page.acessando_tela_de_login()
    context.login_page.informando_credenciais_login("standard_user", "secret_sauce")
    context.login_page.clicando_no_botao_login()

def after_all(context):
     context.browser.quit()
