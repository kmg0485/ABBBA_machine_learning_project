
from django.shortcuts import render, redirect
from Post.models import PostModel
from django.http import HttpResponse
# from User.models import UserModel
# Create your views here.

def post_view(request, id):
    if request.method == 'GET':
        post = PostModel.objects.get(id=id)
        return render(request, 'detail_post.html', {'post': post})

#아직 구현중
def delete_post(request, id):
    post = PostModel.objects.get(id=id)
    post.delete()
    return render(request,'main.html' )

def edit_post(request, id):
    post = PostModel.objects.get(id=id)
    if request.method == "POST":
        post.content = request.POST['content']
        post.photo = request.FILES['photo']
        post.save()
        return redirect( 'post/post_view'+str(id), {'post':post})
    else:
        return render(request, 'edit_post.html', {'post':post})
        
        
def upload_img(request) :
    if request.method == 'GET' :
        return render(request, 'upload_post.html')
    elif request.method == 'POST' :
        post = PostModel()
        post.content=request.POST.get('content')
        '''post.author= request.user'''
        post.photo = request.FILES['photo']
        post.save()
        post_id = post.id
        #return redirect('post:detail_post', post_id)
        return HttpResponse("db에 잘 저장이 됐을까?")
        # 게시물 띄우는 로직이 아직 없어서 시험삼아 글자를 띄운건데, db에 저장되는 건 확인했습니다.
        
def search_view(request):
    if request.method == 'POST':
                searched = request.POST['search']        
                photos = PostModel.objects.filter(name__contains=searched)
                return render(request, 'result.html', {'searched': searched, 'photos': photos})
    else:
            return render(request, 'result.html', {})
    

