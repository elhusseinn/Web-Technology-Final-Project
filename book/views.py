from django.shortcuts import render
from .models import *

# Create your views here.
def bookDetails(request, book_id):
    book = bookDetail.objects.filter(id=book_id)
    print(book)
    return render(request, 'books/details.html', {"book": book[0]})