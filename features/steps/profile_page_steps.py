from lib2to3.fixes.fix_input import context

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Enter test data into the name field: {name}')
def input_name(context, name):
    context.app.profile_page.input_name(name)


@when('Enter test data into the phone number field: {number}')
def input_number(context, number):
    context.app.profile_page.input_number(number)


@when('Enter test data into the company field: {test}')
def input_company(context, test):
    context.app.profile_page.input_company(test)


@when('Enter test data into the email field: {email}')
def input_email(context, email):
    context.app.profile_page.input_email(email)


@then('Verify the correct information is present in the name input field')
def verify_input_name(context):
    context.app.profile_page.verify_input_name("Test Test")


@then('Verify the correct information is present in the phone number input field')
def verify_input_phone(context):
    context.app.profile_page.verify_input_phone("555 555 5555")


@then('Verify the correct information is present in th company input field')
def verify_input_company(context):
    context.app.profile_page.verify_input_company("Testing")


@then('Verify the correct information is present in the email input field')
def verify_input_email(context):
    context.app.profile_page.verify_input_email("test@tester.com")


@then('Check "Save Changes" button is available and clickable')
def click_save_changes_btn(context):
    context.app.profile_page.click_save_changes_btn()


@then('Check "Close" button is available and clickable')
def click_close_btn(context):
    context.app.profile_page.click_close_btn()

