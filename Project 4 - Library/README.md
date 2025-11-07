# 📚 Library Management System

Welcome to the **Library Management System** module!

In this module, you'll build a comprehensive library management application by applying your understanding of:
- **Lists**
- **Dictionaries**
- **Functions**
- **Loops**
- **Conditionals**
- **User Input**
- **Data Structures**

This project will teach you how to build progressively more complex applications, starting with basic functionality and adding features step by step.

---

## 📘 What You'll Do

This module is broken into four hands-on exercises, each building upon the previous one. Each exercise has a corresponding solution file to help you check your work.

### ✅ Exercise 1: Basic Library System (`library1.py`)
You'll build a simple library program that:
- Stores book titles as simple strings in a list.
- Allows users to **add books** to the library.
- Allows users to **list all books** in the library.
- Uses a menu-driven interface for user interaction.
- **Solution File:** `library1_solution.py` (Reference solution for comparison)

### ✅ Exercise 2: Enhanced Library with Book Details (`library2.py`)
Building on Exercise 1, you'll upgrade your library to store more information about each book:
- Stores books as **dictionaries** with title, author, and publication year.
- Maintains the same add and list functionality with richer data.
- Displays detailed information for each book.
- **Solution File:** `library2_solution.py` (Reference solution for comparison)

### ✅ Exercise 3: Full CRUD Operations (`library3.py`)
Expanding on Exercise 2, you'll add complete Create, Read, Update, Delete (CRUD) functionality:
- **Remove books** from the library by title.
- **Update existing books** with new information (title, author, or year).
- Implement more sophisticated data manipulation techniques.
- **Solution File:** `library3_solution.py` (Reference solution for comparison)

### ✅ Exercise 4: Advanced Library with User Authentication (`library4.py`)
The most advanced version with user roles and permissions:
- Adds **user authentication** with different user types (students and librarians).
- Implements a **checkout/return system** for students to borrow books.
- Gives librarians special permissions for managing the library.
- Tracks which books are checked out and by whom.
- **Solution File:** `library4_solution.py` (Reference solution for comparison)

---

## ✏️ Code Comments and Explanation (Required)

You are **required** to add comments at the **bottom of your code** explaining:
- How you developed your solution step-by-step
- Which **methods** and **functions** you used and why
- Any challenges you encountered and how you solved them

> ⚠️ **Important**: Failure to include your explanation will result in a loss of points.

---

## 🧪 Testing Your Code

Unlike Projects 1-3 which use automated pytest files, this module uses **solution files** for manual comparison instead of automated test files. 

1. **Compare your output with the solution:**
   - Run your version: `python library1.py`
   - Run the solution: `python library1_solution.py`
   - Compare the behavior and output

2. **Test different scenarios:**
   - Try adding multiple books
   - Test the list functionality with empty and populated libraries
   - For later exercises, test update and remove operations
   - For Exercise 4, test different user permissions

3. **Making Your Code Work:**
   To ensure your code runs properly, wrap any code that runs the program (like calling `input()`) inside an `if __name__ == "__main__":` block at the end of your file. This is good practice and follows Python conventions.

---

## 🧠 Learning Goals

By completing this project, you will:
- Master working with **lists** and **dictionaries** for data storage
- Learn to build **menu-driven applications** with user interfaces
- Understand **CRUD operations** (Create, Read, Update, Delete)
- Practice implementing **user authentication** and **role-based permissions**
- Build progressively complex applications through **iterative development**
- Learn to organize code with **functions** for better modularity and reusability

---

Let's build a powerful library management system! 📖✨
