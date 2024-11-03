### Create Operation

#### Command
```python
from bookshelf.models import Book
book = Book.objects.create(title="Django for Beginners", author="William S. Vincent", publication_year=2018)
