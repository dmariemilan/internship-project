from pages.base_page import Page
from pages.main_page import MainPage
from pages.sign_in_page import SignInPage
from pages.book_presentation_page import BookPresentationPage



class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.book_presentation_page = BookPresentationPage(driver)
        self.main_page = MainPage(driver)
        self.sign_in_page = SignInPage(driver)












