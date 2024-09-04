from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page


class ChangePasswordPage(Page):
    NEW_PASSWORD = (By.ID, 'Enter-new-password')
    REPEAT_PASSWORD = (By.ID, 'Repeat-password')
    CHANGE_PASSWORD_BTN = (By.CSS_SELECTOR, "a[class='submit-button-2 w-button']")

    def verify_change_password_page_opened(self):
        self.verify_partial_url('set-new-password')

    def password_information(self):
        self.input_text('Mil567*anD', *self.NEW_PASSWORD)
        self.input_text('Mil567*anD', *self.REPEAT_PASSWORD)

    def change_password_btn(self):
        self.find_element(*self.CHANGE_PASSWORD_BTN)

