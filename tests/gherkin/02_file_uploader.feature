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