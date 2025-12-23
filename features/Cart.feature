Feature: Cart Management

    Background: User successfully logged in as standard user and redirected to inventory page
        Given User login as 'standard' user
        Then Verify user is on the inventory page
    
    Scenario: Verify cart updates after adding items
		When User adds item 'bolt t-shirt' to the cart
		Then Verify cart badge should show the correct number of items

	Scenario: Verify cart updates after removing items
		When User adds item 'bike light' to the cart
		And User adds item 'bolt t-shirt' to the cart
		And User removes item 'bike light' from the cart
		Then Verify cart badge should show the correct number of items

    Scenario: Verify items and navigation to checkout page from cart
        When User adds item 'bike light' to the cart
		And User adds item 'bolt t-shirt' to the cart
        And User clicks on the cart icon
        Then Verify the items in cart
        When User clicks on continue button
        Then Verify user should be navigated to the checkout page