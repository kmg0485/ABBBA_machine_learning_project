from django.urls import path
from . import views
urlpatterns = [
   
    path('post_view/<int:id>/',views.post_view),
    path('post_view/<int:id>/delete/',views.delete_post, name='delete-post'),
    path('post_view/<int:id>/edit/',views.edit_post, name='edit-post'),
]