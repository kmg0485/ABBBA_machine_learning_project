from django.urls import path
from User import views

app_name = "User"

urlpatterns = [
    path('', views.signup, name='signup'), # 회원가입 기능 함수 호출
    path('login/', views.login, name='login'), # 로그인 기능 함수 호출
    path('logout/', views.logout, name='logout'), # 로그아웃 기능 함수 호출
path('login/kakao/', views.kakao_social_login, name='kakao_login'),
    path('login/kakao/callback/', views.kakao_social_login_callback, name='kakao_login_callback'),
]