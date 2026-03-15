from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('list_books/', views.list_books, name='list_books'),
    path('one_book/', views.one_book, name='one_book'),
]

