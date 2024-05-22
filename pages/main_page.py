from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page



class MainPage(Page):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "div[class*='ThreeUpButtonWrapper'] button[id*='addToCartButton']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")

    def open_main(self):
        self.driver.get('https://www.target.com/')

    def click_add_to_cart(self):
        self.wait_until_clickable_click(*self.ADD_TO_CART_BTN)

    def side_nav_click_add_to_cart(self):
        self.wait_until_clickable_click(*self.SIDE_NAV_ADD_TO_CART_BTN)

    def store_product_name(self):
        self.wait_until_visible(*self.SIDE_NAV_PRODUCT_NAME)

