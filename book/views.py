from django.shortcuts import render

# Create your views here.
def bookDetails(request, book_id):
    return render(request, 'books/details.html')