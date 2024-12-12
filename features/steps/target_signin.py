from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

@given ("Open target.com")
def open_main(context):
    context.driver.get("https://www.target.com/")

@when ("Click on Cart icon")
def click_cart(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']").click()

@then ("Your cart is empty")
def verify_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[height='150']")


@when("Click on Sign in")
def click_signin(context):
    context.driver.find_element(By.CSS_SELECTOR, "[id*='sign-in']").click()
    sleep(1)


@then("On navigation menu, click on signin")
def navigation_nenu (context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()


@then("Verify Sign In form opened")
def verify_signin (context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='lnvRvp ']")
