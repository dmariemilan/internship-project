from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


BENEFIT_CELLS = (By.CSS_SELECTOR, "[class*='CellItemContainer']")


@given('Open Target circle page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/circle')


#@then('Verify 10 benefit cells are shown')


@then('Verify page has {expected_amount} cells')
def verify_target_circle(context, expected_amount):
    expected_amount = int(expected_amount)
    cells = context.driver.find_elements(*BENEFIT_CELLS)
    assert len(cells) == expected_amount, f'Expected {expected_amount} cells but got {len(cells)}'


