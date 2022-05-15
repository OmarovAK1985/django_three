from books.models import Book
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        name = Book.objects.all()
        for i in name:
            Book.delete(i)
