from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib.auth import authenticate, login as loginsession

# Create your views here.
def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    elif request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        UserModel.objects.create_user(username=username, password=password)
        return redirect("User:login")


def login(request):
    if request.method == 'GET' :
        return render(request, 'signin.html') # url 주소가 아닌, html 파일이여서, 수정할 필요 없습니다.
    elif request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user :
            loginsession(request, user)
            return redirect('Post:search')
        else : 
            return redirect('User:signup')