from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Display these fields in the admin list view
    list_filter = ('publication_year',)  # Filter by publication year
    search_fields = ('title', 'author')  # Add search capabilities by title and author
