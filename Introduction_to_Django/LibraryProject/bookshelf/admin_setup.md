# Django Admin Setup for Book Model

## Step 1: Register the Book Model with the Admin Interface

In `bookshelf/admin.py`, import the `Book` model and register it as follows:

```python
from django.contrib import admin
from .models import Book

admin.site.register(Book)