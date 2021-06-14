from .base_page import Basepage
from selenium.webdriver.common.by import By

class MainPage(Basepage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()