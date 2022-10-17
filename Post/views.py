from django.shortcuts import render, redirect
from Post.models import PostModel
from django.http import HttpResponse
# from User.models import UserModel

# Create your views here.

def upload_img(request) :
    if request.method == 'GET' :
        return render(request, 'upload_post.html')
    elif request.method == 'POST' :
        post = PostModel()
        post.content=request.POST.get('content')
        post.author= request.user
        post.photo = request.FILES['photo']
        post.save()
        post_id = post.id
        # return redirect('post:detail_post', post_id)
        return HttpResponse("db에 잘 저장이 됐을까?")
        # 게시물 띄우는 로직이 아직 없어서 시험삼아 글자를 띄운건데, db에 저장되는 건 확인했습니다.