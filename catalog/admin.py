from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, AuthorAdmin

admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)

