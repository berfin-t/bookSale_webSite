from re import T
from django.shortcuts import render
from django.views.generic import TemplateView
from books.models import Book

class IndexView(TemplateView):
    template_name= 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(available=True).order_by('name')[:1]
        context['total_book'] = Book.objects.filter(available=True).count()
        return context

class DiscoverView(TemplateView):
    template_name= 'discover.html'
