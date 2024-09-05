from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page


class SubAndPaymentsPage(Page):
    SUB_PAY_TITLE = (By.CSS_SELECTOR, ".lotion-your-h3--price")
    UPGRADE_PLAN = (By.XPATH, "//div[contains(@class, 'next-step--') and text()='Upgrade plan']")
    BACK_BTN1 = (By.XPATH, "//div[contains(@class, 'next-step-- black') and text()='<- Back']")
    BACK_BTN2 = (By.CSS_SELECTOR, ".back-text")

    def verify_sub_payments_page_opened(self):
        self.verify_partial_url('subscription')

    def verify_title_subscription_payments(self):
        self.verify_text('Subscription & payments', *self.SUB_PAY_TITLE)

    def verify_back_and_upgrade_plan_buttons(self):
        self.find_element(*self.BACK_BTN1)
        self.find_element(*self.BACK_BTN2)
        self.find_element(*self.UPGRADE_PLAN)
