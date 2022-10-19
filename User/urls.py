from django.urls import path
from User import views

app_name = "User"

urlpatterns = [
    path('signup/', views.signup, name='signup'), 
    path('login/', views.login, name='login'), 
    path('logout/', views.logout, name='logout'),
]