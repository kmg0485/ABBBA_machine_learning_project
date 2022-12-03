from django.urls import path
from User import views

app_name = "User"

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login, name='login'), 
    path('logout/', views.logout, name='logout'), 
    path('login/kakao/', views.kakao_social_login, name='kakao_login'),
    path('login/kakao/callback/', views.kakao_social_login_callback, name='kakao_login_callback'),
]