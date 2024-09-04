from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@then('Verify settings page URL {partial_url}')
def verify_settings_page_url(context, partial_url):
    context.app.settings_page.verify_partial_url(partial_url)


@then('Verify page has {expected_amount} options')
def verify_settings_options(context, expected_amount):
    expected_amount = int(expected_amount)
    context.app.settings_page.verify_settings_options(expected_amount)


@then('Verify connect the company button present')
def verify_connect_button(context):
    context.app.settings_page.verify_connect_button()


@when('Click on Edit profile')
def click_edit_profile(context):
    context.app.settings_page.click_edit_profile()


@when('Click on Add a project')
def click_add_a_project(context):
    context.app.settings_page.click_add_a_project()


@when('Click on Community')
def click_community(context):
    context.app.settings_page.click_community()


@when('Click on Contact us')
def click_contact_us(context):
    context.app.settings_page.click_contact_us()


@when('Click on User guide')
def click_user_guide(context):
    context.app.settings_page.click_user_guide()


@when('Click on Change password')
def click_change_password(context):
    context.app.settings_page.click_change_password()








