from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page


class ContactUsPage(Page):
    SOCIAL_MEDIA_ICONS = (By.CSS_SELECTOR, "[class='social-button']")
    CONNECT_COMPANY_BTN = (By.XPATH, "//div[text()='Connect the company']")

    def verify_contact_us_page_opened(self):
        self.verify_partial_url('contact-us')

    def verify_social_media_icons(self):
        social_icons = self.driver.find_elements(*self.SOCIAL_MEDIA_ICONS)
        assert len(social_icons) >= 4, f'Should have at least 4 but got {len(social_icons)}'

    def verify_connect_company_btn(self):
        self.wait_until_clickable_click(*self.CONNECT_COMPANY_BTN)
