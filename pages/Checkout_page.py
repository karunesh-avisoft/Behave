from playwright.sync_api import Page, expect
import  re
from pages.Base_page import BasePage
from locators.Cart_checkout_locators import CartCheckoutLocators  
from utilities.common import logger
from utilities.test_data import TestData

class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page) 
        self.firstName = ''
        self.lastName = ''      
        self.postalCode = '' 

    # ----------Locators----------
    @property
    def first_name_input(self):
        return self.page.locator(CartCheckoutLocators.FIRSTNAME)
    @property
    def last_name_input(self):
        return self.page.locator(CartCheckoutLocators.LASTNAME)
    @property
    def postal_code_input(self):
        return self.page.locator(CartCheckoutLocators.POSTALCODE)
    @property
    def continue_button(self):
        return self.page.locator(CartCheckoutLocators.CONTINUE)
    @property
    def title(self):
        return self.page.locator(CartCheckoutLocators.TITLE)
    @property
    def finish_button(self):
        return self.page.locator(CartCheckoutLocators.FINISH)
    @property
    def complition_msg(self):
        return self.page.locator(CartCheckoutLocators.COMPLETE_HEADING)
    @property
    def error_container(self):
        return self.page.locator(CartCheckoutLocators.ERROR)
    @property
    def back_home(self):
        return self.page.locator(CartCheckoutLocators.BACK_HOME)
    @property
    def cancel(self):
        return self.page.locator(CartCheckoutLocators.CANCEL)

    # ----------Actions----------
    def verify_open(self):
        logger.info('Verifying checkout page is open')
        expect(self.page).to_have_url(TestData.CHECKOUT_URL)
        logger.info('Checkout page is open')
    
    def cancel_checkout(self):
        logger.info('Cancelling checkout')
        self.cancel.click()
    
    def fill_checkout_details(self, firstName:str, lastName:str, postalCode:int):
        self.firstName = firstName
        self.lastName = lastName        
        self.postalCode = postalCode
        logger.info('Filling checkout information')
        self.first_name_input.type(firstName)
        self.last_name_input.type(lastName)
        self.postal_code_input.press_sequentially(str(postalCode))
        
    def click_continue_checkout(self):
        logger.info('Submitting checkout information')
        self.continue_button.click()
        
    def verify_checkout_overview(self):
        logger.info('Verifying checkout overview page is open')
        expect(self.title).to_contain_text('Overview')
    
    def verify_total_amount(self, total_item_amt: str):
        logger.info('Verifying total amount on checkout overview page')
        total_text = self.page.locator(CartCheckoutLocators.TOTAL).text_content()
        total_price = float(re.search(r'([\d]+\.\d{2})', total_text).group(1))
        # Tax addition at 0.08
        tax = total_item_amt*float(TestData.TAX_RATE)
        expected_total = round(total_item_amt + tax, 2)
        assert expected_total == total_price, f"Expected total '{expected_total}' not found in '{total_price}'"
        logger.info('Total amount verified successfully')
    
    def finish_checkout(self):
        logger.info('Finishing checkout process')
        self.finish_button.click()
        
    def verify_order_completion(self):
        expect(self.complition_msg).to_contain_text('Thank you for your order')
        logger.info('Order completed successfully')
    
    def back_to_home(self):
        self.back_home.click()
        
    # ---------- Assertions ----------
    def assert_lastname(self, error):
        expect(self.error_container).to_be_visible()
        expect(self.error_container, "Error: Last Name is required").to_have_text(error)

        
    def assert_checkout_details(self):
        expect(self.last_name_input, 'Should have last name.').to_have_text(self.lastName)
        expect(self.first_name_input, 'Should have first name.').to_have_text(self.firstName)
        expect(self.postal_code_input, 'Should have postal code.').to_have_text(str(self.postalCode))

    def assert_finish_button(self):
        expect(self.page,"Navigation to order completion stopped for error user.").to_have_url(TestData.CHECKOUT_URL)