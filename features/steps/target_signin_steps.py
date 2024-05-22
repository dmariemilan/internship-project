from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SIGNIN_PAGE_HEADER = (By.XPATH, "//span[text()='Sign into your Target account']")


@when('Click sign in from top navigation')
def click_sign_in_from_top_navigation(context):
    context.app.header.click_signin()


@when('Click sign in from side navigation menu')
def click_sign_in_from_side_navigation(context):
    context.app.account_side_nav.click_sign_in()


@then('Verify {expected_text} is displayed')
def verify_sign_in_form_opened(context, expected_text):
    context.app.signin_page.verify_login_page(expected_text)


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.signin_page.get_current_window()


@when('Click Terms and Conditions Link')
def click_tc_link(context):
    context.app.signin_page.click_tc_link()


@then('Verify Terms and Conditions page opened')
def verify_tc_opened(context):
    context.app.terms_and_conditions_page.verify_tc_opened()

