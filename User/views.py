from django.http import HttpResponse
from django.shortcuts import render
from .models import UserModel
from django.contrib.auth import authenticate, login as loginsession

# Create your views here.
def signup(request):
    return render(request, "signup.html")

def login(request):
    if request.method == 'GET' :
        return render(request, 'signin.html')
    elif request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user :
            loginsession(request, user)
            return HttpResponse(f"추후 메인페이지로 이동하는데, 현재 로그인한 친구는 {request.user}")
        else :
            return HttpResponse("추후 회원가입 페이지로 이동")