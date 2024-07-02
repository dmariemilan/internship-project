from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page


class SignUpPage(Page):
    NAME = (By.ID, "Full-Name")
    PHONE = (By.ID, "phone2")
    EMAIL = (By.ID, "Email-3")
    PASSWORD = (By.ID, "field")
    COMPANY = (By.ID, "Company-website")

    def open_sign_up(self):
        self.driver.get('https://soft.reelly.io/sign-up')

    def input_name_and_phone(self, name, phone):
        self.input_text(name, *self.NAME)
        self.input_text(phone, *self.PHONE)

    def input_email_and_password(self, email, password):
        self.input_text(email, *self.EMAIL)
        self.input_text(password, *self.PASSWORD)

    def input_company(self, company):
        self.input_text(company, *self.COMPANY)

    def verify_input_name(self, name):
        actual_name = self.find_element(*self.NAME)

    def verify_input_phone(self, phone):
        actual_phone = self.find_element(*self.PHONE)

    def verify_input_email(self, email):
        actual_email = self.find_element(*self.EMAIL)

    def verify_input_password(self, password):
        actual_password = self.find_element(*self.PASSWORD)

    def verify_input_company(self, company):
        actual_company = self.find_element(*self.COMPANY)





