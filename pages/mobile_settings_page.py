from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page


class MobileSettingsPage(Page):
    MOB_CTC_BTN = (By.CSS_SELECTOR, "div[class='get-free-period menu']")

    def click_mobile_connect_button(self):
        elements = self.find_elements(*self.MOB_CTC_BTN)
        elements[1].click()
