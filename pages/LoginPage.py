from playwright.sync_api import Page, expect
from pages.Base_page import BasePage
from utilities.test_data import TestData
from utilities.common import logger
from locators.Login_locators import LoginPageLocators
from utilities.credentials import get_user, get_passwd


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    # ----------Locators----------
    @property
    def logo(self):
        return self.page.locator(LoginPageLocators.LOGO)

    @property
    def user_name(self):
        return self.page.locator(LoginPageLocators.USER_NAME)
    @property
    def password(self):
        return self.page.locator(LoginPageLocators.PASSWORD)

    @property
    def submit(self):
        return self.page.locator(LoginPageLocators.SUBMIT)
    @property
    def error_container(self):
        return self.page.locator(LoginPageLocators.ERROR)

    @property
    def cross_btn(self):
        return self.page.locator(LoginPageLocators.CROSS_ERROR)
    # ----------Actions----------
    def open(self):
        self.page.goto(TestData.BASE_URL)
        

    def fill_credentials(self, user_key: str):
        logger.info("Filling credentials")
        user = get_user(user_key)
        if user is None:
            user = user_key
        self.user_name.type(user)
        self.password.type(get_passwd() or "secret_sauce")

    def click_login(self):
        logger.info("Logging in...")
        self.submit.click()

    def cancel_error(self):
        self.cross_btn.click()
        logger.info("Closed error message")

    # ----------Assertions----------
    def assert_username_password(self):
        expect(self.error_container).to_be_visible()
        assert (
            "Epic sadface: Username is required"
            or "Epic sadface: Password is required"
            or "Epic sadface: Username and password do not match any user in this service" in self.error_container.inner_text()
        ), self.error_container.inner_text()

    def assert_locked_out_error(self):
        expect(self.error_container).to_be_visible()
        expect(self.error_container).to_contain_text(
            "Epic sadface: Sorry, this user has been locked out."
        )
        
    def verify_login_page(self):
        logger.info("Verifying Login Page")
        expect(self.logo, "'Swag Labs' logo should be visible").to_be_visible()
