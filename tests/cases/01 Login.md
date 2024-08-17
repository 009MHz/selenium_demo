### **TCP-LGI-01: Password field is masked by dot**

**Preconditions:** The user is on the Login Page.

**Test Steps:**
1. Enter "T|-|!s I5 Sp#ci@l TeXt P4sSw012D" into the password field.
2. Validate that the password field is masked by dots.

**Expected Result:**
- The password field should be masked by dots.

---

### **TCP-LGI-02: Username input is not masked by dot**

**Preconditions:** The user is on the Login Page.

**Test Steps:**
1. Enter "T|-|!s I5 Sp#ci@l TeXt UserN@m3" into the username field.
2. Validate that the username field is not masked.

**Expected Result:**
- The username field should not be masked.

---

### **TCP-LGI-03: Successful Login with Correct Credentials**

**Preconditions:** The user is on the Login Page.

**Test Steps:**
1. Enter "tomsmith" into the username field.
2. Enter "SuperSecretPassword!" into the password field.
3. Click the "Login" button.
4. Validate that the user is redirected to a URL containing "/secure".
5. Validate that a success toast message appears containing "You logged into".
6. Validate that the page title is "Secure Area".
7. Validate that the success page sub-header contains "When you are done".
8. Validate that the "Logout" button is visible and enabled.

**Expected Result:**
- The user is redirected to a URL containing "/secure".
- A success toast message appears containing "You logged into".
- The page title is "Secure Area".
- The success page sub-header contains "When you are done".
- The "Logout" button is visible and enabled.

---

### **TCP-NGI-01: Unsuccessful Login with Invalid Username**

**Preconditions:** The user is on the Login Page.

**Test Steps:**
1. Enter "invalid_username" into the username field.
2. Enter "SuperSecretPassword!" into the password field.
3. Click the "Login" button.
4. Validate that the user remains on the login page.
5. Validate that a failure toast message appears containing "username is invalid!".

**Expected Result:**
- The user remains on the login page.
- A failure toast message appears containing "username is invalid!".

---

### **TCP-NGI-02: Unsuccessful Login with Invalid Password**

**Preconditions:** The user is on the Login Page.

**Test Steps:**
1. Enter "tomsmith" into the username field.
2. Enter "invalid_password" into the password field.
3. Click the "Login" button.
4. Validate that the user remains on the login page.
5. Validate that a failure toast message appears containing "password is invalid!".

**Expected Result:**
- The user remains on the login page.
- A failure toast message appears containing "password is invalid!".

---

### **TCP-NGI-03: Unsuccessful Login with Invalid Credentials**

**Preconditions:** The user is on the Login Page.

**Test Steps:**
1. Enter "invalid_username" into the username field.
2. Enter "invalid_password" into the password field.
3. Click the "Login" button.
4. Validate that the user remains on the login page.
5. Validate that a failure toast message appears containing "username is invalid!".

**Expected Result:**
- The user remains on the login page.
- A failure toast message appears containing "username is invalid!".

---

### **TCP-NGI-04: Unsuccessful Login with Empty Fields**

**Preconditions:** The user is on the Login Page.

**Test Steps:**
1. Click the "Login" button without entering credentials.
2. Validate that the user remains on the login page.
3. Validate that a failure toast message appears containing "username is invalid!".

**Expected Result:**
- The user remains on the login page.
- A failure toast message appears containing "username is invalid!".
