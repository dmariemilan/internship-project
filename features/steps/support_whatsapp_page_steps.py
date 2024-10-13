from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@then('Switch back to Settings page')
def switch_back_to_settings_page(context):
    context.app.support_whatsapp_page.switch_back_to_settings_page()
