from asyncio import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open the main page')
def main_page(context):
    context.app.internship_page.main_url()

@when('Log in to the page')
def login_page(context):
    Login_user = context.driver.find_element(By.CSS_SELECTOR, "[class*='button-hero gray w-inline-block']").click()

    email_input = context.driver.find_element(By.CSS_SELECTOR, "[wized='emailInput']")  # Update with the actual selector
    email_input.send_keys("sreekar.velluri@gmail.com")
    context.driver.wait.until(EC.element_to_be_clickable(email_input)).click()

    password_input = context.driver.find_element(By.CSS_SELECTOR,"[wized='passwordInput']")
    password_input.send_keys("Deadshotcrazy1@")
    context.driver.wait.until(EC.element_to_be_clickable(password_input)).click()

    login_submit = context.driver.find_element(By.CSS_SELECTOR, "[class='login-button w-button']")
    context.driver.wait.until(EC.element_to_be_clickable(login_submit)).click()

@then('Click on “settings” at the left side menu.')
def settings_menu(context):
    settings = context.driver.find_element(By.XPATH, "//div[@class='menu-button-text' and text()='Settings']")
    settings.click()

@then('Click on the verification option.')
def verification_option(context):
    verification_page = context.driver.find_element(By.CSS_SELECTOR, "[href='/verification/step-0']").click()

@then('Verify the right page opens.')
def verify_right_page(context):
        Verification_page_valid = context.driver.find_element(By.CSS_SELECTOR, "[class='lotion-your-h3']")
        print(f"verification page: {Verification_page_valid.text}")


@then('Verify “upload image” and “Next step” buttons are available.')
def buttons_available(context):
    upload_image = context.driver.find_element(By.CSS_SELECTOR, "[for='input_file']")
    print(f"upload image button visible: {upload_image.text}")
    Next_step = context.driver.find_element(By.CSS_SELECTOR, "[wized='nextButtonStep0']")
    print(f"Next step button visible: {Next_step.text}")