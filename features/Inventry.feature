Feature: Inventory Management

	Background: User should be logged in and on inventory page
		Given User login as 'standard' user
		Then Verify user is on the inventory page

	Scenario: Verify available products on inventory page
		Then Verify user should see 6 products listed
	
	Scenario Outline: Verify sorting of products by different options
		When The user sort products by '<sort_option>'
		Then Verify the products should be sorted by '<sort_type>' order

		Examples:
			| sort_option             | sort_type        |
			| az                      | name ascending   |
			| za                      | name descending  |
			| lohi                    | price ascending  |
			| hilo                    | price descending |

	Scenario: Verify logout from inventory page
		When User logs out from the application
		Then Verify user should be redirected to the login page