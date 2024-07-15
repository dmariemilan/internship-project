from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page


class SettingsPage(Page):
    SETTINGS_OPTION = (By.CSS_SELECTOR, "a[class='page-setting-block w-inline-block']")
    NUMBER_OF_OPTIONS = (By.CSS_SELECTOR, "a[class='page-setting-block w-inline-block']")
    CONNECT_TO_COMPANY = (By.CSS_SELECTOR, "div[class='settings-block-menu'] div[class='get-free-period menu']")

    def click_settings(self):
        self.wait_until_clickable_click(*self.SETTINGS_OPTION)

    def verify_settings_page_opened(self):
        self.verify_partial_url('settings')

    def verify_settings_options(self, expected_amount):
        options = self.find_elements(*self.NUMBER_OF_OPTIONS)
        assert len(options) == expected_amount, f'Expected {expected_amount} cells but got {len(options)}'

    def verify_connect_button(self):
        self.find_element(*self.CONNECT_TO_COMPANY)









