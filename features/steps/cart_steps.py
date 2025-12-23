from behave import given, when, then
from pages.Cart_page import CartPage


@when("User clicks on the cart icon")
def step_click_cart_icon(context):
    context.inventory_page.click_cart_icon()
    context.cart_page = CartPage(context.page)
    
@then("User navigates to the cart page")
def step_verify_on_cart(context):
    context.cart_page.verify_cart_open()


@when("User clicks on continue button")
def step_procced_to_checkout(context):
    context.cart_page.click_continue_button()


@when("User adds item '{item}' to the cart")
def step_add_item_to_cart(context, item):
    context.inventory_page.add_to_cart(item)


@when("User removes item '{item}' from the cart")
def step_remove_item_from_cart(context, item):
    context.inventory_page.remove_from_cart(item)


@then("Verify cart badge should show the correct number of items")
def step_verify_cart_badge(context):
    context.inventory_page.assert_badge_count(context.inventory_page.cart_count)


@then("Verify the items in cart")
def step_verify_item_in_cart(context):
    context.cart_page.verify_cart_items(context.inventory_page.cart_count)
