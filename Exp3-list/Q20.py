"""20.	Create a list of books.
Implement:
•	Add a new book 
•	Search a book 
•	Remove a book 
•	Display all books 
•	Count total books
"""

books = ["Python", "C++", "Java"]

# Add a book
books.append("HTML")

# Search a book
name = input("Enter book to search: ")
if name in books:
    print("Book found")
else:
    print("Book not found")

# Remove a book
remove = input("Enter book to remove: ")
if remove in books:
    books.remove(remove)

# Display all books
print("Books =", books)

# Count total books
print("Total books =", len(books))