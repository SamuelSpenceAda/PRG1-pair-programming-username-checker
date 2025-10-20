# Username Validator Activity

## **Line-Specific Questions:**

**L4 (INPUT_FILE = "./test_usernames.txt"):**
- What type of data is stored in INPUT_FILE?            String 
- Why is this defined as a constant at the top?         Because the file path needs to stay the same

**L12 (clean_username = username.strip()):**
- What does `.strip()` do to a string?                  Removes white space from either side of the string
- What happens if we remove this line?                  
- Try changing `username.strip()` to just `username` - what difference does it make?

**L15 (return len(clean_username) > 0):**
- What does this line check for?
- Why do we check the length of `clean_username` instead of `username`?

**L25 (stripped_version = username.strip()):**
- Why do we call `.strip()` again here?
- What will you see in the log file that shows the difference between original and stripped?

**L30 (username_data.split("\n")):**
- What does `.split("\n")` do?
- What type of data does this create?

## **PREDICT Questions:**

**Before running the code, predict what will happen with each username in the file:**

1. **`zara`**
   - Will this be True or False?
   - What gets written to the log file?

2. **` bob `** (spaces at start and end)
   - Will this be True or False?
   - How will the log entry show the difference?

3. **`  charlie  `** (more spaces)
   - Will this be True or False?
   - What does the username become after stripping?

4. **` admin `** (admin with spaces)
   - Will this be True or False?
   - Does the program care what the username says?

5. **`   `** (line with only spaces)
   - Will this be True or False?
   - What happens when we strip a string that's only whitespace?

6. **Empty line in the file**
   - Will this be True or False?
   - What does an empty string become after stripping?

## **File Behaviour Questions:**

1. **What happens if we run the program multiple times?**
   - Does the log file get overwritten or appended to?

2. **What would happen if `test_usernames.txt` didn't exist?**
   - Try renaming the file and run the program

3. **Count prediction:**
   - Looking at the usernames in the file, how many do you predict will be Valid?
   - How many will be Invalid?

## **MODIFY Tasks - Remove .strip():**

1. **Change line 12 from:**
   ```python
   clean_username = username.strip()
   ```
   **To:**
   ```python
   clean_username = username
   ```

2. **Run the program again and compare:**
   - Which usernames that were Valid become Invalid?
   - Look at the log file - what's different about the arrows (-->)?

## **EXTENSION Tasks:**

### **Extension 1: Add Length Checking**
Add this validation rule to `is_valid_username()`:
- Username must be at least 3 characters long (after stripping)

**Questions:**
- Which usernames from the file will now become Invalid?
- Why is it important to check length AFTER stripping?

### **Extension 2: Add Banned Words**
Add this validation rule to `is_valid_username()`:
- Username cannot be "admin", "test", or "user" (case-insensitive, after stripping)

**Questions:**
- Which usernames from the file will now become Invalid?
- What happens with ` admin ` (admin with spaces)?
- Why do we need to strip before checking banned words?

### **Extension 3: Combine Both Rules**
Make a username valid only if:
- It's at least 3 characters long (after stripping), AND
- It's not a banned word (after stripping)

**Challenge:** Can you predict how many usernames will be Valid with both rules applied?

## **Key Learning Points:**
- `.strip()` removes whitespace (spaces, tabs, newlines) from both ends of a string
- Always strip data read from files - users often accidentally add whitespace
- Strip BEFORE doing validation checks (length, content, etc.)
- The original string is unchanged - `.strip()` returns a new string
- File input often needs cleaning with `.strip()` to work properly