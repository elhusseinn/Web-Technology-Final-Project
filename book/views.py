from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

@login_required
def bookDetails(request, book_id):
    book = bookDetail.objects.filter(id=book_id)[0]
    bookings = booking.objects.filter(bookedBook=book)
    context = {
        "book": book,
    }
    context['borrowed'] = bookings.exists()
    if context['borrowed']:
        context['borrowedByUser'] = bookings[0].bookedBy == request.user
        context['borrowedUser'] = bookings[0].bookedBy
    else:
        context['borrowedByUser'] = False
        

    return render(request, 'books/details.html', context)

def browse(request):
    books = bookDetail.objects.all()
    if not request.user.is_superuser:
        bookings = booking.objects.all()
        bookedBooks = [b.bookedBook for b in bookings if b.bookedBy != request.user]
        freeBooks = filter(lambda x: x not in bookedBooks, books)
        return render(request, 'books/browse.html', {'books': freeBooks})
    return render(request, 'books/browse.html', {'books': books})


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