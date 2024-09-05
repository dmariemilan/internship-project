from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@then('Verify subscription payments page URL {partial_url}')
def verify_sub_payments_page_url(context, partial_url):
    context.app.sub_and_payments_page.verify_partial_url(partial_url)


@then('Verify title Subscription & payments is visible')
def verify_title_subscription_payments(context):
    context.app.sub_and_payments_page.verify_title_subscription_payments()


@then('Verify back and upgrade plan buttons are available')
def verify_back_and_upgrade_plan_buttons(context):
    context.app.sub_and_payments_page.verify_back_and_upgrade_plan_buttons()

