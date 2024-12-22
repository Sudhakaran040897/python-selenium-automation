from behave import given, when, then

@given('Open the home page for Cart')
def open_main(context):
    context.app.main_page.open_main()


@when('Click on Cart icon button')
def search_product(context):
    context.app.header.cart_icon()

@then ('Verify “Your cart is empty” message')
def cart_message(context):
    context.app.cart.message()

