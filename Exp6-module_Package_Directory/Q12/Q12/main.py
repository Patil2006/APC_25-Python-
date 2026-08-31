from books.book_details import book_details
from books.book_search import search_book
from members.member_details import member_details
from members.member_registration import register_member
from transactions.issue import issue_book
from transactions.return_book import return_book

book_details()
search_book("Python Programming")

member_details()
register_member("Bhakti")

issue_book("Python Programming")
return_book("Python Programming")