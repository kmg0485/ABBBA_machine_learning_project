from django.urls import path
from django.shortcuts import render, redirect
from . import views
from . import machine


app_name = 'Post'

urlpatterns = [
   

    path('post_view/<int:pk>/',views.post_view, name="post_view"),
    path('post_view/<int:id>/delete/',views.delete_post, name='delete-post'),
    path('post_view/<int:id>/edit/',views.edit_post, name='edit-post'),
    path("upload/", views.upload_img, name="upload_img"),
    path("post_view/upload_cmt/<int:pk>/",views.upload_comment, name="upload_comment"),
    path("post_view/delete_cmt/<int:pk>",views.delete_comment, name="delete_comment"),
    path("search/", views.search_view, name="search"),
    path('main/', views.main_view, name='main'),
    path('upload/tags/<int:pk>', machine.machine, name='tags'),
    path('post_view/<int:id>/likes', views.likes, name='likes'),

    ]
