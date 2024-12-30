from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page


class OffPlanPdp(Page):
    ARCHITECTURE_BTN = (By.ID, 'w-tabs-0-data-w-tab-0')
    INTERIOR_BTN = (By.ID, 'w-tabs-0-data-w-tab-1')
    LOBBY_BTN = (By.ID, 'w-tabs-0-data-w-tab-2')

    def verify_three_options_of_visualization(self):
        self.verify_text('Architecture', *self.ARCHITECTURE_BTN)
        self.verify_text('Interior', *self.INTERIOR_BTN)
        self.verify_text('Lobby', *self.LOBBY_BTN)

    def verify_the_visualization_options_are_clickable(self):
        self.wait_until_clickable_click(*self.ARCHITECTURE_BTN)
        self.wait_until_clickable_click(*self.INTERIOR_BTN)
        self.wait_until_clickable_click(*self.LOBBY_BTN)




