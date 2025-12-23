from behave import given, when, then
from pages.Inventory_page import InventoryPage


@then("Verify user is on the inventory page")
def user_should_be_on_inventory_page(context):
    context.inventory_page = InventoryPage(context.page)
    context.inventory_page.verify_inventory_page()


@then("Verify user should see 6 products listed")
def user_should_see_products(context):
    context.inventory_page.verify_products()


@when("The user sort products by '{sort_option}'")
def step_sort_products(context, sort_option):
    context.inventory_page.apply_sort(sort_option)


@then("Verify the products should be sorted by '{sort_type}' order")
def step_verify_sorted_products(context, sort_type):
    context.inventory_page.assert_sort_order(sort_type)


@when("User logs out from the application")
def step_log_out(context):
    context.inventory_page.log_out()


@then("Verify user should be redirected to the login page")
def step_verify_logout(context):
    context.inventory_page.assert_logout()
