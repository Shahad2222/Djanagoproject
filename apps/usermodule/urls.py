
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('aboutus/', views.aboutus),
    path('list_books/', views.list_books),
    path('one_book/', views.one_book),
]
