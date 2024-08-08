from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep
from lib2to3.fixes.fix_input import context


@when("Change the language of the page to Russian")
def change_language(context):
    context.app.main_menu_page.change_language()


@then("Verify the language has changed")
def verify_language(context):
    context.app.main_menu_page.verify_language()