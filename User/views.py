from django.http import HttpResponse
from django.shortcuts import render
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
        return HttpResponse("회원가입 완료!")


def login(request):
    if request.method == 'GET' :
        return render(request, 'signin.html') # url 주소가 아닌, html 파일이여서, 수정할 필요 없습니다.
    elif request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user :
            loginsession(request, user)
            return HttpResponse(f"추후 메인페이지로 이동하는데, 현재 로그인한 친구는 {request.user}")
        else :
            return HttpResponse("추후 회원가입 페이지로 이동")