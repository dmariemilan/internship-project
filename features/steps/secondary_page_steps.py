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

