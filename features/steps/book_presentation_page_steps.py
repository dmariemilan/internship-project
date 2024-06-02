from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@then('Verify that URL has {partial_url}')
def verify_search_page_url(context, partial_url):
    context.app.book_presentation_page.verify_partial_url(partial_url)

