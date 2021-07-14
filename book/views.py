from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def bookDetails(request, book_id):
    book = bookDetail.objects.filter(id=book_id)
    return render(request, 'books/details.html', {"book": book[0]})

def browse(request):
    books = bookDetail.objects.filter(borrowed=False)
    return render(request, 'books/browse.html', {'books': books})