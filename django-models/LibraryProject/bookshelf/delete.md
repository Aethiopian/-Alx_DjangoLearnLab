
# Delete Operation

## Command
```python
from bookshelf.models import Book
retrieved_book = Book.objects.get(title="1984")
retrieved_book.delete()
# Confirm deletion by trying to retrieve all books
all_books = Book.objects.all()
print(all_books)
```

## Expected Output
```plaintext
<QuerySet []>
```
