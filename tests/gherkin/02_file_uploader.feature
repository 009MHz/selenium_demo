Feature: File Upload Functionality
  As a user
  I want to upload files using the File Uploader page
  So that I can validate the upload process for various file types

  Scenario: File Uploader Page contains the correct components
    Given I am on the File Upload Page
    When I validate the URL contains "upload"
    Then the page title should be "File Uploader"
    And the page info should contain "Choose a file"
    And the page info should contain "Or, drag and drop a file"
    And the "Choose File" button should be accessible
    And the "Upload" button should be accessible
    And the dragging box should be accessible
    And the file name preview and marker should not be visible

  Scenario Outline: Successful File Upload Validation
    Given I am on the File Upload Page
    When I select the file "<file_name>"
    And I click the "Upload" button
    Then the URL should contain "upload"
    And the page title should be "File Uploaded!"
    And the uploaded file name should be "<file_name>"

    Examples:
      | file_name        |
      | testFile.docx    |
      | testFile.pdf     |
      | testFile.png     |
      | testFile.jpeg    |
      | testFile.csv     |
      | testFile.xlsx    |
      | testFile.mp4     |
      | testFile.webm    |

  Scenario: No File Upload Error Validation
    Given I am on the File Upload Page
    When I click the "Upload" button without selecting any file
    Then the URL should contain "upload"
    And the page title should be "Internal Server Error"
    And the file preview should not be visible
