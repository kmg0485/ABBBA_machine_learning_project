
from django.shortcuts import render, redirect
from Post.models import PostModel
from django.http import HttpResponse
# from User.models import UserModel
# Create your views here.

def post_view(request, pk):
    if request.method == 'GET':
        post = PostModel.objects.get(pk=pk)
        return render(request, 'detail_post.html', {'post': post})

#아직 구현중
'''def delete_post(request, id):
    post = PostModel.objects.get(id=id)
    post.delete()
    return render(request,'post/main.html' )

def edit_post(request, id):
    post = PostModel.objects.get(id=id)

    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']
        try:
            post.image = request.FILES['image']
        except:
            post.image = None
        post.save()
        return redirect('post_view/'+str(post.id),{'post':post})
    else:
        return render(request, 'post/detail_post.html', {'post':post})'''
        
        
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
        return redirect('Post:post_view', post_id)
        
def search_view(request):
    if request.method == 'POST':
                searched = request.POST['search']        
                photos = PostModel.objects.filter(name__contains=searched)
                return render(request, 'result.html', {'searched': searched, 'photos': photos})
    else:
            return render(request, 'result.html', {})
    

