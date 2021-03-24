#coding=utf-8

from django.urls import path
from app.client.views.base import Index
from app.client.views.video import ExVideo
from app.client.views.video import Video_sub,CusVideo
from app.client.views.auth import User,Regist,Logout
from app.client.views.comment import CommentView

urlpatterns=[
    path('',Index.as_view(),name='client_index'),
    path('video/ex',ExVideo.as_view(),name='client_ex_video'),
    path('video/<int:video_id>',Video_sub.as_view(),name='client_video_sub'),
    path('video/custom',CusVideo.as_view(),name='client_cus_video'),
    path('auth',User.as_view(),name='client_auth'),
    path('auth/regist',Regist.as_view(),name='client_regist'),
    path('auth/logout',Logout.as_view(),name='client_logout'),
    path('client/add',CommentView.as_view(),name='client_add_comment')

]