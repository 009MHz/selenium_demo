# **Login Functionality**

#### **Test Case 1: Successful Login with Correct Credentials**
- **Test Case ID:** TC_Login_01
- **Description:** Verify that a user can successfully log in with correct credentials.
- **Preconditions:** User is on the login page.
- **Test Steps:**
  1. Verify that the "Username" field is visible.
  2. Verify that the "Password" field is visible.
  3. Enter a valid username in the "Username" field.
  4. Enter a valid password in the "Password" field.
  5. Click on the "Login" button.
- **Expected Result:** User is redirected to the secure area, and a message "You logged into a secure area!" is displayed.

#### **Test Case 2: Unsuccessful Login with Incorrect Credentials**
- **Test Case ID:** TC_Login_02
- **Description:** Verify that an error message is displayed when a user attempts to log in with incorrect credentials.
- **Preconditions:** User is on the login page.
- **Test Steps:**
  1. Verify that the "Username" field is visible.
  2. Verify that the "Password" field is visible.
  3. Enter an invalid username in the "Username" field.
  4. Enter an invalid password in the "Password" field.
  5. Click on the "Login" button.
- **Expected Result:** An error message "Your username is invalid!" or "Your password is invalid!" is displayed.

#### **Test Case 3: Password Field Masking**
- **Test Case ID:** TC_Login_03
- **Description:** Verify that the password field is masked when typing.
- **Preconditions:** User is on the login page.
- **Test Steps:**
  1. Verify that the "Password" field is visible.
  2. Enter text in the "Password" field.
- **Expected Result:** The characters in the "Password" field should be masked and not visible in plain text.

#### **Test Case 4: Login with Empty Username**
- **Test Case ID:** TC_Login_04
- **Description:** Verify that an error message is displayed when the username field is left empty.
- **Preconditions:** User is on the login page.
- **Test Steps:**
  1. Leave the "Username" field empty.
  2. Enter a valid password in the "Password" field.
  3. Click on the "Login" button.
- **Expected Result:** An error message "Your username is invalid!" is displayed.

#### **Test Case 5: Login with Empty Password**
- **Test Case ID:** TC_Login_05
- **Description:** Verify that an error message is displayed when the password field is left empty.
- **Preconditions:** User is on the login page.
- **Test Steps:**
  1. Enter a valid username in the "Username" field.
  2. Leave the "Password" field empty.
  3. Click on the "Login" button.
- **Expected Result:** An error message "Your password is invalid!" is displayed.

## **File Uploader**

#### **Test Case 1: Successful File Upload**
- **Test Case ID:** TC_FileUploader_01
- **Description:** Verify that a file can be successfully uploaded.
- **Preconditions:** User is on the file uploader page.
- **Test Steps:**
  1. Click on the "Choose File" button.
  2. Select a valid file from the file picker.
  3. Click on the "Upload" button.
- **Expected Result:** The name of the uploaded file is displayed on the page.

#### **Test Case 2: Attempt to Upload Without Selecting a File**
- **Test Case ID:** TC_FileUploader_02
- **Description:** Verify the behavior when attempting to upload a file without selecting one.
- **Preconditions:** User is on the file uploader page.
- **Test Steps:**
  1. Ensure no file is selected.
  2. Click on the "Upload" button.
- **Expected Result:** An error message is displayed, or no file name is shown.

#### **Test Case 3: Upload of a File with a Specific Format**
- **Test Case ID:** TC_FileUploader_03
- **Description:** Verify that a file with a specific format can be uploaded.
- **Preconditions:** User is on the file uploader page.
- **Test Steps:**
  1. Click on the "Choose File" button.
  2. Select a file with a specific format (e.g., .txt, .jpg).
  3. Click on the "Upload" button.
- **Expected Result:** The name of the uploaded file is displayed on the page, and the file is accepted if it matches the allowed formats.

### **Missing Element Page**

#### **Test Case 1: Handle Missing Element Gracefully**
- **Test Case ID:** TC_MissingElement_01
- **Description:** Verify that the page loads gracefully even if a specific element is missing.
- **Preconditions:** User is on the missing element page.
- **Test Steps:**
  1. Navigate to the missing element page.
  2. Observe the page's behavior when a specific element is absent.
- **Expected Result:** The page loads without errors, and a placeholder or appropriate message is displayed.

#### **Test Case 2: Interaction with a Dynamically Loaded Element**
- **Test Case ID:** TC_MissingElement_02
- **Description:** Verify that the page functions correctly when interacting with a dynamically loaded element.
- **Preconditions:** User is on the missing element page.
- **Test Steps:**
  1. Navigate to the missing element page.
  2. Wait for the element to load dynamically.
  3. Interact with the element once it appears.
- **Expected Result:** The element loads correctly, and the page functions as expected without errors.