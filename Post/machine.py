# 사물인식
import torch
import cv2

# 장고와 연동할 때 사용
from Post.models import PostModel
from django.shortcuts import redirect
import simplejson as json



def machine(request, pk) :
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    post = PostModel.objects.get(pk=pk) # PostModel의 인스턴스 생성 후 해당 게시글을 가져온다.
   
    imgs = cv2.imread(f'media/{post.photo}') # photo필드에 담긴 경로에 있는 사진 읽어오기
    results = model(imgs)
    results.save()
    
    result = results.pandas().xyxy[0].to_numpy()

    # 사물 인식 결과를 리스트에 담는다.
    auto_tags = []
    for k in result :
        if k[6] not in auto_tags :
            auto_tags.append(k[6])
    
    # 필드에 리스트 타입의 데이터를 저장하기 위해 simplejson 사용
    post.tags = json.dumps(auto_tags)
    post.author = request.user
    post.save()
    return redirect('Post:post_view', post.id)

