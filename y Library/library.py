# Assignment - Library Catalogue - Angelique Everitt
print()
print("Assignment - Library Catalogue")
print()

class Book:
    """
    A class representing a book in a library.
    """

    def __init__(self, title, author):
        """
        Initialize a new Book instance.

        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
        self.is_available = True

    def check_out(self):
        """
        Check out the book if it's available.

        Returns:
            bool: True if check out is successful, False otherwise
        """
        if self.is_available:
            self.is_available = False
            return True
        else:
            return False

    def return_book(self):
        """
        Return the book to the library.

        Returns:
            bool: True if return is successful, False if it was already available
        """
        if not self.is_available:
            self.is_available = True
            return True
        else:
            return False

    def __str__(self):
        """Return a string representation of the book."""
        status = "Available" if self.is_available else "Checked Out"
        return f"'{self.title}' by {self.author} - {status}"


class Library:
    """
    A class representing a library that manages books.
    """

    def __init__(self):
        """Initialize a new Library instance with an empty catalogue."""
        self.catalogue = []

    def add_book(self, title, author):
        """
        Add a new book to the library catalogue.

        Args:
            title (str): The title of the book
            author (str): The author of the book

        Returns:
            Book: The newly created Book object
        """
        new_book = Book(title, author)
        self.catalogue.append(new_book)
        return new_book

    def find_book(self, title, author=None):
        """
        Find a book in the catalogue by title and optionally by author.

        Args:
            title (str): The title of the book
            author (str, optional): The author of the book

        Returns:
            Book or None: The found Book object or None if not found
        """
        for book in self.catalogue:
            if book.title.lower() == title.lower():
                if author is None or book.author.lower() == author.lower():
                    return book
        return None

    def display_catalogue(self):
        """Display all books in the library catalogue."""
        if not self.catalogue:
            print("The library catalogue is empty.")
            return

        print("Library Catalogue:")
        for i, book in enumerate(self.catalogue, 1):
            print(f"{i}. {book}")


if __name__ == "__main__":
    # Create a new library
    my_library = Library()

    # Add some books to the catalogue
    my_library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    my_library.add_book("To Kill a Mockingbird", "Harper Lee")
    my_library.add_book("1984", "George Orwell")

    # Display the catalogue
    my_library.display_catalogue()

    # Check out a book
    book = my_library.find_book("1984")
    if book:
        book.check_out()
        print(f"\nChecked out: {book}")

    # Show updated catalogue
    my_library.display_catalogue()

    # Return the book
    if book:
        book.return_book()
        print(f"\nReturned: {book}")

    # Show updated catalogue
    my_library.display_catalogue()

    print()
    print("fin")
    print()

    
