from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on Mobile Connect the company')
def click_mobile_connect_button(context):
    context.app.mobile_settings_page.click_mobile_connect_button()


