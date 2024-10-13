from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page


class SettingsPage(Page):
    SETTINGS_OPTION = (By.CSS_SELECTOR, "a[class='page-setting-block w-inline-block']")
    NUMBER_OF_OPTIONS = (By.CSS_SELECTOR, "a[class='page-setting-block w-inline-block']")
    CONNECT_TO_COMPANY = (By.CSS_SELECTOR, "div[class='settings-block-menu'] div[class='get-free-period menu']")
    EDIT_PROFILE = (By.XPATH, "//div[contains(@class, 'setting-text') and text()='Edit profile']")
    ADD_A_PROJECT = (By.XPATH, "//div[contains(@class, 'setting-text') and text()='Add a project']")
    COMMUNITY_OPTION = (By.XPATH, "//div[contains(@class, 'setting-text') and text()='Community']")
    CONTACT_US = (By.XPATH, "//div[contains(@class, 'setting-text') and text()='Contact us']")
    USER_GUIDE = (By.XPATH, "//div[contains(@class, 'setting-text') and text()='User guide']")
    CHANGE_PASSWORD = (By.XPATH, "//div[contains(@class, 'setting-text') and text()='Change password']")
    SUBSCRIPTION_PAYMENTS = (By.XPATH, "//div[contains(@class, 'setting-text') and text()='Subscription & payments']")
    SUPPORT_OPTION = (By.XPATH, "//div[contains(@class, 'setting-text') and text()='Support']")
    NEWS_OPTION = (By.XPATH, "//div[contains(@class, 'setting-text') and text()='News']")

    def click_settings(self):
        self.wait_until_clickable_click(*self.SETTINGS_OPTION)

    def verify_settings_page_opened(self):
        self.verify_partial_url('settings')

    def verify_settings_options(self, expected_amount):
        options = self.find_elements(*self.NUMBER_OF_OPTIONS)
        assert len(options) == expected_amount, f'Expected {expected_amount} cells but got {len(options)}'

    def verify_connect_button(self):
        self.find_element(*self.CONNECT_TO_COMPANY)

    def click_edit_profile(self):
        self.wait_until_clickable_click(*self.EDIT_PROFILE)
        sleep(5)

    def click_add_a_project(self):
        self.wait_until_clickable_click(*self.ADD_A_PROJECT)
        sleep(4)

    def click_community(self):
        self.wait_until_clickable_click(*self.COMMUNITY_OPTION)
        sleep(4)

    def click_contact_us(self):
        self.wait_until_clickable_click(*self.CONTACT_US)

    def click_user_guide(self):
        self.wait_until_clickable_click(*self.USER_GUIDE)

    def click_change_password(self):
        self.wait_until_clickable_click(*self.CHANGE_PASSWORD)

    def click_subscription_and_payments(self):
        self.wait_until_clickable_click(*self.SUBSCRIPTION_PAYMENTS)

    def click_support(self):
        self.wait_until_clickable_click(*self.SUPPORT_OPTION)

    def click_news(self):
        self.wait_until_clickable_click(*self.NEWS_OPTION)























