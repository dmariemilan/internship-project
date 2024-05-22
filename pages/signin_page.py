from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SigninPage(Page):
    SIGNIN_PAGE_HEADER = (By.XPATH, "//span[text()='Sign into your Target account']")
    TC_LINK = (By.XPATH, "//a[text()='Target terms and conditions']")


    def verify_login_page(self, expected_text):
        self.verify_text('Sign into your Target account', *self.SIGNIN_PAGE_HEADER)

    def click_tc_link(self):
        self.click(*self.TC_LINK)
