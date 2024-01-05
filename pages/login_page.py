from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.driver.current_url, (
            'Current url do not contain "login" word, '
            'perhaps it is not login url'
        )

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), (
            'Login form is not presented'
        )

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), (
            'Registration form is not presented'
        )

    def register_new_user(self, email: str, password: str):
        self.driver.find_element(
            *LoginPageLocators.REGISTER_FORM_EMAIL
        ).send_keys(email)
        self.driver.find_element(
            *LoginPageLocators.REGISTER_FORM_PASS1
        ).send_keys(password)
        self.driver.find_element(
            *LoginPageLocators.REGISTER_FORM_PASS2
        ).send_keys(password)
        self.driver.find_element(
            *LoginPageLocators.REGISTER_SUBMIT
        ).click()
