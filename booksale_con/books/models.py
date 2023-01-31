from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True,null=True)

    def __str__(self):
        return self.name

# class Author(models.Model):
#     name = models.CharField(max_length=50, null=True)
#     slug = models.SlugField(max_length=50, unique=True,null=True)

#     def __str__(self):
#         return self.name

class Book(models.Model):

    name=models.CharField(max_length=200, verbose_name="Kitap Adı")
    category=models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)
    author=models.CharField(max_length=200, null=True)
    description=models.TextField(blank=True, null=True)
    price=models.DecimalField(max_digits=6, decimal_places=2)
    img=models.ImageField(upload_to="books/%Y/%m/%d/")
    available=models.BooleanField(default=True)

    def __str__(self):
        return self.name
