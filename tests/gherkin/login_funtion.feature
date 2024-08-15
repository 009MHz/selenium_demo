### Part 1: Login Functionality
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

### Part 2: File Uploader
Scenario: Successful File Upload
  Given I am on the file uploader page
  When I upload a valid file
    And I click on the "Upload" button
  Then I should see the name of the uploaded file displayed on the page

Scenario: Attempt to Upload Without Selecting a File
  Given I am on the file uploader page
  When I do not select a file
    And I click on the "Upload" button
  Then I should see an error message or no file name should be displayed

Scenario: Upload of a File with a Specific Format
  Given I am on the file uploader page
  When I upload a file with a specific format (e.g., .txt, .jpg)
    And I click on the "Upload" button
  Then I should see the name of the uploaded file displayed on the page
    And the file should be accepted if it matches the allowed formats

### Part 3: Missing Element Page
Scenario: Handle Missing Element Gracefully
  Given I am on the missing element page
  When a specific element (e.g., a button or a text) is missing from the page
  Then the page should load without breaking
    And a placeholder or an appropriate message should be displayed

Scenario: Interaction with a Dynamically Loaded Element
  Given I am on the missing element page
  When the element is not initially present
    And the element loads dynamically after some time
  Then I should be able to interact with the element once it appears
    And the page should function as expected without any errors
