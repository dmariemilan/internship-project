from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page


class MainMenuPage(Page):
    LANGUAGE_SELECTOR = (By.ID, "w-dropdown-toggle-0")
    RU_BTN = (By.XPATH, "//a[text()='RU']")
    RUSSIAN_HEADER = (By.XPATH, "//h1[@class='h1-menu' and text()='Главное меню']")

    def change_language(self):
        self.wait_until_visible(*self.LANGUAGE_SELECTOR)
        lang = self.find_element(*self.LANGUAGE_SELECTOR)
        actions = ActionChains(self.driver)
        actions.move_to_element(lang)
        actions.move_by_offset(1, 25)
        actions.perform()
        self.click(*self.RU_BTN)

    def verify_language(self):
        actual_text = self.find_element(*self.RUSSIAN_HEADER).text
        expected_text = 'Главное меню'
        assert expected_text == actual_text, f'Error: expected {expected_text}, is not {actual_text}'
