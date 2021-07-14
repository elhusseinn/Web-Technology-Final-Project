from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request, 'user/register.html')

def signin(request):
    return render(request, 'user/signin.html')