from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@then("Verify the three options of visualization are 'architecture', 'interior', 'lobby'")
def verify_three_options_of_visualization(context):
    context.app.off_plan_pdp.verify_three_options_of_visualization()


@then('Verify the visualization options are clickable')
def verify_the_visualization_options_are_clickable(context):
    context.app.off_plan_pdp.verify_the_visualization_options_are_clickable()
