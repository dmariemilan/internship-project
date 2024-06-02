from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page


class BookPresentationPage(Page):
    def verify_bp_page_opened(self):
        self.verify_partial_url('book-presentation')



