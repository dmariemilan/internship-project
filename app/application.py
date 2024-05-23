from pages.account_side_nav import AccountSideNav
from pages.base_page import Page
from pages.cart_page import CartPage
from pages.header import Header
from pages.help_page import HelpPage
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.signin_page import SigninPage
from pages.target_app_page import TargetAppPage
from pages.privacy_policy_page import PrivacyPolicyPage
from pages.terms_and_conditions_page import TermsAndConditionsPage



class Application:

    def __init__(self, driver):
        self.account_side_nav = AccountSideNav(driver)
        self.base_page = Page(driver)
        self.cart_page = CartPage(driver)
        self.header = Header(driver)
        self.help_page = HelpPage(driver)
        self.main_page = MainPage(driver)
        self.search_result_page = SearchResultsPage(driver)
        self.signin_page = SigninPage(driver)
        self.target_app_page = TargetAppPage(driver)
        self.privacy_policy_page = PrivacyPolicyPage(driver)
        self.terms_and_conditions_page = TermsAndConditionsPage(driver)








