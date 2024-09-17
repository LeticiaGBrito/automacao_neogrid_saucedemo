import time
from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
from features.support.elements.elements_web import Elements


class CheckoutPage(BasePage):     
    
    def __init__(self,driver):
        super().__init__(driver)    

    def clicando_em_checkout(self):       
        self.forca_click_element((By.ID, Elements.CHECKOUT_BUTTON))           
        self.capture_screenshot('steep001_tela_de_cadastro')
      
        
    def realizando_cadastro(self, nome, sobrenome, cep):       
        self.find_element((By.ID, Elements.FIRST_NAME_INPUT)).send_keys(nome)       
        self.find_element((By.ID, Elements.LAST_NAME_INPUT)).send_keys(sobrenome)           
        self.find_element((By.ID, Elements.POSTAL_CODE_INPUT)).send_keys(cep)             
        self.capture_screenshot('steep002_tela_de_cadastro_preenchida')         
        self.scroll_page(200)           
        self.capture_screenshot('steep003_tela_de_cadastro_preenchida')

            
        
    def clicando_em_continue(self):       
        self.forca_click_element((By.ID, Elements.CONTINUE_BUTTON))   
        time.sleep(2) 
        self.scroll_page(-300)
        self.capture_screenshot('steep004_overview_produtos')      
        time.sleep(2)
        self.scroll_page(500)
        self.capture_screenshot('steep005_overview_produtos')   
     
       
    def finalizando_compra(self):       
        self.forca_click_element((By.ID, Elements.FINISH_BUTTON))    
        time.sleep(2)
        
    
          
    def validando_compra_finalizada(self):
        self.scroll_page(-200)
        element = self.wait_for_element((By.XPATH, Elements.SELECT_TEXT_03))        
        if element:
            self.capture_screenshot('steep006_validacao_tela_compra_concluida', highlight_element=element)
            return 'Thank you for your order!' in element.text
        else:
            return False
 
    


