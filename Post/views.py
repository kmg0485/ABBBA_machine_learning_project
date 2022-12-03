from django.shortcuts import render, redirect, get_object_or_404
from .models import PostModel, CommentModel
import simplejson as json

# pagination
from django.core.paginator import Paginator


# 게시글 띄우기
def post_view(request, pk):
    if request.method == 'GET':
        current_post = PostModel.objects.get(pk=pk) # 해당하는 게시글 불러오기
        current_comment = CommentModel.objects.filter(post_id = pk).order_by('-created_at') # 게시글에 해당하는 코멘트들 불러오기
        # 필드에 저장된 JSON을 다시 리스트 타입 데이터로 변환 
        json_data = json.decoder.JSONDecoder()
        tags = json_data.decode(current_post.tags)
        return render(request, 'detail_post.html', {'post': current_post, 'comment':current_comment, 'tags' : tags})
        

# 게시글 삭제
def delete_post(request, id):
    post = PostModel.objects.get(id=id)
    post.delete()
    return redirect('Post:main')


# 게시글 수정
def edit_post(request, id):
    post = PostModel.objects.get(id=id)
    if request.method == "POST":
        post.content = request.POST['content']
        post.photo = request.FILES['photo']
        post.id = id
        post.save()
        return redirect('Post:tags', post.id)
    else:
        return render(request, 'edit_post.html', {'post':post})
        

# 사진 업로드
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
        return redirect('Post:tags', post_id)
     
    
# 덧글 업로드
def upload_comment(request, pk):
    if request.method == 'POST' :
        comment = CommentModel()
        comment.comment = request.POST.get('comment_content')
        comment.author = request.user
        comment.post = PostModel.objects.get(pk=pk)
        comment.save()
        return redirect('Post:post_view', comment.post_id)
    
    
# 덧글 삭제
def delete_comment(request, pk):
    if request.method == 'POST' :
        comment = CommentModel.objects.get(pk=pk)
        post_id = comment.post_id
        comment.delete()
        return redirect('Post:post_view', post_id)


# 덧글 삭제 페이지 띄우기
def edit_comment_view(request, pk):
    if request.method == 'POST':
        comment = CommentModel.objects.get(pk=pk)
        return render(request, 'edit_comment.html', {'comment':comment})


# 덧글 수정
def edit_comment(request, pk):
    if request.method == 'POST':
        comment = CommentModel.objects.get(pk=pk)
        comment.comment = request.POST.get("comment_content")
        comment.author = request.user
        comment.post = PostModel.objects.get(pk=comment.post_id)
        comment.save()
        return redirect('Post:post_view', comment.post_id)
 

# 검색 기능
def search_view(request):
    if request.method == 'GET':
        searched = request.GET.get('search')
        results = searched.split(',')
        search = []
        for result in results :
            photos = PostModel.objects.filter(tags__icontains=result) # 대소문자 상관 없이 검색어로 검색 결과 띄우기
            search += photos
        paginator = Paginator(search, 12) # 한 페이지에 게시글 12개
        page = request.GET.get('page') # page에 해당하는 value 받아오기
        posts = paginator.get_page(page)
        return render(request, 'result.html', {'searched': searched, 'posts' : posts})


# 메인 페이지 띄우기
def main_view(request) :
    if request.method  == "GET":
        feeds = PostModel.objects.all().order_by('-created_at') # 최근순으로 띄우기
        paginator = Paginator(feeds, 12) # 한 페이지에 게시글 12개
        page = request.GET.get('page') # page에 해당하는 value 받아오기
        posts = paginator.get_page(page) # 받아온 value에 해당하는 페이지 반환
        return render(request,'main.html',{'posts':posts})


# 좋아요 기능
def likes(request, id):
    post = get_object_or_404(PostModel, id=id)
    user = request.user  
    check_like_post = user.like_posts.filter(id=id)

    if check_like_post.exists():
        user.like_posts.remove(post)
        post.like_count -= 1
        post.save()
        return redirect('Post:post_view',id)
    else:
        user.like_posts.add(post)
        post.like_count += 1
        post.save()
        return redirect('Post:post_view',id)
   

