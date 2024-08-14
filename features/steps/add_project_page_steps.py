from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@then('Verify project page URL {partial_url}')
def verify_project_page_url(context, partial_url):
    context.app.add_project_page.verify_partial_url(partial_url)


@then('Add some test information to the input fields')
def test_information(context):
    context.app.add_project_page.test_information()


@then('Verify the right information is present in the input fields')
def verify_right_information(context):
    context.app.add_project_page.verify_right_information()


@then('Verify Send an application button is available and clickable')
def click_application_btn(context):
    context.app.add_project_page.click_application_btn()
