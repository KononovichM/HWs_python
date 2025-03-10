# Библиотека
class Book:
    def __init__(self, book_name, author, num_pages, isbn):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.reserved_by = None
        self.issued_to = None

    def reserve(self, reader):
        if self.reserved_by or self.issued_to:
            print("Book is already reserved or issued.")
            return False
        self.reserved_by = reader
        return True

    def cancel_reserve(self, reader):
        if self.reserved_by == reader:
            self.reserved_by = None
            return True
        print("You cannot cancel reservation of this book.")
        return False

    def get_book(self, reader):
        if self.issued_to or self.reserved_by not in [None, reader]:
            print("Book is not available.")
            return False
        self.issued_to = reader
        self.reserved_by = None
        return True

    def return_book(self, reader):
        if self.issued_to == reader:
            self.issued_to = None
            return True
        print("You cannot return this book.")
        return False


class Reader:
    def __init__(self, name):
        self.name = name

    def reserve_book(self, books):
        if books.reserve(self):
            print(f"{self.name} reserved the book.")

    def cancel_reserve(self, book1):
        if book1.cancel_reserve(self):
            print(f"{self.name} canceled the reservation.")

    def get_book(self, book1):
        if book1.get_book(self):
            print(f"{self.name} got the book.")

    def return_book(self, book1):
        if book1.return_book(self):
            print(f"{self.name} returned the book.")


# Тестирование
book = Book("The Hobbit", "J.R.R. Tolkien", 400, "0006754023")

vasya = Reader("Vasya")
petya = Reader("Petya")

vasya.reserve_book(book)
petya.reserve_book(book)
vasya.cancel_reserve(book)

petya.reserve_book(book)
vasya.get_book(book)
petya.get_book(book)
vasya.return_book(book)
petya.return_book(book)

vasya.get_book(book)
