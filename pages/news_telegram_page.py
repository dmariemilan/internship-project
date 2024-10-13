from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page


class NewsTelegramPage(Page):

    def verify_news_page_opened(self):
        self.verify_partial_url('t.me')
