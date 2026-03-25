from datetime import date


class Member:
    """Represents a library member."""

    MAX_BOOKS = 5

    def __init__(self, member_id: str, name: str, email: str):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.joined_date = date.today()
        self._borrowed_books: list = []

    @property
    def borrowed_count(self) -> int:
        return len(self._borrowed_books)

    def can_borrow(self) -> bool:
        return self.borrowed_count < self.MAX_BOOKS

    def borrow_book(self, book) -> bool:
        if not self.can_borrow():
            return False
        if book.checkout():
            self._borrowed_books.append(book)
            return True
        return False

    def return_book(self, isbn: str) -> bool:
        for book in self._borrowed_books:
            if book.isbn == isbn:
                book.return_book()
                self._borrowed_books.remove(book)
                return True
        return False

    def get_borrowed_books(self) -> list:
        return list(self._borrowed_books)

    def __repr__(self) -> str:
        return f"Member({self.member_id}, '{self.name}', borrowed={self.borrowed_count})"
