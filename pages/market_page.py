from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page


class MarketPage(Page):
    DEVELOPER_BTN = (By.XPATH, "//div[contains(@class, 'tag-text-proparties') and text()='Developers']")
    LICENSE_TAG = (By.XPATH, "//div[contains(@class, 'license-txt') and text()='License']")
    LICENSE_BLOCK = (By.CSS_SELECTOR, "div[class='license-block']")

    def click_developers_filter(self):
        self.wait_until_clickable_click(*self.DEVELOPER_BTN)

    def verify_all_cards_have_license_tag(self):
        all_cards = self.wait.until(EC.visibility_of_all_elements_located(self.LICENSE_BLOCK))
        for card in all_cards:
            tag = card.find_element(*self.LICENSE_TAG)
            assert tag.text == 'License', f"Tag does not contain 'License'"


