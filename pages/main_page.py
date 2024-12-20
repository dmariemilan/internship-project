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
    OFF_PLAN_SIDE_OPTION = (By.XPATH, "//div[contains(@class, 'menu-button-text') and text()='Off-plan']")
    OFF_PLAN_FILTER_BUTTON = (By.CSS_SELECTOR, "a[class='filter-button w-inline-block']")
    OP_APPLY_FILTER_BTN = (By.CSS_SELECTOR, "a[wized='applyFilterButton']")
    PROPERTY_CARDS = (By.CSS_SELECTOR, "a[wized='cardOfProperty']")
    OFF_PLAN_PRICE = (By.CSS_SELECTOR, "div[class='price-value']")

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
        sleep(5)

    def click_on_off_plan_side_option(self):
        self.wait_until_clickable_click(*self.OFF_PLAN_SIDE_OPTION)
        sleep(10)

    def click_on_off_plan_filter(self):
        self.wait_until_clickable_click(*self.OFF_PLAN_FILTER_BUTTON)

    def click_on_off_plan_apply_filter(self):
        self.wait_until_clickable_click(*self.OP_APPLY_FILTER_BTN)

    def verify_price_in_range(self):
        all_property = self.wait.until(EC.visibility_of_all_elements_located(self.PROPERTY_CARDS))
        for property in all_property:
            property_price = property.find_element(*self.OFF_PLAN_PRICE)
            amount = property_price.text.replace('AED', '').replace(',', '')
            assert int(amount) in range(1200000, 2000000), f"Price not in Range"




















