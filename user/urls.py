from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('signin/', auth_views.LoginView.as_view(template_name='user/signin.html'), name='signin'),
    path('signout/', auth_views.LogoutView.as_view(template_name='Home/home.html'), name='signout'),
    path('profile/', views.profile, name="profile")
]