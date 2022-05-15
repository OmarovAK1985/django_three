from django.shortcuts import render, get_object_or_404
from .models import Phones


def all_phones(request):
    sort = request.GET.get('sort')
    if sort == 'name':
        phone = Phones.objects.order_by('name')
    elif sort == 'min_price':
        phone = Phones.objects.order_by('price')
    elif sort == 'max_price':
        phone = Phones.objects.order_by('-price')
    else:
        phone = Phones.objects.all()

    values = {
        'title': 'Главная страница',
        'phones': phone,
    }
    return render(request, 'phones/index.html', values)


def detail_phone(request, id, name_slug):
    detail = get_object_or_404(Phones, id=id, slug=name_slug)
    values = {
        'title': f'Характеристики телефона {detail.name}',
        'phone': detail,
    }
    return render(request, 'phones/detail.html', values)
