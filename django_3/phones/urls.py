from django.urls import path
from . import views

app_name = 'phones'
urlpatterns = [
    path('', views.all_phones, name='list'),
    path('detail/<int:id>/<slug:name_slug>', views.detail_phone, name='detail'),

]
