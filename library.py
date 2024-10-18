library = []

# Function to add a new book to the library
def add_book(title, author, year):
    book = {
        'title': title,
        'author': author,
        'year': year,
        'available': True
    }
    library.append(book)
    print(f"Book '{title}' added to the library!")

# Function to update the availability of a book when borrowed or returned
def update_availability(title, is_borrowed):
    for book in library:
        if book['title'].lower() == title.lower():
            if is_borrowed:
                if book['available']:
                    book['available'] = False
                    print(f"Book '{title}' has been borrowed.")
                else:
                    print(f"Book '{title}' is already borrowed.")
            else:
                if not book['available']:
                    book['available'] = True
                    print(f"Book '{title}' has been returned.")
                else:
                    print(f"Book '{title}' was not borrowed.")
            return
    print(f"Book '{title}' not found in the library.")

# Function to display all available books
def display_available_books():
    available_books = [book for book in library if book['available']]
    if available_books:
        print("Available books:")
        for book in available_books:
            print(f"{book['title']} by {book['author']} ({book['year']})")
    else:
        print("No books are currently available.")

# Sample Usage
add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
add_book("To Kill a Mockingbird", "Harper Lee", 1960)
add_book("1984", "George Orwell", 1949)

# Display available books
display_available_books()

# Borrow a book
update_availability("The Great Gatsby", is_borrowed=True)

# Display available books again
display_available_books()

# Return a book
update_availability("The Great Gatsby", is_borrowed=False)

# Display available books after return
display_available_books()