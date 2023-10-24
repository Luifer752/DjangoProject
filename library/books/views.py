from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from books.models import Author, Books, Genre


def authors_list(request):
    authors = Author.objects.all()
    context = {'authors': authors, 'title': 'list of Authors'}
    return render(request, 'books/authors_list.html', context)


def books_list(request):
    books = Books.objects.all()
    genres = Genre.objects.all()
    context = {
        'books': books,
        'genres': genres
    }
    return render(request, 'books/books_list.html', context)


def genres_details(request, genre_id=None):
    books = Books.objects.filter(genre__id=genre_id)
    genres = Genre.objects.all()
    try:
        genre = Genre.objects.get(pk=genre_id)
    except Genre.DoesNotExist:
        return HttpResponseNotFound()
    context = {
        'books': books,
        'genres': genres,
        'genre': genre
    }
    return render(request, 'books/genre.html', context)



def add_book(request):
    return


def book_details(request, a=None):
    return