from lib2to3.fixes.fix_input import context

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)


@then('Verify search results shown')
def verify_search_results(context):
    expected_result = 'tea'
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'


@given('Open target circle page')
def target_circle(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')



@then('Verify there are {expected_amount} benefit cells')
def verify_header_links_amount(context, expected_amount):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[class*='h-margin-b-tiny']")
    print('\nFind elements:')
    print(links)
    print(type(len(links)))

    assert len(links) == int(expected_amount), f'Expected {expected_amount} links but got {len(links)}'

@when('Add the toy to cart')
def Add_to_cart(context):
    toy_element = context.driver.find_element(By.CSS_SELECTOR, "[aria-label='Add McFarlane Toys DC Comics Jokerized Scarecrow Action Figure (Target Exclusive) to cart']")
    sleep(10)
    toy_element.click()
    add_to_cart_button = context.driver.find_element(By.CSS_SELECTOR, "[data-test='shippingButton']")
    add_to_cart_button.click()
    sleep(3)


@when('Decline protection')
def Decline_protection(context):
    Decline_protection = context.driver.find_element(By.CSS_SELECTOR, "[data-test='espDrawerContent-declineCoverageButton']")
    Decline_protection.click()
    sleep(10)

@then("I should see the product in my cart")
def cart(context):
    add_cart = context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
    add_cart.click()
    sleep(10)
    click_total = context.driver.find_element(By.CSS_SELECTOR, "[class*='styles_buttonEnabledMenu']")
    click_total.click()
    sleep(5)


@then("Can see the total price")
def total_price(context):
    Total_Est = context.driver.find_element(By.CSS_SELECTOR, "[class='h-text-lg h-text-bold']")
    print(f"The total price in the cart is: {Total_Est}")
    assert Total_Est, "Total price is not displayed!"










