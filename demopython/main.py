from library import Library
from models import Book, Member
from utils import Calculator


def demo_library():
    print("=== Library Demo ===")
    lib = Library("City Library")

    # Add books
    books = [
        Book("The Pragmatic Programmer", "David Thomas", "978-0-13-595705-9", 2019, "Tech"),
        Book("Clean Code", "Robert C. Martin", "978-0-13-235088-4", 2008, "Tech"),
        Book("Dune", "Frank Herbert", "978-0-441-17271-9", 1965, "Sci-Fi"),
        Book("1984", "George Orwell", "978-0-45-228423-4", 1949, "Dystopia"),
    ]
    for book in books:
        lib.add_book(book)

    # Register members
    alice = Member("M001", "Mamata Gupta", "mamata@gmail.com")
    bob = Member("M002", "Bob Jones", "bob@example.com")
    lib.register_member(alice)
    lib.register_member(bob)

    # Transactions
    lib.checkout_book("M001", "978-0-13-235088-4")  # Alice borrows Clean Code
    lib.checkout_book("M002", "978-0-44-117271-9")  # Bob borrows Dune

    print(lib.stats())
    print("Available:", lib.available_books())
    print("Search 'code':", lib.search_by_title("code"))
    print(alice)

    lib.return_book("M001", "978-0-13-235088-4")
    print("After return:", lib.stats())


def demo_calculator():
    print("\n=== Calculator Demo ===")
    calc = Calculator()
    print(calc.add(10, 5))
    print(calc.multiply(3, 7))
    print(calc.divide(20, 4))
    print("History:", calc.get_history())


if __name__ == "__main__":
    demo_library()
    demo_calculator()
