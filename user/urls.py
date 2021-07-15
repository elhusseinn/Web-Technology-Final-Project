from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('signin/', auth_views.LoginView.as_view(template_name='user/signin.html'), name='signin'),
    path('signout/', auth_views.LogoutView.as_view(), name='signout'),
    path('profile/changepassword', views.changePassword, name='changepassword'),
    path('profile/', views.profile, name="profile"),
    path('changeAdminStatus', views.changeAdminStatus, name='changeadminstatus')
]