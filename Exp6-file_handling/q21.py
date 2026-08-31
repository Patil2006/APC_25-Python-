# Q21. Book management: add, search, issue, return and display available books

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")

    file = open("books.txt", "a")
    file.write(book_id + "," + title + "," + author + ",Available\n")
    file.close()

    print("Book added successfully.")


def search_book():
    book_id = input("Enter Book ID: ")

    file = open("books.txt", "r")

    found = False

    for line in file:
        data = line.strip().split(",")

        if data[0] == book_id:
            print("Book Found:", data)
            found = True

    file.close()

    if not found:
        print("Book not found.")


def display_available():
    file = open("books.txt", "r")

    print("\nAvailable Books:")

    for line in file:
        data = line.strip().split(",")

        if data[3] == "Available":
            print(data)

    file.close()


def update_status(book_id, status):
    file = open("books.txt", "r")
    lines = file.readlines()
    file.close()

    file = open("books.txt", "w")

    for line in lines:
        data = line.strip().split(",")

        if data[0] == book_id:
            data[3] = status

        file.write(",".join(data) + "\n")

    file.close()


def issue_book():
    book_id = input("Enter Book ID: ")
    update_status(book_id, "Issued")
    print("Book issued successfully.")


def return_book():
    book_id = input("Enter Book ID: ")
    update_status(book_id, "Available")
    print("Book returned successfully.")


# Create file with sample books
file = open("books.txt", "w")
file.write("101,Python Basics,John,Available\n")
file.write("102,Java Programming,James,Available\n")
file.write("103,C Programming,Robert,Issued\n")
file.close()


while True:

    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        search_book()

    elif choice == "3":
        issue_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        display_available()

    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")