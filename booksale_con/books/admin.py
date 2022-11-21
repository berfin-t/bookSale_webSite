from django.contrib import admin
from . models import Book, Category

admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('name','available')
    search_fields=('name')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
