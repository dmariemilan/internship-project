from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")
    CART_VIEW_AND_SUMMARY = (By.CSS_SELECTOR, "a[href='/cart']")
    CART_SUMMARY = (By.CSS_SELECTOR, "[class*='CartSummarySpan']")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

    def verify_cart_empty_message(self):
        # actual_text = self.find_element(*self.CART_EMPTY_MSG).text
        # expected_text = 'Your cart is empty'
        # assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)

    def click_on_view_cart(self):
        self.wait_until_clickable_click(*self.CART_VIEW_AND_SUMMARY)

    def verify_cart_items(self, amount):
        actual_amount = self.find_element(*self.CART_SUMMARY).text
        assert amount in actual_amount, f'Expected {amount} items but got {actual_amount}'

    def verify_product_name(self, product_name):
        actual_name = self.find_element(*self.CART_ITEM_TITLE).text
        assert product_name in actual_name.lower(), f'Expected {product_name} but got {actual_name}'






