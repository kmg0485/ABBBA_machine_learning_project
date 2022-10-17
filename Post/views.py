from django.shortcuts import render,redirect
from .models import PostModel
# Create your views here.

def post_view(request, id):
    if request.method == 'GET':
        post = PostModel.objects.get(id=id)
        return render(request, 'post/detail_post.html', {'post': post})

def delete_post(request, id):
    post = PostModel.objects.get(id=id)
    post.delete()
    return render(request,'post/main.html' )

def edit_post(request, id):
    post = PostModel.objects.get(id=id)

    if request.method == "POST":
        post.content = request.POST['content']
        try:
            post.image = request.FILES['image']
        except:
            post.image = None
        post.save()
        return redirect('post_view/'+str(post.id),{'post':post})
    elif request.method == "GET":
        post = PostModel.objects.get(id=id)
        return render(request, 'post/edit_post.html', {'post':post})

