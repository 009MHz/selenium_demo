### Test Case 1: Login Functionality

---

**Test Case ID:** TCP_LGI_01  
**Test Scenario:** Username input is not masked by dot

**Pre-conditions:**
1. User is on the login page of the website.
2. The login page has visible fields for "Username" and "Password."

**Test Steps:**
1. Enter any text in the "Username" field.

**Expected Results:**
- The characters in the "Username" field should not be masked (e.g., as dots or asterisks).
- The Username input character should be displayed as it is

---

**Test Case ID:** TCP_LGI_02  
**Test Scenario:** Password Field Masking

**Pre-conditions:**
1. User is on the login page of the website.
2. The login page has visible fields for "Username" and "Password."

**Test Steps:**
1. Enter any text in the "Password" field.

**Expected Results:**
- The characters in the "Password" field should be masked (e.g., as dots or asterisks).
- The password should not be visible in plain text.

---

**Test Case ID:** TCP_LGI_03  
**Test Scenario:** Successful Login with Correct Credentials

**Pre-conditions:**
1. User is on the login page of the website.
2. The login page has visible fields for "Username" and "Password."
3. The "Login" button is available.

**Test Steps:**
1. Enter the valid username "tomsmith" in the "Username" field.
2. Enter the valid password "SuperSecretPassword!" in the "Password" field.
3. Click on the "Login" button.

**Expected Results:**
- The user is redirected to the secure area.
- A success message "You logged into a secure area!" is displayed.

---

**Test Case ID:** TCN_LGI_01  
**Test Scenario:** Unsuccessful Login with Incorrect Credentials

**Pre-conditions:**
1. User is on the login page of the website.
2. The login page has visible fields for "Username" and "Password."
3. The "Login" button is available.

**Test Steps:**
1. Enter an invalid username "invalid_user" in the "Username" field.
2. Enter an invalid password "invalid_password" in the "Password" field.
3. Click on the "Login" button.

**Expected Results:**
- An error message "Your username is invalid!" or "Your password is invalid!" is displayed.
- The user remains on the login page.

---

**Test Case ID:** TCN_LGI_02  
**Test Scenario:** Login with Empty Username

**Pre-conditions:**
1. User is on the login page of the website.
2. The login page has visible fields for "Username" and "Password."

**Test Steps:**
1. Leave the "Username" field empty.
2. Enter a valid password "SuperSecretPassword!" in the "Password" field.
3. Click on the "Login" button.

**Expected Results:**
- An error message "Your username is invalid!" is displayed.
- The user remains on the login page.

---

**Test Case ID:** TCN_LGI_03  
**Test Scenario:** Login with Empty Password

**Pre-conditions:**
1. User is on the login page of the website.
2. The login page has visible fields for "Username" and "Password."

**Test Steps:**
1. Enter a valid username "tomsmith" in the "Username" field.
2. Leave the "Password" field empty.
3. Click on the "Login" button.

**Expected Results:**
- An error message "Your password is invalid!" is displayed.
- The user remains on the login page.
