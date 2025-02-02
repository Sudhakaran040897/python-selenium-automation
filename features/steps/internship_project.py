from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@given('Open the main page')
def main_page(context):
    context.app.internship_page.main_url()


@when('Log in to the page')
def login_page(context):
    context.app.login_page.login_user("sreekar.velluri@gmail.com", "Deadshotcrazy1@")



@when('the user clicks on "settings" in the left menu')
def step_user_clicks_settings(context):
    context.app.settings_page.open_settings()
    sleep(5)



@when('the user clicks on the "verification" option')
def step_user_clicks_verification(context):
    context.app.settings_page.open_verification()
    sleep(5)


@then("the verification page should open")
def step_verify_verification_page(context):
    assert context.app.settings_page.is_verification_page_open(), "Verification page did not open."


@then('"upload image" and "Next step" buttons should be available')
def step_verify_buttons(context):
    assert context.app.settings_page.are_buttons_present(), "'Upload image' or 'Next step' buttons are missing."