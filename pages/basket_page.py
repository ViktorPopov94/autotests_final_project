from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasketPageLocators
import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasketPage(BasePage):
    def product_in_basket_not_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def product_in_basket_should_not_be(self):
        assert self.product_in_basket_not_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "Товар в корзине есть, хотя быть его не должно"

    def basket_is_empty_message_exists(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), "Сообщение о пустой корзине не найдено"