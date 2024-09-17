import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

class BasePage:
    
    def __init__(self, driver):
        self.browser = driver
        self.screenshot_dir = 'evidencias'
    
    def capture_screenshot(self, step_name=None, highlight_element=None):
        page_name = self.__class__.__name__.lower()
        
        # Criação do diretório para armazenar as capturas de tela
        directory = os.path.join(self.screenshot_dir, page_name)
        os.makedirs(directory, exist_ok=True)
        
        # Geração do nome do arquivo com timestamp
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"{step_name}_{timestamp}.png" if step_name else f"SCREENSHOT_{timestamp}.png"
        file_path = os.path.join(directory, filename)
        
        # Caso haja um elemento para destacar, rola a página até o elemento
        if highlight_element:
            self.browser.execute_script("arguments[0].scrollIntoView();", highlight_element)
        
        # Captura a screenshot diretamente via Selenium
        self.browser.save_screenshot(file_path)
        
        print(f"Screenshot salva em: {file_path}")


    def wait_for_element(self, locator, timeout=20):
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except TimeoutException as e:
            print(f"Elemento não encontrado dentro do tempo: {e}")
            return None

    def find_element(self, locator):
        return self.wait_for_element(locator)

    def send_keys_to_element(self, locator, text):
        element = self.wait_for_element(locator)
        if element:
            try:
                WebDriverWait(self.browser, 60).until(
                    EC.element_to_be_clickable(locator)
                )
                element.clear()
                element.send_keys(text)
            except Exception as e:
                print(f"Erro ao enviar texto para o elemento: {e}")
        else:
            print(f"Elemento não encontrado para ação send_keys: {locator}")

    def scroll_page(self, pixels):
        self.browser.execute_script(f"window.scrollBy(0, {pixels});")

    def forca_click_element(self, locator):
        clico_button = WebDriverWait(self.browser, 30).until(
            EC.element_to_be_clickable(locator)
        )
        actions = ActionChains(self.browser)
        actions.move_to_element(clico_button).click().perform()
