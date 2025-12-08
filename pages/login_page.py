from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
    
    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert "login" in login_url, "The URL does not contain 'login'"
        
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not found"
        
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form not found"
        
    def register_new_user(self, email, passw):
        email_address = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS)
        email_address.send_keys(email)
        
        password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password.send_keys(passw)
        
        password_confirm = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM)
        password_confirm.send_keys(passw)
        
        button_registration = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION)
        button_registration.click()