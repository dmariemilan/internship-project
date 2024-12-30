from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@then('Click on Developers filter at the top of the page')
def click_developers_filter(context):
    context.app.market_page.click_developers_filter()


@then('Verify all cards have license tag')
def verify_all_cards_have_license_tag(context):
    context.app.market_page.verify_all_cards_have_license_tag()



