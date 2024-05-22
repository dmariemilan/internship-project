from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
CART_SUMMARY = (By.CSS_SELECTOR, "[class*='CartSummarySpan']")
CART_VIEW_AND_SUMMARY = (By.CSS_SELECTOR, "a[href='/cart']")


@when('Click on view cart & and check out')
def click_on_view_cart(context):
    # context.driver.find_element(*CART_VIEW_AND_SUMMARY).click()
    # context.wait.until(
    #    EC.invisibility_of_element_located(CART_VIEW_AND_SUMMARY),
    #   message="View cart and Check Out did not disappear")
    context.app.cart_page.click_on_view_cart()


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    #cart_summary = context.driver.find_element(*CART_SUMMARY).text
    #assert amount in cart_summary, f'Expected {amount} items but got {cart_summary}'
    context.app.cart_page.verify_cart_items(amount)


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty_message(context):
    context.app.cart_page.verify_cart_is_empty()
    # context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']")


@then('Verify cart has correct product')
def verify_product_name(context):
    context.app.cart_page.verify_product_name('coffee')







