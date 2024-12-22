from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from behave import given, when, then




CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")

@given('Open target main page')
def open_main(context):
    context.app.main_page.open_main()


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product(product)


@then('Verify search results shown for {product}')
def verify_search_results(context, product):
    context.app.search_results_page.verify_search_results(product)



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
    toy_element = context.driver.find_element(By.CSS_SELECTOR,"[data-focusid*='89198670']")
    context.driver.wait.until(EC.element_to_be_clickable(toy_element)).click()
    add_to_cart_button = context.driver.find_element(By.CSS_SELECTOR, "[data-test='shippingButton']")
    context.driver.wait.until(EC.element_to_be_clickable(add_to_cart_button)).click()


@when('Decline protection')
def Decline_protection(context):
    Decline_protection = context.driver.find_element(By.CSS_SELECTOR, "[data-test='espDrawerContent-declineCoverageButton']")
    context.driver.wait.until(EC.element_to_be_clickable(Decline_protection)).click()


@then("I should see the product in my cart")
def cart(context):
    add_cart = context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
    context.driver.wait.until(EC.element_to_be_clickable(add_cart)).click()
    click_total = context.driver.find_element(By.CSS_SELECTOR, "[class*='styles_buttonEnabledMenu']")
    context.driver.wait.until(EC.element_to_be_clickable(click_total)).click()



@then("Can see the total price")
def total_price(context):
    Total_Est = context.driver.find_element(By.CSS_SELECTOR, "[class='h-text-lg h-text-bold']")
    print(f"The total price in the cart is: {Total_Est}")
    assert Total_Est, "Total price is not displayed!"










