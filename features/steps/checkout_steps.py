from behave import when, then
from pages.Checkout_page import CheckoutPage


@then("Verify user should be navigated to the checkout page")
def step_verify_checkout_page(context):
    context.checkout_page = CheckoutPage(context.page)
    context.checkout_page.verify_open()


@when("User clicks cancel on checkout overview page")
def step_click_cancel(context):
    context.checkout_page.cancel_checkout()


@then("User clicks continue from checkout overview page")
def step_continue_from_checkout(context):
    context.checkout_page.click_continue_checkout()


@then("Verify '{error}' should be displayed")
def step_verify_last_name_error(context):
    context.checkout_page.assert_lastname(context.error)
