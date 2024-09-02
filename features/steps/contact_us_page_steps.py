from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep
from lib2to3.fixes.fix_input import context


@then('Verify contact us page URL {partial_url}')
def verify_contact_us_page_url(context, partial_url):
    context.app.contact_us_page.verify_partial_url(partial_url)


@then('Verify there are at least 4 social media icons')
def verify_social_media_icons(context):
    context.app.contact_us_page.verify_social_media_icons()


@then('Verify Connect the company button is available and clickable')
def verify_connect_company_btn(context):
    context.app.contact_us_page.verify_connect_company_btn()