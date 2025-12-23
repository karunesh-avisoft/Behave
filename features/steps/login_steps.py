from behave import given, when, then
from playwright.sync_api import sync_playwright
from pages.LoginPage import LoginPage


@given("User login as '{username}' user")
def step_user_login(context, username):
    context.login_page = LoginPage(context.page)
    context.login_page.open()
    context.login_page.fill_credentials(username)
    context.login_page.click_login()


@given("User should be on the login page")
def user_login_page(context):
    context.login_page = LoginPage(context.page)
    context.login_page.open()
    context.login_page.verify_login_page()
    context.login_page.take_screenshot("login_page")


@when("User enters '{username}' as username")
def user_enter_credentials(context, username):
    context.login_page.fill_credentials(username)


@when("User click on the login button")
def user_submit_login_form(context):
    context.login_page.click_login()
    context.login_page.take_screenshot("after_click_login")


@then("Verify user should see error '{error}'")
def user_should_see_error_message(context, error):
    context.login_page.assert_username_password(error)
    context.login_page.take_screenshot("login_error_message")
