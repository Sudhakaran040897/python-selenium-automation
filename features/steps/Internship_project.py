from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open the main page')
def main_page(context):
    context.app.internship_page.main_url()

@when("the user logs in with valid credentials")
def step_user_logs_in(context):
    context.main_page.login("sreekar.velluri@gmail.com", "Deadshotcrazy1@")

@then('Click on “settings” at the left side menu.')
def settings_menu(context):
    context.app.settings_menu.open_settings_page()

    sleep(5)



@then('Click on the verification option.')
def verification_option(context):
    verification_page = context.driver.find_element(By.CSS_SELECTOR, "[href='/verification/step-0']")
    context.driver.wait.until(EC.element_to_be_clickable(verification_page)).click()

@then('Verify the right page opens.')
def verify_right_page(context):
        Verification_page_valid = context.driver.find_element(By.CSS_SELECTOR, "[class='description-text']")
        print(f"verification page: {Verification_page_valid.text}")
        sleep(5)


@then('Verify “upload image” and “Next step” buttons are available.')
def buttons_available(context):
    upload_image = context.driver.find_element(By.CSS_SELECTOR, "[for='input_file']")
    print(f"upload image button visible: {upload_image.text}")
    Next_step = context.driver.find_element(By.CSS_SELECTOR, "[wized='nextButtonStep0']")
    print(f"Next step button visible: {Next_step.text}")