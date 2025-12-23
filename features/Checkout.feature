Feature: Checkout Page

	Background: User successfully logged in as standard user and redirected to inventory page
		Given User login as 'problem' user
		Then Verify user is on the inventory page
		When User adds item 'backpack' to the cart
		And User adds item 'Onesie' to the cart
		And User clicks on the cart icon
		And User clicks on continue button
		Then Verify user should be navigated to the checkout page
		
	Scenario: Verify cancel checkout action
		When User clicks cancel on checkout overview page
		Then Verify user navigates to the cart page	
		And Verify cart badge should show the correct number of items

	Scenario: Verify error on empty checkout fields
		When User fills checkout details with first name:'John', last name:'Problem', and postal code:'12345'
		Then User clicks continue from checkout overview page
		And Verify 'Error: Last Name is required' should be displayed