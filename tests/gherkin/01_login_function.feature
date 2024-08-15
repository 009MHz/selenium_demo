Scenario: Successful Login with Correct Credentials
  Given I am on the login page
    And the "Username" field is visible
    And the "Password" field is visible
  When I enter valid credentials ("username" and "password")
    And I click on the "Login" button
  Then I should be redirected to the secure area
    And I should see a message "You logged into a secure area!"

Scenario: Unsuccessful Login with Incorrect Credentials
  Given I am on the login page
    And the "Username" field is visible
    And the "Password" field is visible
  When I enter invalid credentials ("invalid_user" and "invalid_password")
    And I click on the "Login" button
  Then I should see an error message "Your username is invalid!" or "Your password is invalid!"

Scenario: Password Field Masking
  Given I am on the login page
  When I enter text into the "Password" field
  Then the characters in the "Password" field should be masked
    And the password should not be visible in plain text

Scenario: Login with Empty Username
  Given I am on the login page
    And the "Username" field is empty
    And the "Password" field contains valid text
  When I click on the "Login" button
  Then I should see an error message "Your username is invalid!"

Scenario: Login with Empty Password
  Given I am on the login page
    And the "Username" field contains valid text
    And the "Password" field is empty
  When I click on the "Login" button
  Then I should see an error message "Your password is invalid!"
