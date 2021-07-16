from django import forms
from .models import bookDetail
from django.utils import timezone

class addBookForm(forms.ModelForm):
    publishDate = forms.DateInput()
    class Meta:
        model = bookDetail
        fields = ['ISBN', 'title', 'author', 'publishDate']
        