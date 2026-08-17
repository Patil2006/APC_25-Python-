# 29. Create a dictionary containing book IDs and book names.
# Implement:
# • Add a book
# • Search a book
# • Remove a book
# • Display all books
# • Count total books

books = {
    101: "Python",
    102: "Java",
    103: "C++"
}

books[104] = "HTML"

book_id = 102
if book_id in books:
    print("Book found:", books[book_id])
else:
    print("Book not found")

del books[103]

print("All books:")
for book_id, book_name in books.items():
    print(book_id, ":", book_name)

print("Total books:", len(books))