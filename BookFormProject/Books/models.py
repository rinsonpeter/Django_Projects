from django.db import models

# Create your models here.
class Book(models.Model):
    book_name=models.CharField(max_length = 120)
    author = models.CharField(max_length = 120)
    price=models.IntegerField(default = 100)
    pages = models.IntegerField()

    def __str__(self):
        return self.book_name

