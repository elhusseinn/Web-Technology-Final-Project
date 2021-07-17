from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import *
from .forms import *


@login_required
def editBook(request, book_id):
    if not request.user.is_superuser:
        return redirect('home')
    book = bookDetail.objects.filter(id=book_id)[0]
    if request.method == "POST":
        form = addBookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect('browse')
        return render(request, 'books/editBook.html', {"form": form})
    form = addBookForm(instance=book)
    return render(request, 'books/editBook.html', {"form": form})
    

@login_required
def extendBorrowPeriod(request):
    toExtend = booking.objects.filter(bookedBy = request.user)[0]
    toExtend.returnDate = toExtend.returnDate + timezone.timedelta(days=10)
    toExtend.save()
    return redirect('browse')

@login_required
def deleteBook(request, book_id):
    if not request.user.is_superuser:
        return redirect('home')
    bookDetail.objects.filter(id=book_id)[0].delete()
    return redirect('browse')

@login_required
def borrowBook(request, book_id):
    toBorrow = bookDetail.objects.filter(id=book_id)[0]
    newBooking = booking()
    newBooking.bookedBy = request.user
    newBooking.bookedBook = toBorrow
    newBooking.save()
    return redirect('browse')


@login_required
def returnBook(request):
    toDelete = booking.objects.filter(bookedBy = request.user)
    toDelete.delete()
    return redirect('browse')

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
        context['returnDate'] = bookings[0].returnDate
    else:
        context['borrowedByUser'] = False
        

    return render(request, 'books/details.html', context)

def browse(request):
    books = bookDetail.objects.all()
    filteredBooks = BookFilter(request.GET, queryset=books)
    return render(request, 'books/browse.html', {'books': filteredBooks})


@login_required
def addBook(request):
    if not request.user.is_superuser:
        return redirect('home')
    if request.method == "POST":
        form = addBookForm(request.POST)
        if form.is_valid():
            book = form.save()
            book.save()
            return redirect('browse')
        return render(request, 'books/addBook.html', {"form": form})
    form = addBookForm()
    return render(request, 'books/addBook.html', {"form": form})