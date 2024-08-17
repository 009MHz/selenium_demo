### **TCP-MEP-01: Dismissed Initial Page Validation**

**Preconditions:** The user is on the Add/Remove Elements page.

**Test Steps:**
1. Navigate to the Add/Remove Elements page.
2. Verify that the current page URL contains "add_remove_elements".
3. Verify that the page title is "Add/Remove Elements".
4. Verify that the "Add Element" button is interactable.
5. Verify that the "Delete" button is not present initially.

**Expected Result:**
- The page URL contains "add_remove_elements".
- The title matches.
- The "Add Element" button is interactable.
- No "Delete" buttons are present initially.

---

### **TCP-MEP-02: Validate the Additional Element After Clicking on the Add Button**

**Preconditions:** The user is on the Add/Remove Elements page.

**Test Steps:**
1. Click on the "Add Element" button.
2. Verify that the "Delete" button appears.

**Expected Result:**
- The "Delete" button appears after clicking "Add Element".

---

### **TCP-MEP-03: Validate Element Removal After Clicking on the Delete Button**

**Preconditions:** The user has added an element on the Add/Remove Elements page.

**Test Steps:**
1. Click on the "Delete" button.
2. Verify that the "Delete" button disappears.

**Expected Result:**
- The "Delete" button disappears after clicking on it.

---

### **TCP-MEP-04: Validate Multiple Interactions with Elements**

**Preconditions:** The user is on the Add/Remove Elements page.

**Test Steps:**
1. Click the "Add Element" button 5 times.
2. Verify that 5 "Delete" buttons are present.
3. Click the "Delete" button 3 times.
4. Verify that 2 "Delete" buttons remain.

**Expected Result:**
- After 5 additions, 5 "Delete" buttons are present.
- After 3 deletions, 2 "Delete" buttons remain.

---
