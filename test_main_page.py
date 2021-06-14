#pytest -v --tb=line --language=en test_main_page.py
"""
В этой команде мы использовали опцию PyTest --tb=line, которая указывает, что нужно
выводить только одну строку из лога каждого упавшего теста
"""

from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

def test_login_page_has_login_in_url(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()  # проверка, что подстрока "login" есть в текущем url браузера

def test_login_page_has_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()  # проверка наличия формы логина

def test_login_page_has_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()  # проверка наличия формы регистрации

