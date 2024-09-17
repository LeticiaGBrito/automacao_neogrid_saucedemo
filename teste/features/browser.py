from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

class Browser: 
    def __init__(self):
        edge_options = Options()
        edge_options.add_argument("profile-directory=Default")
        # edge_options.add_argument('--headless')
        edge_options.add_argument('--enable-logging')    
        edge_options.add_argument('--start-maximized')          
        edge_options.add_argument('--disable-gpu')
        edge_options.add_argument('--ignore-certificate-errors')
        edge_options.add_argument('--ignore-ssl-errors')
        edge_options.add_argument('--disable-web-security')
        edge_options.add_argument('--disable-site-isolation-trials')           
        edge_options.add_argument('--no-sandbox')
        edge_options.add_argument('--incognito')        
        service = Service(executable_path='C:\\edgedriver\\msedgedriver.exe')
        self.driver = webdriver.Edge(service=service, options=edge_options)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def quit(self):
        self.driver.quit()
        
    def limpa_cache_browser(self):
        self.driver.delete_all_cookies()
        
    def save_screenshot(self, filepath):
        self.driver.save_screenshot(filepath)
        print(f"Screenshot salva em:{filepath}")
