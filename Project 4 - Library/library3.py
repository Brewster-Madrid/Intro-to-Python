# Library Management System - Level 3
# This version adds the ability to remove and update books
# Goal: Add full CRUD operations (Create, Read, Update, Delete) to the library

# TODO: Create a global list to store all books
# Hint: Initialize an empty list called 'all_books'


# TODO: Define an 'add_book' function (same as Level 2)
# Parameters: title, author, year
# Should create a dictionary with these three fields and append to all_books


# TODO: Define a 'remove_book' function that takes one parameter: title
# This function should:
# 1. Use the 'global' keyword to modify the global all_books variable
# 2. Create a new list that contains all books EXCEPT the one with matching title
# 3. Assign this new list back to all_books
#
# Hint: Use a list comprehension with a condition
# Example of list comprehension: new_list = [item for item in old_list if condition]
# To compare strings case-insensitively: string1.lower() == string2.lower()
#
# Example of filtering a list:
# numbers = [1, 2, 3, 4, 5]
# # Keep only numbers greater than 3
# numbers = [num for num in numbers if num > 3]
# Result: [4, 5]


# TODO: Define an 'update_book' function with four parameters:
# Parameters: old_title, new_title=None, new_author=None, new_year=None
# Note: The last three parameters have default values of None (making them optional)
#
# This function should:
# 1. Loop through each book in all_books
# 2. Find the book where the title matches old_title (case-insensitive)
# 3. When found, update only the fields that were provided (not None):
#    - If new_title is provided: update book['title']
#    - If new_author is provided: update book['author']
#    - If new_year is provided: update book['year']
# 4. Break out of the loop after finding and updating the book
#
# Hint: Use if statements to check if optional parameters were provided
# Example: if new_title:  # This checks if new_title is not None


# TODO: Define a 'book_list' function that returns all_books


# TODO: Define a main() function
# The main function should have a menu-driven interface similar to Level 2
# At minimum, implement the 'add', 'list', and 'exit' options
#
# OPTIONAL CHALLENGE: Extend the menu to include:
# - 'remove': Ask for title, call remove_book(), print confirmation
# - 'update': Ask for old title and new values, call update_book(), print confirmation
#
# Note: The remove_book() and update_book() functions defined above are required
# for this level, but calling them from the menu is optional extra practice!


# TODO: Add the if __name__ == "__main__": block to run main()
