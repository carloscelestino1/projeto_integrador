from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.SignUp.as_view(), name="signup"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]