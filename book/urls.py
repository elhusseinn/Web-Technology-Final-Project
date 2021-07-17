from django.urls import path
from . import views

urlpatterns = [
    path('<int:book_id>/details/', views.bookDetails, name='bookdetails'),
    path('browse/', views.browse, name='browse'),
    path('addBook/', views.addBook, name='addbook'),
    path('returnBook/', views.returnBook, name='returnbook'),
    path('<int:book_id>/borrow/', views.borrowBook, name='borrowbook'),
    path('<int:book_id>/delete/', views.deleteBook, name="deletebook"),
    path('extend', views.extendBorrowPeriod, name="extend"),
    path('<int:book_id>/edit', views.editBook, name='editbook')
]