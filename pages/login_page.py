from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = str(self.browser.current_url)
        index = url.find("login")
        print(index)
        assert index != -1, "It is not login page!"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "There is no login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "There is no registration form"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        password_repeat = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD)
        password_repeat.send_keys(password)
        button_enter = self.browser.find_element(*LoginPageLocators.ENTER_BUTTON)
        button_enter.click()
