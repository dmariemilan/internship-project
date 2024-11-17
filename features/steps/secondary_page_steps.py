from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@then('Go to the final page using the pagination button')
def go_to_final_page(context):
    context.app.secondary_page.go_to_final_page()


@then('Go back to the first page using the pagination button')
def go_to_first_page(context):
    context.app.secondary_page.go_to_final_page()


@then('Click on Filters')
def click_on_filters(context):
    context.app.secondary_page.click_on_filters()


@then('Filter the products by want to sell')
def click_want_to_sell(context):
    context.app.secondary_page.click_want_to_sell()


@then('Filter the products by want to buy')
def click_want_to_buy(context):
    context.app.secondary_page.click_want_to_buy()


@then('Click on Apply Filter')
def click_apply_filter(context):
    context.app.secondary_page.click_apply_filter()


@then('Verify all cards have for sale tag')
def verify_all_cards_have_for_sale_tag(context):
    context.app.secondary_page.verify_all_cards_have_for_sale_tag()


@then('Verify all cards have want to buy tag')
def verify_all_cards_have_want_to_buy_tag(context):
    context.app.secondary_page.verify_all_cards_have_want_to_buy_tag()



