class BookNotFoundException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class BookAlreadyBorrowedException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class MemberLimitExceededException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class MemberNotFoundException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"'{self.title}' by {self.author} (Borrowed: {self.is_borrowed})"

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"'{book.title}' is already borrowed.")
        book.is_borrowed = True
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
        else:
            raise BookNotFoundException(f"'{book.title}' is not borrowed by {self.name}.")

    def __str__(self):
        borrowed_titles = [book.title for book in self.borrowed_books]
        return f"Member: {self.name}, Borrowed Books: {borrowed_titles}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Added book: {book}")

    def add_member(self, name):
        member = Member(name)
        self.members.append(member)
        print(f"Added member: {member}")

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"Book '{title}' not found in the library.")

    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        raise MemberNotFoundException(f"Member '{name}' not found in the library.")

    def borrow_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        member.borrow_book(book)
        print(f"{member_name} borrowed '{book_title}'.")

    def return_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        member.return_book(book)
        print(f"{member_name} returned '{book_title}'.")

library = Library()

library.add_book("Harry Potter 1", "J. K. Rowling")
library.add_book("Harry Potter 2", "J. K. Rowling")
library.add_book("1984", "George Orwell")
library.add_book("Atomic Habits", "James Clear")

library.add_member("Avaz")
library.add_member("Behruz")

try:
    library.borrow_book("Avaz", "1984")
    library.borrow_book("Avaz", "Harry Potter 1")
    library.borrow_book("Avaz", "Atomic Habits")
    library.borrow_book("Avaz", "1984")
except Exception as e:
    print(e)

try:
    library.return_book("Avaz", "1984")
    library.return_book("Avaz", "1984")
except Exception as e:
    print(e)

try:
    library.borrow_book("Behruz", "1984")
    library.borrow_book("Behruz", "Harry Potter 1")
    library.borrow_book("Behruz", "Atomic Habits")
    library.borrow_book("Behruz", "1984")
except Exception as e:
    print(e)