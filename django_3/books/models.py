from django.db import models
from django.urls import reverse
from datetime import date


class Author(models.Model):
    author = models.CharField(max_length=25)

    def __str__(self):
        return self.author


class Book(models.Model):
    name_book = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_publication = models.DateField()

    def __str__(self):
        return self.name_book

    def get_absolute_url(self):
        return reverse('books:books_filter',
                       args=[self.date_publication.year, self.date_publication.month, self.date_publication.day])
