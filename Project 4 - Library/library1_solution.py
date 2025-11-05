all_books = []

def add_book(title, author, year):
    book = {
        'title': title,
        'author': author,
        'year': year
    }
    all_books.append(book)

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
