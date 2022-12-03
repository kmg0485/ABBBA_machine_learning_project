from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    nickname = models.CharField(max_length=500, blank=True)
    like_posts = models.ManyToManyField('Post.PostModel', blank=True, related_name='like_users',)
    kakao_id = models.CharField(max_length=256, null=True, blank=True)

    
