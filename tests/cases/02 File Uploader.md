**Test Case ID:** TCP_FUP_01  
**Test Scenario:** Successful File Upload

**Pre-conditions:**
1. User is on the file uploader page.
2. The file uploader allows file selection.

**Test Steps:**
1. Click on the "Choose File" button.
2. Select a valid file from the local machine.
3. Click on the "Upload" button.

**Expected Results:**
- The name of the uploaded file is displayed on the page.

**Actual Results:**


---

**Test Case ID:** TCN_FUP_02  
**Test Scenario:** Attempt to Upload Without Selecting a File

**Pre-conditions:**
1. User is on the file uploader page.
2. The file uploader allows file selection.

**Test Steps:**
1. Do not select any file.
2. Click on the "Upload" button.

**Expected Results:**
- An error message is displayed, or no file name is shown.

**Actual Results:**


---

**Test Case ID:** TCP_FUP_03  
**Test Scenario:** Upload of a File with a Specific Format

**Pre-conditions:**
1. User is on the file uploader page.
2. The file uploader allows file selection.

**Test Steps:**
1. Click on the "Choose File" button.
2. Select a file with a specific format (e.g., .txt, .jpg).
3. Click on the "Upload" button.

**Expected Results:**
- The name of the uploaded file is displayed on the page.
- The file should be accepted if it matches the allowed formats.

**Actual Results:**
