from models.book import Book
from models.member import Member


class Library:
    """Manages the collection of books and members."""

    def __init__(self, name: str):
        self.name = name
        self._books: dict[str, Book] = {}       # isbn -> Book
        self._members: dict[str, Member] = {}   # member_id -> Member

    # --- Book management ---

    def add_book(self, book: Book) -> None:
        if book.isbn in self._books:
            raise ValueError(f"Book with ISBN {book.isbn} already exists.")
        self._books[book.isbn] = book

    def remove_book(self, isbn: str) -> bool:
        if isbn in self._books:
            del self._books[isbn]
            return True
        return False

    def find_book(self, isbn: str) -> Book | None:
        return self._books.get(isbn)

    def search_by_title(self, keyword: str) -> list[Book]:
        keyword = keyword.lower()
        return [b for b in self._books.values() if keyword in b.title.lower()]

    def search_by_author(self, author: str) -> list[Book]:
        author = author.lower()
        return [b for b in self._books.values() if author in b.author.lower()]

    def available_books(self) -> list[Book]:
        return [b for b in self._books.values() if b.is_available]

    # --- Member management ---

    def register_member(self, member: Member) -> None:
        if member.member_id in self._members:
            raise ValueError(f"Member ID {member.member_id} already registered.")
        self._members[member.member_id] = member

    def get_member(self, member_id: str) -> Member | None:
        return self._members.get(member_id)

    # --- Transactions ---

    def checkout_book(self, member_id: str, isbn: str) -> bool:
        member = self.get_member(member_id)
        book = self.find_book(isbn)
        if not member or not book:
            return False
        return member.borrow_book(book)

    def return_book(self, member_id: str, isbn: str) -> bool:
        member = self.get_member(member_id)
        if not member:
            return False
        return member.return_book(isbn)

    # --- Stats ---

    def stats(self) -> dict:
        total = len(self._books)
        available = len(self.available_books())
        return {
            "library": self.name,
            "total_books": total,
            "available": available,
            "checked_out": total - available,
            "total_members": len(self._members),
        }

    def __repr__(self) -> str:
        return f"Library('{self.name}', books={len(self._books)}, members={len(self._members)})"
