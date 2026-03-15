from django.shortcuts import render

def index(request):
    return render(request, 'layout/index.html')

def aboutus(request):
    return render(request, 'layout/aboutus.html')

def list_books(request):
    return render(request, 'layout/list_books.html')

def one_book(request):
    return render(request, 'layout/one_book.html')

# Create your views here.
