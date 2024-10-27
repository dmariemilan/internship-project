from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page


class SecondaryPage(Page):
    NEXT_PAGE_BUTTON = (By.CSS_SELECTOR, "[wized=nextPageMLS]")
    PREV_PAGE_BUTTON = (By.CSS_SELECTOR, "[wized=previousPageMLS]")

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



