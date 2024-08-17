Feature: Login Functionality
  As a user
  I want to be able to log in to the secure area
  So that I can access protected resources

  Scenario: Password field is masked by dot
    Given I am on the Login Page
    When I enter "T|-|!s I5 Sp#ci@l TeXt P4sSw012D" into the password field
    Then the password field should be masked by dots

  Scenario: Username input is not masked by dot
    Given I am on the Login Page
    When I enter "T|-|!s I5 Sp#ci@l TeXt UserN@m3" into the username field
    Then the username field should not be masked

  Scenario: Successful Login with Correct Credentials
    Given I am on the Login Page
    When I enter "tomsmith" into the username field
    And I enter "SuperSecretPassword!" into the password field
    And I click the "Login" button
    Then I should be redirected to a URL containing "/secure"
    And I should see a success toast message containing "You logged into"
    And the page title should be "Secure Area"
    And the success page sub-header should contain "When you are done"
    And the "Logout" button should be visible and enabled

  Scenario: Unsuccessful Login with Invalid Username
    Given I am on the Login Page
    When I enter "invalid_username" into the username field
    And I enter "SuperSecretPassword!" into the password field
    And I click the "Login" button
    Then I should remain on the login page
    And I should see a failure toast message containing "username is invalid!"

  Scenario: Unsuccessful Login with Invalid Password
    Given I am on the Login Page
    When I enter "tomsmith" into the username field
    And I enter "invalid_password" into the password field
    And I click the "Login" button
    Then I should remain on the login page
    And I should see a failure toast message containing "password is invalid!"

  Scenario: Unsuccessful Login with Invalid Credentials
    Given I am on the Login Page
    When I enter "invalid_username" into the username field
    And I enter "invalid_password" into the password field
    And I click the "Login" button
    Then I should remain on the login page
    And I should see a failure toast message containing "username is invalid!"

  Scenario: Unsuccessful Login with Empty Fields
    Given I am on the Login Page
    When I click the "Login" button without entering credentials
    Then I should remain on the login page
    And I should see a failure toast message containing "username is invalid!"
