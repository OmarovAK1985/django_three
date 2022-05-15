from books.models import Author
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        name = Author.objects.all()
        for i in name:
            Author.delete(i)
