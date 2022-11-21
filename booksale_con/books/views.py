from django.shortcuts import render
from .models import Book

def books_list(request):
    books = Book.objects.all()
    #category = Category.objects.all()

    context = {
        'books': books,
        #'category':category
    }

    return render(request, 'books.html', context)

def books_detail(request, category_slug, book_id):
    book = Book.objects.get(category__slug=category_slug, id=book_id)

    context = {
        'book':book
    }

    return render(request, 'book.html', context)

def category_list(request, category_slug):
    books = Book.objects.all().filter(category__slug=category_slug)
    category = Category.objects.all()

    context = {
        'books':books,
        'category':category
    }

    return render(request, 'books.html', context)
