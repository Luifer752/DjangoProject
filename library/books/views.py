from django.shortcuts import render
from django.http import HttpResponse

from books.models import Author


def index(request):
    authors = Author.objects.all()
    context = {'authors': authors, 'title': 'list of Authors'}
    return render(request, 'books/authors_list.html', context)


def test(request):
    print(dir(request))
    return HttpResponse("<h1>Test title</h1>")
