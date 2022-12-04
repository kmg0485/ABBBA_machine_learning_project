from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    nickname = models.CharField(max_length=30)
    like_posts = models.ManyToManyField('Post.PostModel',null=True, blank=True, related_name='like_users',)
    kakao_id = models.CharField(max_length=50, null=True, blank=True)

    
