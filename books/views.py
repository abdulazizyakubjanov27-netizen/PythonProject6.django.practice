from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm


# READ (list)
def book_list(request):
    books = Book.objects.all()
    print(books)
    return render(request, 'book/list.html', {'book': books})


# CREATE
def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')

    return render(request, 'book/create.html', {'form': form})


# UPDATE
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect('book_list')

    return render(request, 'book/update.html', {'form': form})


# DELETE
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()
        return redirect('book_list')

    return render(request, 'book/delete.html', {'book': book})