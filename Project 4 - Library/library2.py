# Library Management System - Level 2
# This version stores books as dictionaries with multiple attributes
# Goal: Upgrade the library to store title, author, and publication year for each book

# TODO: Create a global list to store all books
# Hint: Initialize an empty list called 'all_books'


# TODO: Define a function called 'add_book' that takes THREE parameters: title, author, year
# This function should:
# 1. Create a dictionary called 'book' with three key-value pairs:
#    - 'title': the title parameter
#    - 'author': the author parameter  
#    - 'year': the year parameter
# 2. Append this book dictionary to the all_books list
#
# Example of creating a dictionary:
# person = {
#     'name': 'John',
#     'age': 25,
#     'city': 'New York'
# }


# TODO: Define a function called 'book_list' that returns the all_books list
# This function should return the all_books list


# TODO: Define a main() function with the program's main loop
# This function should:
# 1. Create an infinite loop using 'while True:'
# 2. Display a menu of options to the user
# 3. Get user input and clean it with .strip().lower()
# 4. Handle three choices using if/elif/else:
#
#    Choice 'add':
#    - Prompt for book title and store it
#    - Prompt for book author and store it  
#    - Prompt for publication year and store it
#    - Call add_book() with all three values
#    - Print a confirmation message
#
#    Choice 'list':
#    - Get the list of books by calling book_list()
#    - Check if the list is empty (use 'if not books:')
#    - If empty: print "No books in the library"
#    - If not empty: 
#      * Print a header like "Books in the library:"
#      * Loop through books with enumerate(books, start=1)
#      * For each book, you can either:
#        Option A: Print the entire dictionary: print(f"{index}. {book}")
#        Option B: Print formatted details: print(f"{index}. Title: {book['title']} | Author: {book['author']} | Year: {book['year']}")
#
#    Choice 'exit':
#    - Print a goodbye message
#    - Break out of the loop
#
#    Invalid choice:
#    - Print an error message asking them to try again
#
# Hint: Access dictionary values using square brackets: my_dict['key']


# TODO: Add the if __name__ == "__main__": block to run main()
