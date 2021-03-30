# coding=utf-8

from django.urls import path
from app.dashboard.views.base import Index
from app.dashboard.views.auth import (Login,AdminManage,Logout,
UpdateAdminStatus,DashboardUser,Updateuserstatus)
from  app.dashboard.views.video import (ExternaVideo,VideoSubView,
VideoStartView,StarDelete,SubDelete,VideoUpdate,VideoUpdateStatus)


urlpatterns = [
    path('',Index.as_view(),name='dashboard_index'),
    path('login',Login.as_view(),name='dashboard_login'),
    path('admin/manger',AdminManage.as_view(),name='admin_manger'),
    path('logout',Logout.as_view(),name='logout'),
    path('admin/manger/update/status',UpdateAdminStatus.as_view(),name='admin_update_status'),
    path('video/externa',ExternaVideo.as_view(),name='externa_video'),
    path('video/videosub/<int:video_id>',VideoSubView.as_view(),name='video_sub'),
    path('video/star',VideoStartView.as_view(),name='video_star'),
    path('video/star/delete/<int:star_id>/<int:video_id>',StarDelete.as_view(),name='star_delete'),
    path('video/sub/delete/<int:videosub_id>/<int:video_id>',SubDelete.as_view(),name='sub_delete'),
    path('video/update/<int:video_id>',VideoUpdate.as_view(),name='video_update'),
    path('video/update/status/<int:video_id>',VideoUpdateStatus.as_view(),name='video_update_status'),
    path('user',DashboardUser.as_view(),name='dashboard_user'),
    path('user/update/status',Updateuserstatus.as_view(),name='update_user_status')
]