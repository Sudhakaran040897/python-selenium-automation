from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[class*='button-hero gray w-inline-block']")
    EMAIL_FIELD = (By.ID, "email-2")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[name='Password']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[class='login-button w-button']")


    def login_user(self, email, password):
        self.click(*self.LOGIN_BUTTON)
        self.input_text(email, *self.EMAIL_FIELD)
        self.input_text(password, *self.PASSWORD_FIELD,)
        self.click(*self.SUBMIT_BUTTON)

