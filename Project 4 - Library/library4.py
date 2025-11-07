# Library Management System - Level 4
# This version adds user authentication and a checkout/return system
# Goal: Create different user roles (students and librarians) with different permissions

# TODO: Create a global list of users
# This should contain a list of valid usernames
# Example: users = ["Alice", "Bob", "Charlie", "Librarian"]
# Note: The last user "Librarian" will have special permissions


# TODO: Create a global list to store all books (same as before)


# TODO: Define an 'add_book' function (same as Level 2 and 3)
# Parameters: title, author, year
# Creates a dictionary and appends to all_books


# TODO: Define a 'remove_book' function (same as Level 3)
# Parameter: title
# Removes the book with matching title from all_books


# TODO: Define an 'update_book' function (same as Level 3)
# Parameters: old_title, new_title=None, new_author=None, new_year=None
# Updates the matching book's fields


# TODO: Define a 'checkout_book' function that takes two parameters: title, student_name
# This function should:
# 1. Loop through all books in all_books
# 2. Find the book with matching title (case-insensitive)
# 3. Check if the book already has a 'checked_out_by' key:
#    - If NOT (book is available): 
#      * Add a 'checked_out_by' key to the book dictionary with student_name as value
#      * Return a success message like "Book 'title' has been checked out by student_name"
#    - If YES (book is already checked out):
#      * Return a message like "Book 'title' is already checked out by {name}"
# 4. If the book is not found in the library, return "Book 'title' not found"
#
# Hint: To check if a key exists in a dictionary: if 'key' in my_dict:
# Hint: To check if a key does NOT exist: if 'key' not in my_dict:
#
# Example of adding a key to a dictionary:
# book = {'title': 'Python 101', 'author': 'John'}
# book['status'] = 'available'  # Now book has a 'status' key


# TODO: Define a 'return_book' function that takes one parameter: title
# This function should:
# 1. Loop through all books in all_books
# 2. Find the book with matching title (case-insensitive)
# 3. Check if the book has a 'checked_out_by' key:
#    - If YES (book is checked out):
#      * Delete the 'checked_out_by' key from the book dictionary
#      * Return a success message like "Book 'title' has been returned"
#    - If NO (book was not checked out):
#      * Return "Book 'title' was not checked out"
# 4. If the book is not found, return "Book 'title' not found"
#
# Hint: To delete a key from a dictionary: del my_dict['key']


# TODO: Define a 'book_list' function that returns all_books


# TODO: Define an 'authenticate_user' function with no parameters
# This function should:
# 1. Prompt the user to enter their name
# 2. Clean the input with .strip()
# 3. Check if the name is in the users list and determine their role:
#    - If the name is in the users list AND is NOT "Librarian" (i.e., is a student):
#      * Print a welcome message
#      * Return the name
#    - If the name is exactly "Librarian":
#      * Print a special welcome message for librarian
#      * Return "Librarian"
#    - If the name is not in the users list at all:
#      * Print "Authentication failed"
#      * Return None
#
# Hint: users[:-1] gives you all users except the last one (all students)
# Hint: Check if name == "Librarian" to identify the librarian
# Hint: Check if name in users[:-1] to identify students


# TODO: Define a main() function
# This function should:
# 1. Call authenticate_user() and store the result
# 2. If authentication failed (returned None), exit the function with 'return'
# 3. If user is "Librarian":
#    - Print a message about librarian capabilities
#    - Create a menu loop with options: 'add', 'list', 'exit'
#    - Handle each option appropriately (similar to Level 2)
#    - When listing books, print full details in a nice format
#
# 4. If user is a student (in users list but not "Librarian"):
#    - Print a message about student capabilities  
#    - Create a menu loop with options: 'checkout', 'return', 'list', 'exit'
#    - Handle 'checkout': Ask for title, call checkout_book(title, user), print message
#    - Handle 'return': Ask for title, call return_book(title), print message
#    - Handle 'list': Display all books with their details
#    - Handle 'exit': Break the loop
#
# Note: You may want to consider having separate while loops for librarian and student
# to keep the code organized


# TODO: Add the if __name__ == "__main__": block to run main()
