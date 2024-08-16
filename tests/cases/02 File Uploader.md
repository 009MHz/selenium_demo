**Test Case ID:** TCP-FUP-01  
**Test Scenario:** File Uploader Page contains the correct components

**Pre-conditions:**

**Test Steps:**
1. Navigate to the file uploader page
2. Ensure upload file page contains proper information
3. Ensure the file uploader components are exist and interactable

**Expected Results:**
- The page title displayed "File Uploader"
- The page description is available and contains the proper information
- The File Selector button is enabled and displayed as "Choose File"
- The default filename state displayed as empty and written as "No file chosen"
- The submit file button is enabled and displayed as "Upload"
- The drag box section is displayed and contains the empty value 

---

**Test Case ID:** TCP-FUP-02  
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

---

**Test Case ID:** TCN-FUP-01  
**Test Scenario:** Attempt to Upload Without Selecting a File

**Pre-conditions:**
1. User is on the file uploader page.
2. The file uploader allows file selection.

**Test Steps:**
1. Do not select any file.
2. Click on the "Upload" button.

**Expected Results:**
- An error message is displayed, or no file name is shown.

---

**Test Case ID:** TCP-FUP-03  
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
