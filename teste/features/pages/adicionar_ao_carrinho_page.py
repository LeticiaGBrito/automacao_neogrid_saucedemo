from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
from features.support.elements.elements_web import Elements


class CarrinhoComprasPage(BasePage):     
    
    def __init__(self,driver):
        super().__init__(driver)    

    def adicionando_produto(self):       
        self.forca_click_element((By.ID, Elements.ADD_PRODUTO_01))           
        self.capture_screenshot('steep001_produto_adicionado')
        self.scroll_page(500)
        self.forca_click_element((By.ID, Elements.ADD_PRODUTO_02)) 
        self.capture_screenshot('steep002_produto_adicionado')      
        
    def acessando_carrinho(self):        
        self.scroll_page(-500)
        self.forca_click_element((By.XPATH, Elements.CARRINHO))
        self.capture_screenshot('steep003_total_produto_adicionado')
        
    def validando_produto_adicionado(self):
        element = self.wait_for_element((By.XPATH, Elements.SELECT_TEXT_02)) 
        if element:
                self.capture_screenshot('steep004_validacao_produto_adicionado', highlight_element=element)
                self.scroll_page(500)
                self.capture_screenshot('steep005_validacao_produto_adicionado')
                return 'Your Cart' in element.text
        else:
                return False

    def clicando_em_Continue_Shopping(self):
        self.forca_click_element((By.ID, Elements.BUTTON_CONTINUE)) 
        self.scroll_page(-200)
        

    def removendo_produto_da_lista(self):
        self.forca_click_element((By.XPATH, Elements.REMOVE_PRODUTO_01)) 
        self.capture_screenshot('steep006_mochila_removido')
        self.scroll_page(500)
        self.forca_click_element((By.XPATH, Elements.REMOVE_PRODUTO_02)) 
        self.capture_screenshot('steep007_bory_removido')
        
    def verficando_exclusao_produtos_no_carrinho(self):
        self.scroll_page(-500)
        self.forca_click_element((By.XPATH, Elements.CARRINHO)) 
        self.capture_screenshot('steep008_carrinho_vazio')
   


    
