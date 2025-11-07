# 📋 Class Attendance Counter

Welcome to the **Class Attendance Counter** module!

In this module, you'll build a Python program to help teachers keep track of class attendance by applying your understanding of:
- **User Input**
- **Conditionals**
- **Loops**
- **Lists**
- **Functions**

This is a practical way to create real-world applications that solve everyday problems.

---

## 📘 What You'll Do

This module is broken into two hands-on exercises, each with its own test file to help you check your work.

### ✅ Exercise 1: Basic Attendance Counter (`counter1.py`)
You'll build a simple attendance tracking program that:
- Asks the user for the **class size**.
- Prompts the user to record whether each student is **present or absent**.
- Displays the **total number of present and absent students** at the end.
- **Test File:** `counter1_test.py` (Tests your counter function with various inputs)

### ✅ Exercise 2: Advanced Attendance Tracker (`counter2.py`)
Building on Exercise 1, you'll create a more sophisticated tracker that:
- Asks the user for the **names of each student** in the class.
- Prompts the user to mark each student as **present or absent** by name.
- Displays:
  - The **total number of present and absent students**.
  - A list of the **names of present and absent students**.
- **Test File:** `counter2_test.py` (Tests your advanced tracking functionality)

---

## ✏️ Code Comments and Explanation (Required)

You are **required** to add comments at the **bottom of your code** explaining:
- How you developed your solution step-by-step
- Which **methods** and **functions** you used and why

> ⚠️ **Important**: Failure to include your explanation will result in a loss of points.

---

## 🧪 Running Tests

To check your work, you will use the `pytest` library.

1.  **Install pytest:**
    ```bash
    pip install pytest
    ```

2.  **Run tests for a specific exercise:**
    ```bash
    # To run tests for counter1
    pytest counter1_test.py
    
    # To run tests for counter2
    pytest counter2_test.py
    ```

3.  **Making Tests Pass:**
    To make your code testable, you must wrap any code that *runs* the program (like calling `input()`) inside an `if __name__ == "__main__":` block at the end of your file. This allows `pytest` to `import` your functions without running the whole program.
    
    You will also need to structure your main logic into a function (e.g., `counter()`) that can be called by the tests.

---

## 🧠 Learning Goals

By completing this project, you will:
- Practice using **loops** and **conditional logic** effectively
- Learn to work with **user input** and **lists**
- Understand how to build simple, real-world applications
- Begin to think about how to **test** and **validate** your code

---

Let's build a tool that makes attendance easy and efficient! 🎓
