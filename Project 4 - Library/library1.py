# Library Management System - Level 1
# This is a basic library program that stores book titles as simple strings
# Goal: Create a simple menu-driven program to add books and list all books

# TODO: Create a global list to store all books
# Hint: Initialize an empty list called 'all_books' that will hold book titles as strings
# Example: my_list = []


# TODO: Define a function called 'add_book' that takes one parameter: title
# This function should:
# 1. Take the title parameter and store it in a variable called 'book'
# 2. Append the book to the all_books list
# Hint: Use the .append() method to add items to a list
# Example of append: my_list.append(item)


# TODO: Define a function called 'book_list' that returns the all_books list
# This function should:
# 1. Return the all_books list so other parts of the program can access it
# Hint: Use the 'return' keyword


# TODO: Define a main() function that contains the program's main loop
# This function should:
# 1. Create an infinite loop using 'while True:'
# 2. Print a message asking the user what they want to do
# 3. Get user input and store it in a variable (remember to use .strip().lower() to clean the input)
# 4. Use if/elif/else statements to handle different user choices:
#    - 'add': Ask for book title, call add_book(), print confirmation
#    - 'list': Call book_list(), check if empty, display all books with numbers
#    - 'exit': Print goodbye message and break the loop
#    - Invalid input: Print an error message
# 
# Hint for displaying numbered lists:
# Use enumerate(list, start=1) in a for loop to get both index and item
# Example: for index, item in enumerate(my_list, start=1):


# TODO: Add the standard Python idiom to run main() when the script is executed
# Hint: if __name__ == "__main__":
#           main()
