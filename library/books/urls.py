from django.urls import path
from .views import books_list, authors_list, genres_details, add_book, book_details

urlpatterns = [
    path('', books_list, name="books_list"),
    path('details', book_details, name="book_details"),
    path('authors', authors_list, name="authors_list"),
    path('books/genres/<int:genre_id>', genres_details, name="genres_details"),
    path('add_book/', add_book, name="add_book")

]

