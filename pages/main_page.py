from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage
from .basket_page import BasketPage


class MainPage(BasketPage): #было basepage, возможна ошибка
    # Заглушка, тк не осталось никаких методов:
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
