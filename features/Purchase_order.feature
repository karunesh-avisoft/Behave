Feature: Successfull Purchase Order Flow

	Background: User should be logged in as standard user and on inventory page
		Given User login as 'standard' user
		Then Verify user is on the inventory page

	Scenario: Verify successful completion of an order purchase
		When User adds item 'backpack' to the cart
		And User adds item 'fleece jacket' to the cart
		And User clicks on the cart icon
		And User clicks on continue button
		And User fills checkout details with first name:'John', last name:'Doe', and postal code:'12345'
		Then User clicks continue from checkout overview page
		When User verifies total amount as well as finishes the order
		Then Verify user should see the order confirmation page


