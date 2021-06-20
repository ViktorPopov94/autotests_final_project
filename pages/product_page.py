from .base_page import BasePage
from .locators import ProductPageLocators
import pytest
#col-sm-6 product_main
#alertinner
class ProductPage(BasePage):

    def click_to_add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_LINK)
        link.click()

    def check_of_name_of_book(self):  # Проверка совпадения выбранного и добавленного товаров
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        added_book_name = self.browser.find_element(*ProductPageLocators.ADDED_BOOK_NAME).text

        assert book_name == added_book_name, 'Названия выбранного и добавленного товаров не совпадают'
        if book_name == added_book_name:
            print('Товар добавлен в корзину. Названия выбранного и добавленного товаров совпадают')

    def check_of_price_of_book(self):  # Проверка совпадения стоимости выбранного и добавленного товаров
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        added_book_price = self.browser.find_element(*ProductPageLocators.ADDED_BOOK_PRICE).text

        assert book_price == added_book_price, "Стоимость выбранного товара не соответствует стоимости добавленного товара"
        if book_price == added_book_price:
            print('Стоимость выбранного товара соответствует стоимости добавленного товара')
