# 사물인식
import torch
import cv2

from Post.models import PostModel
from django.http import HttpResponse


def machine(request, pk) :
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    post = PostModel.objects.get(pk=pk)
   
    imgs = cv2.imread(f'media/{post.photo}')
    results = model(imgs)
    results.save()
    
    result = results.pandas().xyxy[0].to_numpy()
    tags = []
    for k in result :
        tags.append(k[6])
    return HttpResponse(set(tags))