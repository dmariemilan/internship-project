from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep
from lib2to3.fixes.fix_input import context


@then('Verify change password page URL {partial_url}')
def verify_change_password_page_url(context, partial_url):
    context.app.change_password_page.verify_partial_url(partial_url)


@then('Add some test password to the input fields')
def password_information(context):
    context.app.change_password_page.password_information()


@then('Verify the Change password button is available')
def change_password_btn(context):
    context.app.change_password_page.change_password_btn()




