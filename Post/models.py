# 모델링
from django.db import models


# 사진
import os
from uuid import uuid4
from django.utils import timezone
from django.conf import settings

#태그

class PostModel(models.Model) :
    content = models.TextField()
    author = models.ForeignKey('User.UserModel', on_delete=models.CASCADE, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    like_count = models.PositiveIntegerField(default=0, )
    tags = models.TextField()
   
    def upload_img(instance, filename):
        # upload_to="%Y/%m/%d" 처럼 날짜로 세분화
        ymd_path = timezone.now().strftime('%Y/%m/%d')

        # 길이 32 인 uuid 값
        uuid_name = uuid4().hex

        # 확장자 추출
        extension = os.path.splitext(filename)[-1].lower()

        # 결합 후 return
        return '/'.join([
            ymd_path,
            uuid_name + extension,
        ])

    photo = models.ImageField(upload_to=upload_img)

    def __str__(self):
        return str(F'{self.author.username}의 글 내용 : {self.content}')

class CommentModel(models.Model) :
    author = models.ForeignKey('User.UserModel', on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
