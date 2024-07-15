from pages.base_page import Page
from pages.main_page import MainPage
from pages.sign_in_page import SignInPage
from pages.book_presentation_page import BookPresentationPage
from pages.mobile_settings_page import MobileSettingsPage
from pages.sign_up_page import SignUpPage
from pages.settings_page import SettingsPage


class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.book_presentation_page = BookPresentationPage(driver)
        self.main_page = MainPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.mobile_settings_page = MobileSettingsPage(driver)
        self.sign_up_page = SignUpPage(driver)
        self.settings_page = SettingsPage(driver)















