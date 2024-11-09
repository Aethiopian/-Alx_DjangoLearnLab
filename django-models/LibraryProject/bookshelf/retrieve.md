# Retrieve Operation

## Command
```python
retrieved_book = Book.objects.get(title="1984")
print(retrieved_book)
```

## Expected Output
```plaintext
<Book: 1984 by George Orwell (1949)>
```