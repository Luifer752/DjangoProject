from django.contrib import admin

from  books.models import Author, Books, Genre

admin.site.register(Author)
admin.site.register(Books)
admin.site.register(Genre)

