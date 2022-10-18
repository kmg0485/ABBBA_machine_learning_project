from django.urls import path, include
from User import views

app_name = "User"

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'), # 221018 / 14:49 문제 없음
]