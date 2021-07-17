from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'Home/home.html')

def about_us(request):
    return render(request, 'Home/about-us.html')
