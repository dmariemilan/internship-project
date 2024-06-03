from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


USER_EMAIL = (By.ID, "email-2")
USER_PASSWORD = (By.ID, "field")
CONTINUE_BTN = (By.CSS_SELECTOR, "a[class='login-button w-button']")


@when('Input user email and password and sign in')
def input_email_and_password(context):
    context.app.sign_in_page.input_email_and_password("donna.milan123@gmail.com", "D0nRee1lly!")














