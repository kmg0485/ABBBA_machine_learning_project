# 사물인식
import torch
import cv2

from Post.models import PostModel
from django.shortcuts import render, redirect
import simplejson as json


def machine(request, pk) :
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    post = PostModel.objects.get(pk=pk)
   
    imgs = cv2.imread(f'media/{post.photo}')
    results = model(imgs)
    results.save()
    
    result = results.pandas().xyxy[0].to_numpy()
    auto_tags = []
    for k in result :
        if k[6] not in auto_tags :
            auto_tags.append(k[6])
    
    tag = PostModel.objects.get(pk=pk)
    tag.tags = json.dumps(auto_tags)
    tag.author = request.user
    tag.save()
    return redirect('Post:post_view', tag.id)