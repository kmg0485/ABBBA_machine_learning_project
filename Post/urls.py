from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path("upload/", views.upload_img, name="upload_img"),
    # path("detail/<int:pk>/", views.detail_post, name="detail_post"),
]