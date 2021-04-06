from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login is not in URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USER_NAME), "Form for login username not found"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Form for login password not found"
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT), "Button for login click not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Form for registration email not found"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1), "Form for registration password first not found"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2), "Form for registration password second not found"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT), "Button for registration click not found"