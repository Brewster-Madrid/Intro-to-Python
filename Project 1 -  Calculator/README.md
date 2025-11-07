# 🧮 Calculator Project

Welcome to the **first set of activities** in this Python course!

In this project, you'll build a calculator by applying your knowledge of:
- **Statements**
- **Expressions**
- **Operators**
- **Conditionals**

These exercises are designed to give you a solid foundation in writing basic logic-driven programs.

---

## 📘 What You'll Do

This module is broken into three hands-on exercises, each with its own test file to help you check your work.

### ✅ Exercise 1: Basic Calculator (`calc_v1.py`)
You must complete `calc_v1.py` **before moving on** to the other versions. You'll build a simple calculator that:
- Implements basic arithmetic operations (add, subtract, multiply, divide, remainder, exponent).
- Takes user input for numbers and operations.
- Performs the selected calculation and displays the result.
- **Test File:** `calcv1_test.py` (Tests your arithmetic functions and main program logic)

### ✅ Exercise 2: Enhanced Calculator (`calc_v2.py`)
Building on Exercise 1, you'll enhance your calculator with additional features and improved error handling.
- Follow the in-code `#comments` with instructions to complete the activity.
- **Test File:** `calcv2_test.py` (Tests your enhanced functionality)

### ✅ Exercise 3: Advanced Calculator (`calc_v3.py`)
The most advanced version with comprehensive functionality.
- Follow the in-code `#comments` with instructions to complete the activity.
- **Test File:** `calcv3_test.py` (Tests your advanced features)

---

## ✍️ Code Reflection (Required)

At the **bottom of your code**, you **must include a comment section** that explains:
- How you developed your solution (your thought process)
- Which Python methods, functions, or techniques you used

> ⚠️ **Note:** This reflection is part of your assessment. Failing to include it will result in lost points.

---

## 🧪 Running Tests

To check your work, you will use the `pytest` library.

1.  **Install pytest:**
    ```bash
    pip install pytest
    ```

2.  **Run tests for a specific exercise:**
    ```bash
    # To run tests for calc_v1
    pytest calcv1_test.py
    
    # To run tests for calc_v2
    pytest calcv2_test.py
    
    # To run tests for calc_v3
    pytest calcv3_test.py
    ```

3.  **Making Tests Pass:**
    To make your code testable, you must wrap any code that *runs* the program (like calling `input()`) inside an `if __name__ == "__main__":` block at the end of your file. This allows `pytest` to `import` your functions without running the whole program.
