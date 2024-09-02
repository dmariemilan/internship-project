from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@then('Verify community page URL {partial_url}')
def verify_community_page_url(context, partial_url):
    context.app.community_page.verify_partial_url(partial_url)


@then('Verify Contact support button is available and clickable')
def click_contact_support_btn(context):
    context.app.community_page.click_contact_support_btn()





