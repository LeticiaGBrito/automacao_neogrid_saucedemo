from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
from features.support.elements.elements_web import Elements
from features.support.ambient.base_url import BASE_URL



class LoginPage(BasePage):  # Herda da BasePage

    def acessando_tela_de_login(self):               
        self.browser.get(BASE_URL)    
        self.capture_screenshot('steep001_tela_de_autenticacao')
        self.scroll_page(200)
        self.capture_screenshot('steep002_tela_de_autenticacao')   
        
 
    def informando_credenciais_login(self, usuario, senha ):
        self.scroll_page(-200)
        self.send_keys_to_element((By.ID,Elements.USERNAME), usuario)
        self.send_keys_to_element((By.ID, Elements.PASSWORD), senha)    
        self.capture_screenshot('steep003_crendenciais_informada')  
 
    
    def clicando_no_botao_login(self):
        self.forca_click_element((By.ID, Elements.LOGIN_BUTTON)) 
       
    def validar_tela_inicial(self):
        element = self.wait_for_element((By.XPATH, Elements.SELECT_TEXT_01)) 
        if element:
            self.capture_screenshot('steep004_validacao_tela_inicial', highlight_element=element)
            self.scroll_page(500)
            self.capture_screenshot('steep005_validacao_tela_inicial')
            return 'Products' in element.text
        else:
            return False


      