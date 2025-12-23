Feature: User Login Page
	
	@valid_login
	Scenario: Verify successful user login with valid username
		Given User should be on the login page
		When User enters 'standard' as username
		And User click on the login button
		Then Verify user is on the inventory page
	
	@invalid_login
	Scenario: Verify unsuccessful user login with incorrect username
		Given User should be on the login page
		When User enters 'wrongUser' as username
		And User click on the login button
		Then Verify user should see error 'Epic sadface: Username and password do not match any user in this service'

	