from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib.auth import authenticate, login as loginsession
import requests
from django.contrib.auth.decorators import login_required
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    elif request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        UserModel.objects.create_user(username=username, password=password)
        return redirect('User:login')

def login(request):
    if request.method == 'GET' :
        return render(request, 'signin.html') # url 주소가 아닌, html 파일이여서, 수정할 필요 없습니다.
    elif request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user :
            loginsession(request, user)
            return redirect('Post:main')
        else : 
            return redirect('User:login') # 로그인 기능 완성
        
@login_required
def logout(request):
    auth.logout(request)
    return redirect('User:login') # 로그인 페이지로 이동 
        
        
def kakao_social_login(request):
    """
    카카오톧에 나의 애플리케이션의 정보를 담아 사용자에게 카카오 로그인 요청
    """
    if request.method == 'GET':
        client_id = '416dbc093af7d45fc2f47b28d0dd0e14'
        redirect_uri = 'http://127.0.0.1:8000/user/login/kakao/callback'
        # 인가 코드를 받을 uri
        return redirect(
            f'https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code'
        )

def kakao_social_login_callback(request):
    """
    받은 인가 코드, 애플리케이션 정보를 담아 /oath/token/에 post요청하여 접근코드를 받아 처리하는 함수
    """
    try:
        code = request.GET.get('code')
        client_id = '416dbc093af7d45fc2f47b28d0dd0e14'
        redirect_uri = 'http://127.0.0.1:8000/user/login/kakao/callback' # 인가 코드를 받은 URI
        token_request = requests.post(
            'https://kauth.kakao.com/oauth/token', {'grant_type': 'authorization_code',
                                                    'client_id': client_id, 'redierect_uri': redirect_uri, 'code': code}
        )
        
        token_json = token_request.json()
        #------------유효성 검증 --------------#
        error = token_json.get('error', None)

        if error is not None:
            print(error)
            return JsonResponse({"message": "INVALID_CODE"}, status=400)
        #-------------받은 토큰---------------#
        access_token = token_json.get("access_token")

    except KeyError:
        return JsonResponse({"message": "INVALID_TOKEN"}, status=400)

    except access_token.DoesNotExist:
        return JsonResponse({"message": "INVALID_TOKEN"}, status=400)

    #------토큰을 이용하여 사용자 정보 조회------#
    profile_request = requests.get(
        "https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {access_token}"},
    )
    #------사용자 정보를 활용---------------#
    profile_json = profile_request.json()
    kakao_id = profile_json.get('id')
    username = profile_json['properties']['nickname']
    
    if UserModel.objects.filter(kakao_id=kakao_id).exists():
        user = UserModel.objects.get(kakao_id=kakao_id)
        auth.login(request, user)
    else:
        UserModel.objects.create(
            username=username,
            kakao_id=kakao_id,
        )
        user = UserModel.objects.get(kakao_id=kakao_id)
        auth.login(request, user)
    return redirect('Post:main')
