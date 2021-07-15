from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import *

# Create your views here.

def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('home')
        return render(request, 'user/profile.html', {'form': form})
    form = PasswordChangeForm(request.user)
    return render(request, 'user/profile.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1']
                                    )
            login(request, new_user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserForm(instance=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
        return render(request, 'user/profile.html', {'form': form, 'users': User.objects.all()})
    form = UserForm(instance=request.user)
    return render(request, 'user/profile.html', {'form': form, 'users': User.objects.all()})


@login_required
def changeAdminStatus(request):
    if not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        user = request.POST.get('username')
        user = User.objects.filter(username=user)[0]
        user.is_superuser = not user.is_superuser
        user.is_staff = not user.is_staff
        user.save()
        return HttpResponse('')
            
    