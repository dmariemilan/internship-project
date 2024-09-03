from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep
from lib2to3.fixes.fix_input import context


@then('Verify user guide page URL {partial_url}')
def verify_user_guide_page_url(context, partial_url):
    context.app.user_guide_page.verify_partial_url(partial_url)


@then('Verify all lesson videos contain titles')
def verify_video_titles(context):
    context.app.user_guide_page.verify_video_titles()


