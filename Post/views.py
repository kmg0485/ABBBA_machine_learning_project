
from django.shortcuts import render, redirect
from Post.models import PostModel, CommentModel
from django.http import HttpResponse
# from User.models import UserModel
# Create your views here.

def post_view(request, pk):
    if request.method == 'GET':
        current_post = PostModel.objects.get(pk=pk)
        current_comment = CommentModel.objects.filter(post_id = pk).order_by('-created_at')
        return render(request, 'detail_post.html', {'post': current_post, 'comment':current_comment})
        


def delete_post(request, id):
    post = PostModel.objects.get(id=id)
    post.delete()
    return redirect('Post:search')

def edit_post(request, id):
    post = PostModel.objects.get(id=id)
    if request.method == "POST":
        post.content = request.POST['content']
        post.photo = request.FILES['photo']
        post.save()
        return redirect('Post:post_view', id)
    else:
        return render(request, 'edit_post.html', {'post':post})
        
        
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
        return redirect('Post:post_view', post_id)
     
def upload_comment(request, pk):
    if request.method == 'POST' :
        comment = CommentModel()
        comment.comment = request.POST.get('comment_content')
        comment.author = request.user
        comment.post = PostModel.objects.get(pk=pk)
        comment.save()
        return redirect('Post:post_view', comment.post_id)
    
def delete_comment(request, pk):
    if request.method == 'POST' :
        comment = CommentModel.objects.get(pk=pk)
        post_id = comment.post_id
        comment.delete()
        return redirect('Post:post_view', post_id)
   
def search_view(request):
    if request.method == 'POST':
        searched = request.POST['search']        
        photos = PostModel.objects.filter(content__contains=searched)
        return render(request, 'result.html', {'searched': searched, 'photos': photos})
    else:
        return render(request, 'result.html', {})
    
    
def main_view(request) :
    feeds = PostModel.objects.all()
    return render(request,'main.html',{'feeds':feeds})