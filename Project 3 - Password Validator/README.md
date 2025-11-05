# 🔐 Password Strength Checker

Welcome to the **Password Strength Checker** module!

In this module, you'll expand your Python skills by working with external modules, handling user input, and learning about **automated testing** with `pytest`.

You'll apply your understanding of:
- **Expressions**
- **Conditionals**
- **Loops**
- **Functions**
- **Strings**
- **External Modules** (`getpass`)

To create programs that evaluate password strength and reinforce secure coding practices.

---

## 📘 What You'll Do

This module is broken into three hands-on exercises, each with its own test file to help you check your work.

### ✅ Exercise 1: Basic Password Strength Evaluator (`checker1.py`)
You'll build a simple program that:
- Takes user input for a password.
- Evaluates the password based on basic strength criteria (length, letters, numbers, punctuation).
- Gives the user feedback about how strong or weak their password is.
- **Test File:** `checker1_test.py` (Tests your helper functions and main strength logic)

### ✅ Exercise 2: Username & Password Entry with Visibility Toggle (`checker2.py`)
Building on Exercise 1, you'll:
- Ask the user for both a **username** and **password**.
- Give the user the option to **show or hide** their password as they type using the `getpass` module.
- **Test File:** `checker2_test.py` (Tests your helper functions and new username validation)

### ✅ Exercise 3: Breaking the Code (`checker3.py`)
This exercise is different. There is no new code to write in `checker3.py`.
- Your goal is to **find flaws and edge cases** in your `checker2.py` program.
- The instructions for this thought exercise are in `checker3.py`.
- **Test File:** `checker3_test.py`
    - This test file is designed to *run against* your `checker2.py` code.
    - It tests for the **ambiguous cases and edge cases** (like "numbers and punctuation only") that the original instructions didn't cover.
    - Your goal is to make your `checker2.py` code robust enough to pass all the tests in `checker3_test.py`.

---

## 🧪 Running Tests

To check your work, you will use the `pytest` library.

1.  **Install pytest:**
    ```bash
    pip install pytest
    ```

2.  **Run tests for a specific exercise:**
    ```bash
    # To run tests for checker1
    pytest checker1_test.py
    
    # To run tests for checker2
    pytest checker2_test.py
    
    # To run tests for checker3 (against checker2's code)
    pytest checker3_test.py
    ```

3.  **Making Tests Pass:**
    To make your code testable, you must wrap any code that *runs* the program (like calling `input()`) inside an `if __name__ == "__main__":` block at the end of your file. This allows `pytest` to `import` your functions without running the whole program.

    You will also need to put your main strength logic into a function (e.g., `check_strength(password)`) that returns a string, so the tests can call it.