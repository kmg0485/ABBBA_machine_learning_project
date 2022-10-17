from django.shortcuts import render
from .models import PostModel
# Create your views here.

def post_view(request, id):
    if request.method == 'POST':
        comment = request.POST.get("comment", "")
        post = PostModel.objects.get(id=id)

        Posts = PostModel
        Posts.comment = comment
        Posts.author = request.user
        Posts.image = image
        Posts.save()
    elif request.method == 'GET':
        return render(request, 'upload_post.html' )

def upload_post(request):
    pass
