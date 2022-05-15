import csv
import os
from phones.models import Phones
from django.core.management.base import BaseCommand
from transliterate import translit


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        file = os.path.join(os.getcwd(), 'phones.csv')
        my_list = []
        with open(file, mode='r', encoding='utf-8') as file_csv:
            reader = csv.DictReader(file_csv, delimiter=';')
            for i in reader:
                my_list.append(i)
        list_phones_in_model = []
        for i in my_list:
            if len(Phones.objects.all()) == 0:
                slug = i['name'].replace(' ', '_').lower()
                slug = translit(slug, language_code='ru', reversed=True)
                Phones.objects.create(name=i['name'], price=i['price'], image=i['image'], release_date=i['release_date'], lte_exists=i['lte_exists'], slug=slug)
            elif len(Phones.objects.all()) > 0:
                for k in Phones.objects.all():
                    list_phones_in_model.append(str(k))
                if i['name'] not in list_phones_in_model:
                    Phones.objects.create(name=i['name'], price=i['price'], image=i['image'],
                                          release_date=i['release_date'], lte_exists=i['lte_exists'], slug=slug)
