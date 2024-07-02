from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open Reelly sign up page')
def open_reelly_sign_up(context):
    context.app.sign_up_page.open_sign_up()


@when('Input a name and phone number')
def input_name_and_phone(context):
    context.app.sign_up_page.input_name_and_phone("Donna Test", "555-123-1234")


@when('Input an email and password')
def input_email_and_password(context):
    context.app.sign_up_page.input_email_and_password("donna.test@test.com", "D0nTest!")


@when('Input a company name')
def input_company_name(context):
    context.app.sign_up_page.input_company("Careerist")


@then('Verify input name is correct')
def verify_input_name(context):
    context.app.sign_up_page.verify_input_name("Donna Test")


@then('Verify phone number is correct')
def verify_phone(context):
    context.app.sign_up_page.verify_input_phone("555-123-1234")


@then('Verify email is correct')
def verify_email(context):
    context.app.sign_up_page.verify_input_email("donna.test@test.com")


@then('Verify password is correct')
def verify_password(context):
    context.app.sign_up_page.verify_input_password("D0nTest!")


@then('Verify company name is correct')
def verify_company(context):
    context.app.sign_up_page.verify_input_company("Careerist")



