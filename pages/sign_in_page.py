from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page


class SignInPage(Page):
    USER_EMAIL = (By.ID, "email-2")
    USER_PASSWORD = (By.ID, "field")
    CONTINUE_BTN = (By.CSS_SELECTOR, "a[class='login-button w-button']")

    def input_email_and_password(self, email, password):
        self.input_text(email, *self.USER_EMAIL)
        self.input_text(password, *self.USER_PASSWORD)
        self.click(*self.CONTINUE_BTN)


