class Book:
    """Represents a book in the library."""

    def __init__(self, title: str, author: str, isbn: str, year: int, genre: str = "General"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.genre = genre
        self._is_available = True

    @property
    def is_available(self) -> bool:
        return self._is_available

    def checkout(self) -> bool:
        if self._is_available:
            self._is_available = False
            return True
        return False

    def return_book(self) -> None:
        self._is_available = True

    def __repr__(self) -> str:
        status = "Available" if self._is_available else "Checked Out"
        return f"Book('{self.title}' by {self.author}, {self.year}) [{status}]"

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "year": self.year,
            "genre": self.genre,
            "available": self._is_available,
        }
