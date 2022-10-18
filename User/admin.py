from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserModel # import 값은 models.py 의 AbstractUser 함수의 새로 지은 변수명을 작성
# Register your models here.

admin.site.register(UserModel, UserAdmin) # 괄호 첫번째의 값은 models.py 의 AbstractUser 함수의 새로 지은 변수명을 작성