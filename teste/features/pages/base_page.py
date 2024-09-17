import time
import os
import io
from PIL import Image, ImageDraw
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
        
        directory = os.path.join(self.screenshot_dir, page_name)
        os.makedirs(directory, exist_ok=True)
        
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"{step_name}_{timestamp}.png" if step_name else f"SCREENSHOT_{timestamp}.png"
        file_path = os.path.join(directory, filename)
        
        if highlight_element:
            self.browser.execute_script("arguments[0].scrollIntoView();", highlight_element)
        
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(io.BytesIO(screenshot))
        
        if highlight_element:
            location = highlight_element.location_once_scrolled_into_view
            size = highlight_element.size
            left = location['x']
            top = location['y']
            right = left + size['width']
            bottom = top + size['height']
            
            draw = ImageDraw.Draw(screenshot)
            draw.rectangle([left, top, right, bottom], outline="red", width=4)
        
        screenshot.save(file_path)
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
