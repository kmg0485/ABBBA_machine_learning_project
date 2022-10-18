from django.urls import path, include
from User import views

app_name = "User"

urlpatterns = [
    
    path('signup/', views.signup, name='signup'),
]