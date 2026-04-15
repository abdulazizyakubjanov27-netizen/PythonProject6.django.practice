from django.shortcuts import render
from django.http import HttpResponse
from books.models import Books


def book_list(request):
    books = Books.objects.all()  # Queryset list [<booq1>.
    return render(request,'books/list.html', {"books":books})


def book_detail(request,pk):
    book = Books.objects.filter(id=pk).first()
    return render(request,'books/detail.html', {"book":book})

def book_create_form(request):
    return HttpResponse("Book create form page")

def book_create(request):
    return HttpResponse("Book created")

def book_update_forme(request):
    return HttpResponse("Book update forme")

def book_update(request):
    return HttpResponse("Book update")

def book_delete(request):
    return HttpResponse("Book delete")

