from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class AccountSideNav(Page):
    SIGN_IN = (By.XPATH, "//a[@data-test='accountNav-signIn']")

    def click_sign_in(self):
        self.wait_until_clickable_click(*self.SIGN_IN)
        sleep(6)


