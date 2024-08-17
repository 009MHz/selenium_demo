Feature: Element Disappearance on the Add/Remove Elements Page
  As a user
  I want to interact with the Add/Remove Elements page
  So that I can validate the appearance and disappearance of elements

Scenario: Dismissed Initial Page Validation
  Given I am on the Add/Remove Elements page
  When I verify the current page URL contains "add_remove_elements"
  Then the page title should be "Add/Remove Elements"
    And the "Add Element" button should be interactable
    And the "Delete" button should not be present

Scenario: Validate the additional element after clicking on the Add button
  Given I am on the Add/Remove Elements page
  When I click on the "Add Element" button
  Then the "Delete" button should appear

Scenario: Validate element removal after clicking on the Delete button
  Given I have added an element on the Add/Remove Elements page
  When I click on the "Delete" button
  Then the "Delete" button should disappear

Scenario: Validate multiple interactions with elements
  Given I am on the Add/Remove Elements page
  When I click the "Add Element" button 5 times
  Then there should be 5 "Delete" buttons present
  When I click the "Delete" button 3 times
  Then there should be 2 "Delete" buttons remaining
