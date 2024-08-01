from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page


class ProfilePage(Page):
    TEST_NAME = (By.ID, "Fullname")
    TEST_PHONE = (By.ID, "number")
    TEST_COMPANY = (By.ID, "Company-name")
    TEST_EMAIL = (By.ID, "Email-2")
    SAVE_CHANGES_BTN = (By.XPATH, "//*[text()='Save changes']")
    CLOSE_BTN = (By.XPATH, "//*[text()='Close']")

    def input_name(self, name):
        input_fname = self.find_element(*self.TEST_NAME)
        input_fname.clear()
        self.input_text(name, *self.TEST_NAME)
        sleep(3)

    def input_number(self, number):
        input_number = self.find_element(*self.TEST_PHONE)
        input_number.clear()
        self.input_text(number, *self.TEST_PHONE)
        sleep(2)

    def input_company(self, company):
        input_company = self.find_element(*self.TEST_COMPANY)
        input_company.clear()
        self.input_text(company, *self.TEST_COMPANY)

    def input_email(self, email):
        input_email = self.find_element(*self.TEST_EMAIL)
        input_email.clear()
        self.input_text(email, *self.TEST_EMAIL)

    def verify_input_name(self, name):
        actual_name = self.find_element(*self.TEST_NAME)

    def verify_input_phone(self, phone):
        actual_phone = self.find_element(*self.TEST_PHONE)

    def verify_input_company(self, company):
        actual_company = self.find_element(*self.TEST_COMPANY)

    def verify_input_email(self, email):
        actual_email = self.find_element(*self.TEST_EMAIL)

    def click_save_changes_btn(self):
        self.click(*self.SAVE_CHANGES_BTN)
        sleep(3)

    def click_close_btn(self):
        self.click(*self.CLOSE_BTN)






