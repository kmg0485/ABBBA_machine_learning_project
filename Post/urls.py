from django.urls import path
from . import views
urlpatterns = [
   
    path('post_view/<int:id>/',views.post_view),
    path('upload_post/',views.upload_post),
]