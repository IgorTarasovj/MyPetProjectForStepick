from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, " expected 'login' in base current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.login_form), "login_form not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.register_form), "register_form not found"


    def register_new_user(self, email, password):
        registration_email = self.browser.find_element(*LoginPageLocators.registration_email)
        registration_email.send_keys(email)

        registration_password1 = self.browser.find_element(*LoginPageLocators.registration_password1)
        registration_password1.send_keys(password)

        registration_password2 = self.browser.find_element(*LoginPageLocators.registration_password2)
        registration_password2.send_keys(password)

        registration_submit = self.browser.find_element(*LoginPageLocators.registration_submit)
        registration_submit.click()