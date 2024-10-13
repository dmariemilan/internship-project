from pages.base_page import Page
from pages.main_page import MainPage
from pages.sign_in_page import SignInPage
from pages.book_presentation_page import BookPresentationPage
from pages.mobile_settings_page import MobileSettingsPage
from pages.sign_up_page import SignUpPage
from pages.settings_page import SettingsPage
from pages.profile_page import ProfilePage
from pages.main_menu_page import MainMenuPage
from pages.add_project_page import AddProjectPage
from pages.community_page import CommunityPage
from pages.contact_us_page import ContactUsPage
from pages.user_guide_page import UserGuidePage
from pages.change_password_page import ChangePasswordPage
from pages.sub_and_payments_page import SubAndPaymentsPage
from pages.support_whatsapp_page import SupportWhatsappPage
from pages.news_telegram_page import NewsTelegramPage


class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.book_presentation_page = BookPresentationPage(driver)
        self.main_page = MainPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.mobile_settings_page = MobileSettingsPage(driver)
        self.sign_up_page = SignUpPage(driver)
        self.settings_page = SettingsPage(driver)
        self.profile_page = ProfilePage(driver)
        self.main_menu_page = MainMenuPage(driver)
        self.add_project_page = AddProjectPage(driver)
        self.community_page = CommunityPage(driver)
        self.contact_us_page = ContactUsPage(driver)
        self.user_guide_page = UserGuidePage(driver)
        self.change_password_page = ChangePasswordPage(driver)
        self.sub_and_payments_page = SubAndPaymentsPage(driver)
        self.support_whatsapp_page = SupportWhatsappPage(driver)
        self.news_telegram_page = NewsTelegramPage(driver)


























