### **TCP-FUP-01: File Uploader Page contains the correct components**

**Preconditions:** 

**Test Steps:**
1. Navigate to the File Upload Page.
2. Validate the URL contains "upload".
3. Validate the page title is "File Uploader".
4. Validate the page info contains "Choose a file".
5. Validate the page info contains "Or, drag and drop a file".
6. Validate the "Choose File" button is accessible.
7. Validate the "Upload" button is accessible.
8. Validate the dragging box is accessible and the file name preview and marker are not visible.

**Expected Result:**
- The URL contains "upload".
- The page title is "File Uploader".
- The page info contains the correct text.
- The "Choose File" button is accessible.
- The "Upload" button is accessible.
- The dragging box is accessible, and the file name preview and marker are not visible.

---

### **TCP-FUP-02: Successful File Upload Validation**

**Preconditions:** The user is on the File Upload Page.

**Test Steps:**
1. Select the file e.g: `testFile.docx`.
2. Click the "Upload" button.
3. Verify the URL contains "upload".
4. Verify the page title is "File Uploaded!".
5. Verify the uploaded file name is "testFile.docx".

**Expected Result:**
- The URL contains "upload".
- The page title is "File Uploaded!".
- The uploaded file name is "testFile.docx".

---

### **TCP-FUP-03: File Upload Documents Test**

**Preconditions:** The user is on the File Upload Page.

**Test Steps:**
1. Select the file "testFile.docx" or "testFile.pdf".
2. Click the "Upload" button.
3. Verify the URL contains "upload".
4. Verify the page title is "File Uploaded!".
5. Verify the uploaded file name matches the selected file.

**Expected Result:**
- The URL contains "upload".
- The page title is "File Uploaded!".
- The uploaded file name matches the selected file.

---

### **TCP-FUP-04: File Upload Images Test**

**Preconditions:** The user is on the File Upload Page.

**Test Steps:**
1. Select the file "testFile.png" or "testFile.jpeg".
2. Click the "Upload" button.
3. Verify the URL contains "upload".
4. Verify the page title is "File Uploaded!".
5. Verify the uploaded file name matches the selected file.

**Expected Result:**
- The URL contains "upload".
- The page title is "File Uploaded!".
- The uploaded file name matches the selected file.

---

### **TCP-FUP-05: File Upload Data Test**

**Preconditions:** The user is on the File Upload Page.

**Test Steps:**
1. Select the file "testFile.csv" or "testFile.xlsx".
2. Click the "Upload" button.
3. Verify the URL contains "upload".
4. Verify the page title is "File Uploaded!".
5. Verify the uploaded file name matches the selected file.

**Expected Result:**
- The URL contains "upload".
- The page title is "File Uploaded!".
- The uploaded file name matches the selected file.

---

### **TCP-FUP-06: File Upload Video Test**

**Preconditions:** The user is on the File Upload Page.

**Test Steps:**
1. Select the file "testFile.mp4" or "testFile.webm".
2. Click the "Upload" button.
3. Verify the URL contains "upload".
4. Verify the page title is "File Uploaded!".
5. Verify the uploaded file name matches the selected file.

**Expected Result:**
- The URL contains "upload".
- The page title is "File Uploaded!".
- The uploaded file name matches the selected file.

---

### **TCN-FUP-01: No File Upload Error Validation**

**Preconditions:** The user is on the File Upload Page.

**Test Steps:**
1. Click the "Upload" button without selecting any file.
2. Verify the URL contains "upload".
3. Verify the page title is "Internal Server Error".
4. Verify the file preview is not visible.

**Expected Result:**
- The URL contains "upload".
- The page title is "Internal Server Error".
- The file preview is not visible.
