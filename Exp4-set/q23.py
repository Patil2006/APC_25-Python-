# 23. Create a set containing available books and another set containing requested books. Determine which requested books are available.

available_books = {"Python Basics", "Java Programming", "Data Structures", "Web Development"}
requested_books = {"Python Basics", "Data Structures", "C Programming"}

available_requested = available_books.intersection(requested_books)

print("Requested books that are available:", available_requested)