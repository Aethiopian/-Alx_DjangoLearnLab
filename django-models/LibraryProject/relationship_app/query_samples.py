# relationship_app/query_samples.py

import django
import os

# Initialize Django to run standalone scripts
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """Query all books by a specific author."""
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with the name '{author_name}'")

def list_books_in_library(library_name):
    """List all books in a specific library."""
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in the library '{library_name}':")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'")

def retrieve_librarian_for_library(library_name):
    """Retrieve the librarian for a specific library."""
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # Access the OneToOneField relationship
        print(f"Librarian for the library '{library_name}': {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to the library '{library_name}'")

# Example function calls:
if __name__ == "__main__":
    query_books_by_author("Author Name")  # Replace "Author Name" with an actual author name
    list_books_in_library("Library Name")  # Replace "Library Name" with an actual library name
    retrieve_librarian_for_library("Library Name")  # Replace "Library Name" with an actual library name