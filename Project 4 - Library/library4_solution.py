users = ["Alice", "Bob", "Charlie", "Librarian"]

all_books = []

def add_book(title, author, year):
    book = {
        'title': title,
        'author': author,
        'year': year
    }
    all_books.append(book)

def remove_book(title):
    global all_books
    all_books = [book for book in all_books if book['title'].lower() != title.lower()]

def update_book(old_title, new_title=None, new_author=None, new_year=None):
    for book in all_books:
        if book['title'].lower() == old_title.lower():
            if new_title:
                book['title'] = new_title
            if new_author:
                book['author'] = new_author
            if new_year:
                book['year'] = new_year
            break

def checkout_book(title, student_name):
    for book in all_books:
        if book['title'].lower() == title.lower():
            if 'checked_out_by' not in book:
                book['checked_out_by'] = student_name
                return f"Book '{title}' has been checked out by {student_name}."
            else:
                return f"Book '{title}' is already checked out by {book['checked_out_by']}."
    return f"Book '{title}' not found in the library."

def return_book(title):
    for book in all_books:
        if book['title'].lower() == title.lower():
            if 'checked_out_by' in book:
                del book['checked_out_by']
                return f"Book '{title}' has been returned."
            else:
                return f"Book '{title}' was not checked out."
    return f"Book '{title}' not found in the library."

def book_list():
    return all_books

def authenticate_user():
    name = input("Enter your name: ").strip()
    if name in users[:-1]:  # Exclude 'Librarian' from student list
        print(f"Welcome, {name}!")
        return name
    elif name == "Librarian":
        print("Welcome, Librarian! You have full access.")
        return name
    else:
        print("Authentication failed. You are not recognized as a student.")
        return None

def main():
    user = authenticate_user()
    if not user:
        return
    if user == "Librarian":
        print("As a Librarian, you can add, remove, update, checkout, and return books.")
        while True:
            print("Would you like to add a book to the library? Or would you like to see all the books?")
            choice = input("Type 'add' to add a book, 'list' to see all books, or 'exit' to quit: ").strip().lower()

            if choice == 'add':
                title = input("Enter the book title: ").strip()
                author = input("Enter the book author: ").strip()
                year = input("Enter the publication year: ").strip()
                add_book(title, author, year)
                print(f"Book '{title}' added to the library.\n")
            
            elif choice == 'list':
                books = book_list()
                if not books:
                    print("No books in the library.\n")
                else:
                    print("Books in the library:")
                    for index, book in enumerate(books, start=1):
                        print(f"{index}. Title: {book['title']} | Author: {book['author']} | Year: {book['year']}")
                    print()

            elif choice == 'exit':
                print("Exiting the library program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")
    
    elif user in users[:-1]:
        print("As a student, you can checkout and return books.")
        while True:
            print("Would you like to checkout a book or return a book?")
            choice = input("Type 'checkout' to checkout a book, 'return' to return a book, 'list' to see all books, or 'exit' to quit: ").strip().lower()

            if choice == 'checkout':
                title = input("Enter the book title to checkout: ").strip()
                message = checkout_book(title, user)
                print(message + "\n")
            
            elif choice == 'return':
                title = input("Enter the book title to return: ").strip()
                message = return_book(title)
                print(message + "\n")
            
            elif choice == 'list':
                books = book_list()
                if not books:
                    print("No books in the library.\n")
                else:
                    print("Books in the library:")
                    for index, book in enumerate(books, start=1):
                        print(f"{index}. Title: {book['title']} | Author: {book['author']} | Year: {book['year']}")
                    print()

            elif choice == 'exit':
                print("Exiting the library program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")

        
if __name__ == "__main__":
    main()
