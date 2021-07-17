from django import forms
from .models import bookDetail
from django.utils import timezone
import django_filters

class addBookForm(forms.ModelForm):
    publishDate = forms.DateInput()
    class Meta:
        model = bookDetail
        fields = ['ISBN', 'title', 'author', 'publishDate']

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', field_name='title', label="Title:")
    author = django_filters.CharFilter(lookup_expr='icontains', field_name='author', label="Author:")
    ISBN = django_filters.CharFilter(lookup_expr='icontains', field_name='ISBN', label="ISBN:")

    class Meta:
        model = bookDetail
        fields = ['title', 'author', 'ISBN']
        