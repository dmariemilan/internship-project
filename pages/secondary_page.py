from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page


class SecondaryPage(Page):
    NEXT_PAGE_BUTTON = (By.CSS_SELECTOR, "[wized=nextPageMLS]")
    PREV_PAGE_BUTTON = (By.CSS_SELECTOR, "[wized=previousPageMLS]")
    FILTER_BUTTON = (By.XPATH, "//div[contains(@class, 'filter-text') and text()='Filters']")
    WANT_TO_SELL = (By.XPATH, "//div[contains(@class, 'tag-text-filters') and text()='Want to sell']")
    WANT_TO_BUY = (By.XPATH, "//div[contains(@class, 'tag-text-filters') and text()='Want to buy']")
    APPLY_FILTER_BUTTON = (By.CSS_SELECTOR, "[wized=applyFilterButtonMLS]")
    LISTING_CARDS = (By.CSS_SELECTOR, "[class=listing-card]")
    FOR_SALE_TAG = (By.XPATH, "//div[contains(@wized, 'saleTagMLS') and text()='For sale']")
    WANT_TO_BUY_TAG = (By.XPATH, "//div[contains(@wized, 'saleTagMLS') and text()='Want to buy']")
    FROM_TO_INPUT_FIELD = (By.XPATH, "//div[@class='project-block']")
    UNIT_PRICE_FROM = (By.CSS_SELECTOR, "input[wized='unitPriceFromFilter']")
    UNIT_PRICE_TO = (By.CSS_SELECTOR, "input[wized='unitPriceToFilter']")
    LISTING_PRICE = (By.CSS_SELECTOR, "div[wized='unitPriceMLS']")

    def go_to_final_page(self):

        while True:
            try:
                next_page_button = self.wait_until_clickable_click(*self.NEXT_PAGE_BUTTON)
                actions = ActionChains(self.driver)
                actions.move_to_element(next_page_button)
                actions.perform()
                next_page_button.click()
                self.wait.until(EC.staleness_of(next_page_button))

            except:
                 print('Reached the end of the pages')

                 break

        while True:
            try:
                prev_page_button = self.wait_until_clickable_click(*self.PREV_PAGE_BUTTON)
                actions = ActionChains(self.driver)
                actions.move_to_element(prev_page_button)
                actions.perform()
                prev_page_button.click()
                self.wait.until(EC.staleness_of(prev_page_button))

            except:
                 print('Reached the beginning of the pages')

                 break

    def click_on_filters(self):
        self.wait_until_clickable_click(*self.FILTER_BUTTON)

    def click_want_to_sell(self):
        self.wait_until_clickable_click(*self.WANT_TO_SELL)

    def click_want_to_buy(self):
        self.wait_until_clickable_click(*self.WANT_TO_BUY)

    def click_apply_filter(self):
        self.wait_until_clickable_click(*self.APPLY_FILTER_BUTTON)

    def verify_all_cards_have_for_sale_tag(self):
        all_cards = self.wait.until(EC.visibility_of_all_elements_located(self.LISTING_CARDS))
        for card in all_cards:
            tag = card.find_element(*self.FOR_SALE_TAG).text
            assert 'for sale' in tag.lower(), f"Tag does not contain 'for sale' in card: {card}"

    def verify_all_cards_have_want_to_buy_tag(self):
        all_cards = self.wait.until(EC.visibility_of_all_elements_located(self.LISTING_CARDS))
        for card in all_cards:
            tag = card.find_element(*self.WANT_TO_BUY_TAG).text
            assert 'want to buy' in tag.lower(), f"Tag does not contain 'want to buy' in card: {card}"

    def filter_products_by_price_range(self):
        self.wait_until_visible(*self.FROM_TO_INPUT_FIELD)
        self.input_text('1200000', *self.UNIT_PRICE_FROM)
        self.input_text('2000000', *self.UNIT_PRICE_TO)

    def verify_price_range_in_all_cards(self):
        all_cards = self.wait.until(EC.visibility_of_all_elements_located(self.LISTING_CARDS))
        for card in all_cards:
            listing_price = card.find_element(*self.LISTING_PRICE)
            amount = listing_price.text.replace('AED', '').replace(',', '')
            assert int(amount) in range(1200000, 2000000), f"Price not in Range"














