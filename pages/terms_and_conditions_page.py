from selenium.webdriver.common.by import By

from pages.base_page import Page


class TermsAndConditionsPage(Page):

    def verify_tc_opened(self):
       self.verify_partial_url('terms-conditions/')