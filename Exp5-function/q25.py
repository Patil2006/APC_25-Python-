# 25. Create functions to add books, issue books, return books, search books, and display available books.
# Maintain book availability using dictionaries.

books = {}

def add_book(book_id, title):
    books[book_id] = {"title": title, "available": True}
    print("Book added successfully.")

def issue_book(book_id):
    if book_id in books:
        if books[book_id]["available"]:
            books[book_id]["available"] = False
            print("Book issued successfully.")
        else:
            print("Book is already issued.")
    else:
        print("Book not found.")

def return_book(book_id):
    if book_id in books:
        if not books[book_id]["available"]:
            books[book_id]["available"] = True
            print("Book returned successfully.")
        else:
            print("Book is already available.")
    else:
        print("Book not found.")

def search_book(title):
    found = False

    for book_id, book in books.items():
        if title.lower() in book["title"].lower():
            print("Book ID:", book_id)
            print("Title:", book["title"])
            print("Available:", book["available"])
            found = True

    if not found:
        print("Book not found.")

def display_available_books():
    print("Available Books:")

    for book_id, book in books.items():
        if book["available"]:
            print("Book ID:", book_id, "Title:", book["title"])

add_book("B101", "Python Programming")
add_book("B102", "Data Structures")
add_book("B103", "Computer Networks")

issue_book("B101")
return_book("B101")
search_book("Python")
display_available_books()