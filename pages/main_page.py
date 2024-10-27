from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page


class MainPage(Page):
    CTC_BTN = (By.CSS_SELECTOR, "div[class='get-free-period menu']")
    MOB_MENU_BTN = (By.CSS_SELECTOR, "div[class='mobile-top-menu']")
    SETTINGS_OPTION = (By.XPATH, "//div[contains(@class, 'menu-button-text') and text()='Settings']")
    MAIN_MENU_OPTION = (By.XPATH, "//div[text()='Main menu']")
    SECONDARY_OPTION = (By.XPATH, "//div[contains(@class, 'menu-button-text') and text()='Secondary']")

    def open_main(self):
        self.driver.get('https://soft.reelly.io/sign-in')

    def click_mobile_menu_button(self):
        self.wait_until_clickable_click(*self.MOB_MENU_BTN)

    def click_connect_button(self):
        self.wait_until_clickable_click(*self.CTC_BTN)

    def click_settings_option(self):
        self.wait_until_clickable_click(*self.SETTINGS_OPTION)

    def click_main_menu_option(self):
        self.wait_until_clickable_click(*self.MAIN_MENU_OPTION)

    def click_secondary_option(self):
        self.wait_until_clickable_click(*self.SECONDARY_OPTION)








