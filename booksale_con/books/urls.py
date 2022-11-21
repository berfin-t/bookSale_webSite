from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_list, name="books"),
    path('<slug:category_slug>/<int:book_id>', views.books_detail, name="books_detail"),
    #path('<slug:author_slug>/<int:author_id>', views.authors_detail, name="authors_detail"),
    path('categories/<slug:category_slug>', views.books_list, name="books_by_category"),
    
]