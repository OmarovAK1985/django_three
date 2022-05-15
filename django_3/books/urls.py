from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.BookListView, name='books_list'),
    path('<int:year>-<int:month>-<int:day>', views.BookFilterView, name='books_filter'),

]