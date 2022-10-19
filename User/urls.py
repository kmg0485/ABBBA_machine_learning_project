from django.urls import path, include
from django.shortcuts import render, redirect
from User import views

app_name = "User"

urlpatterns = [
    path('signup/', views.signup, name='signup'), 
    path('login/', views.login, name='login'), 
]