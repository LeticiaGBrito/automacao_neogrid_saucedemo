import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from features.pages.base_page import BasePage
from features.support.elements.elements_web import Elements


class FiltroProdutosPage(BasePage):     
    
    def __init__(self,driver):
        super().__init__(driver)      


    def selecionando_tipo_do_filtro(self, opcao):  
        self.capture_screenshot('steep001_tela_de_filtro')   
        time.sleep(2)   
        dropdown = Select(self.browser.find_element(By.CSS_SELECTOR,Elements.SELECT_FILTRO))
        dropdown.select_by_visible_text(opcao)
     

            
    def verificar_ordenacao_precos_na_lista(self): 
        self.capture_screenshot('steep002_tela_de_filtro') 
        self.scroll_page(300)       
        self.capture_screenshot('steep003_tela_de_filtro') 
  