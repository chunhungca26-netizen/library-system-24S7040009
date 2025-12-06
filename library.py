# Global list to store data
library = []

def add_book():
    """Add a new book to the library"""
    print("\n--- ADD NEW BOOK ---")
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    
    # Create book dictionary
    book = {
        'title': title,
        'author': author,
        'is_available': True
    }
    
    # Add to library
    library.append(book)
    print(f"✓ Book '{title}' added successfully!")

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
            print("Feature coming soon...")
        elif choice == '3':
            print("Feature coming soon...")
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()