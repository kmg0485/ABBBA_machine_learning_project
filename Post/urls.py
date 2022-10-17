from django.urls import path
from . import views


app_name = 'Post'

urlpatterns = [
   
    path('post_view/<int:id>/',views.post_view),
    path('post_view/<int:id>/delete/',views.delete_post, name='delete-post'),
    path('post_view/<int:id>/edit/',views.edit_post, name='edit-post'),
    path("upload/", views.upload_img, name="upload_img"),
    path("search/", views.search_view, name="search"),

    # path("detail/<int:pk>/", views.detail_post, name="detail_post"),
    ]
