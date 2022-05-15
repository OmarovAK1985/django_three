from django.shortcuts import render
from .models import Book
from datetime import date
from django.core.paginator import Paginator


def BookListView(request):
    book_list = Book.objects.all()
    title = 'Каталог книг'
    values = {
        'books': book_list,
        'title': title,
    }
    return render(request, 'books/list_books.html', values)


def BookFilterView(request, year, month, day):
    date_from_model = date(year, month, day)
    date_list = []
    for i in Book.objects.all():
        date_list.append(i.date_publication)
    date_set = set(date_list)
    date_list = list(date_set)
    date_list.sort()
    current_index = date_list.index(date_from_model)
    if current_index < len(date_list) - 1:
        next_index = current_index + 1
        next_date = date_list.pop(next_index)
    else:
        next_date = 1
    if current_index > 0:
        previous_index = current_index - 1
        previous_date = date_list.pop(previous_index)
    else:
        previous_date = 1

    books_filter = Book.objects.filter(date_publication=date_from_model)
    values = {
        'title': f'Каталог книг на дату: {date_from_model}',
        'books': books_filter,
        'next_date': next_date,
        'previous_date': previous_date,
        'current_date': date_from_model,

    }
    return render(request, 'books/books_filter.html', values)
