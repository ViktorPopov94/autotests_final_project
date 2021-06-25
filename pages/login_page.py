from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "login в url отсутствует"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "форма логина не найдена"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "форма регистрации не найдена"

    def register_new_user(self, email, password):
        # Заполнение поля Email:
        email_field_registration = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION)
        email_field_registration.send_keys (email)
        # Заполнение паролей:
        password1 = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION)
        password1.send_keys (password)

        password2 = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION_REPEAT)
        password2.send_keys (password)

        # нажимаем "зарегистрироваться"
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()

