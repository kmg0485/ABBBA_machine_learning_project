from django.db import models
from django.contrib.auth.models import AbstractUser
from Post.models import PostModel

# Create your models here.
class UserModel(AbstractUser):
    nickname = models.CharField(max_length=500, blank=True)
    like_posts = models.ManyToManyField('Post.PostModel', blank=True, related_name='like_users',)

   