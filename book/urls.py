from django.urls import path
from . import views

urlpatterns = [
    path('<int:book_id>/details/', views.bookDetails, name='bookdetails')
]