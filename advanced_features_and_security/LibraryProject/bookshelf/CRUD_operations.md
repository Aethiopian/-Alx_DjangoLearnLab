# CRUD Operations on Book Model

## Create Operation

### Command
```python
from bookshelf.models import Book
book = Book.objects.create(title="Django for Beginners", author="William S. Vincent", publication_year=2018)

retrieved_book = Book.objects.get(id=book.id)

## Retrieve Operation
retrieved_book = Book.objects.get(id=book.id)

# Output
<Book: Django for Beginners by William S. Vincent (2018)>


## Update Operation
retrieved_book.title = "Django for Professionals"
retrieved_book.save()

#Output
<Book: Django for Professionals by William S. Vincent (2018)>

## Delete Operation
retrieved_book.delete()

#Output
(1, {'bookshelf.Book': 1})
