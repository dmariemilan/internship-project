from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

CTC_BTN = (By.CSS_SELECTOR, "div[class='get-free-period menu']")


@given('Open Reelly main page')
def open_reelly(context):
    context.app.main_page.open_main()


@when('Click on Connect the company')
def click_connect_button(context):
    context.app.main_page.click_connect_button()


@when('Switch to new window')
def switch_to_new_window(context):
    context.app.main_page.switch_to_new_window()
    sleep(5)





