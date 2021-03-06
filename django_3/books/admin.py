from django.contrib import admin
from .models import Book, Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author',)
    list_filter = ('author',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'name_book', 'date_publication')
    list_filter = ('author',)
