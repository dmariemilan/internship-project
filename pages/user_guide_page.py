from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page

class UserGuidePage(Page):
    VIDEO_TITLES = (By.CSS_SELECTOR, "a[data-sessionlink='feature=player-title']")

    def verify_user_guide_page_opened(self):
        self.verify_partial_url('user-guide')

    def verify_video_titles(self):
        lesson_titles = self.find_elements(*self.VIDEO_TITLES)

        for title in lesson_titles:
            assert title.text, f'Video lesson does not have a title for {title.text}'




