from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page


class CommunityPage(Page):
    CONTACT_SUPPORT_BTN = (By.CSS_SELECTOR, 'div[class="community-cards"] a[href*="https://t.me/reelly_dubai_bot"][id*="w-node-f"]')
    #CONTACT_SUPPORT_BTN = (By.ID, "w-node-f7ead340-ee2a-2b84-cdd5-5a35322aacbf-7f66deba")
    #CONTACT_SUPPORT_BTN = (By.CSS_SELECTOR, "[href*='community'].page-setting-block")
    #CONTACT_SUPPORT_BTN = (By.XPATH, "//*[text()='Contact support']")

    def verify_community_page_opened(self):
        self.verify_partial_url('community')
        sleep(10)

    def click_contact_support_btn(self):
        sleep(5)
        self.wait_until_clickable_click(*self.CONTACT_SUPPORT_BTN)
        #contact_support_btn = self.find_element(*self.CONTACT_SUPPORT_BTN)
        #contact_support_btn.click()
        sleep(4)
