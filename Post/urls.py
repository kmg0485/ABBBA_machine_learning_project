from django.urls import path
from django.shortcuts import render, redirect
from . import views
from . import machine


app_name = 'Post'

urlpatterns = [
    # 태그 생성 함수 호출
    path('<int:pk>/tags/', machine.machine, name='tags'),
    
    #페이지 띄우는 함수 호출
    path("", views.main_view, name='main'),
    path("tags/", views.search_view, name="search"),
    path('<int:pk>/',views.post_view, name="post_view"),
    path("comment/<int:pk>",views.edit_comment_view, name="edit_comment"),
    
    # 게시글 관련 함수 호출
    path("upload/", views.upload_img, name="upload_img"),
    path('<int:id>/delete/',views.delete_post, name='delete-post'),
    path('<int:id>/edit/',views.edit_post, name='edit-post'),
    
    # 코멘트 관련 함수 호출
    path("<int:pk>/comment/",views.upload_comment, name="upload_comment"),
    path("comment/<int:pk>/edit",views.edit_comment, name="edit_cmt"),
    path("comment/<int:pk>/delete",views.delete_comment, name="delete_comment"),
    
    # 좋아요 관련 함수 호출
    path('<int:id>/likes', views.likes, name='likes'),
    ]
