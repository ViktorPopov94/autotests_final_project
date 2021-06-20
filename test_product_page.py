#pytest -v --tb=line --language=en test_product_page.py
# pytest -s test_product_page.py
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import time

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.click_to_add_to_basket()
    page.solve_quiz_and_get_code()  # решение мат.задачи 4.3.2
    page.check_of_name_of_book()  # Проверка совпадения выбранного и добавленного товаров
    page.check_of_price_of_book()  # Проверка совпадения стоимости выбранного и добавленного товаров
