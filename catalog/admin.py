from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, AuthorAdmin

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
#admin.site.register(BookInstance)