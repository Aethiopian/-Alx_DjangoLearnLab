# Delete Operation

## Command
```python
retrieved_book.delete()
# Confirm deletion by trying to retrieve all books
all_books = Book.objects.all()
print(all_books)
```

## Expected Output
```plaintext
<QuerySet []>
```