from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page



class MainPage(Page):
    CTC_BTN = (By.CSS_SELECTOR, "div[class='get-free-period menu']")

    def open_main(self):
        self.driver.get('https://soft.reelly.io/sign-in')

    def click_connect_button(self):
        self.wait_until_clickable_click(*self.CTC_BTN)