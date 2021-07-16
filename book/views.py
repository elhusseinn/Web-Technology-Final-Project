from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

@login_required
def bookDetails(request, book_id):
    book = bookDetail.objects.filter(id=book_id)
    return render(request, 'books/details.html', {"book": book[0]})

def browse(request):
    books = bookDetail.objects.all()
    bookings = booking.objects.all()
    bookedBooks = [b.bookedBook for b in bookings if b.bookedBy != request.user]
    freeBooks = filter(lambda x: x not in bookedBooks, books)
    return render(request, 'books/browse.html', {'books': freeBooks})


@login_required
def addBook(request):
    if not request.user.is_superuser:
        return redirect('home')
    if request.method == "POST":
        form = addBookForm(request.POST)
        if form.is_valid():
            book = form.save()
            book.save()
            return redirect('home')
        return render(request, 'books/addBook.html', {"form": form})
    form = addBookForm()
    return render(request, 'books/addBook.html', {"form": form})