from selenium.webdriver.common.by import By
##posts > .item:nth-child(2) > .title
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")

class ProductPageLocators():
    # Кнопка добавления в корзину:
    ADD_TO_BASKET_LINK = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    # Название книги:
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    # Название добавленной в корзину книги:
    ADDED_BOOK_NAME = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in .alertinner strong")
    # Стоимость книги:
    BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main p")
    # Стоимость добавленной в корзину книги:
    ADDED_BOOK_PRICE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner strong")
    # Сообщение о добавлении товара:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in .alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
