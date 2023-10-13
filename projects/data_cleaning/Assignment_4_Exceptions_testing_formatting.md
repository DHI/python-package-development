# Module 4 Assignment: Exceptions, Testing, and Formatting

## Objective:
Enhance the robustness, reliability, and readability of your code by integrating error handling, writing comprehensive tests, and applying consistent formatting standards.

## Tasks:

### 1. **Error Handling:**
   Add appropriate error handling mechanisms to gracefully manage potential issues during the data cleaning process.
   
   **Subtasks:**
   - Identify areas in your code where errors are likely to occur (e.g., data type inconsistencies, out-of-range issues).
   - Implement `try-except` blocks to catch and handle these errors effectively.
   - Provide informative error messages to make debugging easier.

### 2. **Testing:**
   Develop unit tests to validate the functionality and reliability of your data cleaning functions.
   
   **Subtasks:**
   - Identify the core functionalities that need testing (e.g., range check, spike detection, flat period identification).
   - Write pytest functions to test these core functionalities, ensuring they work as expected with various data inputs.
   - Consider edge cases and potential anomalies in the data while writing your tests.

### 3. **Formatting:**
   Apply consistent formatting standards to enhance the readability and maintainability of your code.
   
   **Subtasks:**
   - Review your code to ensure it adheres to PEP-8 standards.
   - Utilize the auto-formatting tool Black to automatically format your code.   

### 4. **GitHub:**
   - Commit the updated, tested, and well-formatted code to your GitHub repository.
   - Create a pull request, providing a summary of the enhancements made.

## Example:

```python
# Implementing error handling
try:
    range_check(data, 5, 95)
except ValueError as e:
    print(f"Value Error: {e}")

# Sample pytest function for testing range check
def test_range_check():
    assert range_check(test_data, 5, 95) == expected_output

# Apply auto-formatting tools for consistent code structure
# Ensure the use of tools like Black
```

## Submission:
Open a pull request to submit your enhanced code, and actively engage in the peer review process, evaluating and learning from the code enhancements made by others.