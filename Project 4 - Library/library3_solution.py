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

def book_list():
    return all_books

def main():
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
                    print(f"{index}. {book})")
                    # print(f"{index}. Title: {book['title']} | Author: {book['author']} | Year: {book['year']}")
                print()

        elif choice == 'exit':
            print("Exiting the library program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

        
if __name__ == "__main__":
    main()
