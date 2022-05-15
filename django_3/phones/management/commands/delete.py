from phones.models import Phones
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        name = Phones.objects.all()
        for i in name:
            Phones.delete(i)
