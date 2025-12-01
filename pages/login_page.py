from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    URL = "https://thinking-tester-contact-list.herokuapp.com/"

    # Locators
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "submit")

    
    ADD_CONTACT_BUTTON = (By.ID, "add-contact")

    
    ERROR_MESSAGE = (By.ID, "error")

    def open_login(self):
        self.open(self.URL)

    def login(self, email, password):
        self.type(self.EMAIL_INPUT, email)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def is_logged_in(self):
       
        return self.is_visible(self.ADD_CONTACT_BUTTON)

    def has_error_message(self):
        return self.is_visible(self.ERROR_MESSAGE)
