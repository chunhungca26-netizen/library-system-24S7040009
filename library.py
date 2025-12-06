# Global list to store data
library = []

def add_book():
    """Add a new book to the library"""
    print("\n--- ADD NEW BOOK ---")
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    
    book = {
        'title': title,
        'author': author,
        'is_available': True
    }
    
    library.append(book)
    print(f"✓ Book '{title}' added successfully!")

def view_books():
    """Display all books in the library"""
    print("\n--- ALL BOOKS ---")
    
    if len(library) == 0:
        print("No books in the library yet.")
        return
    
    for i, book in enumerate(library, 1):
        status = "Available" if book['is_available'] else "Not Available"
        print(f"\n{i}. Title: {book['title']}")
        print(f"   Author: {book['author']}")
        print(f"   Status: {status}")

def search_book():
    """Search for a book by title keyword"""
    print("\n--- SEARCH BOOK ---")
    query = input("Enter search keyword: ").lower()
    
    found_books = []
    
    for book in library:
        if query in book['title'].lower():
            found_books.append(book)
    
    if len(found_books) == 0:
        print(f"No books found with keyword '{query}'.")
    else:
        print(f"\n✓ Found {len(found_books)} book(s):")
        for i, book in enumerate(found_books, 1):
            status = "Available" if book['is_available'] else "Not Available"
            print(f"\n{i}. Title: {book['title']}")
            print(f"   Author: {book['author']}")
            print(f"   Status: {status}")

def main():
    while True:
        print("\n--- LIBRARY MANAGEMENT SYSTEM ---")
        print("1. Add New Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()