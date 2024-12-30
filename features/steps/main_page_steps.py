from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open Reelly main page')
def open_reelly(context):
    context.app.main_page.open_main()


@when('Click on Connect the company')
def click_connect_button(context):
    context.app.main_page.click_connect_button()


@when('Click on Mobile Menu button')
def click_mobile_menu_button(context):
    context.app.main_page.click_mobile_menu_button()


@when('Switch to new window')
def switch_to_new_window(context):
    context.app.main_page.switch_to_new_window()
    sleep(5)


@when('Click on settings option')
def click_settings_option(context):
    context.app.main_page.click_settings_option()


@when('Click on main menu option')
def click_main_menu_option(context):
    context.app.main_page.click_main_menu_option()


@when('Click on secondary option')
def click_secondary_option(context):
    context.app.main_page.click_secondary_option()


@when('Click on off plan side option')
def click_on_off_plan_side_option(context):
    context.app.main_page.click_on_off_plan_side_option()


@then('Click on off plan Filter')
def click_on_off_plan_filter(context):
    context.app.main_page.click_on_off_plan_filter()


@then('Click on off plan Apply Filter')
def click_on_off_plan_apply_filter(context):
    context.app.main_page.click_on_off_plan_apply_filter()


@then("Verify the price in all cards is in the range (1200000 - 2000000)")
def verify_price_in_range(context):
    context.app.main_page.verify_price_in_range()


@then('Verify each product on the page contains a title and a picture')
def verify_product_contains_title_and_image(context):
    context.app.main_page.verify_product_contains_title_and_image()


@then('Click on sales status filter')
def click_on_sales_status_filter(context):
    context.app.main_page.click_on_sales_status_filter()


@then('Click on out of stock')
def click_on_out_of_stock(context):
    context.app.main_page.click_on_out_of_stock()


@then('Verify all cards have Out of Stock tag')
def verify_all_cards_have_out_of_stock_tag(context):
    context.app.main_page.verify_all_cards_have_out_of_stock_tag()


@when('Click on the first product')
def click_on_first_product(context):
    context.app.main_page.click_on_first_product()


@when('Click on market side option')
def click_market_option(context):
    context.app.main_page.click_market_option()













