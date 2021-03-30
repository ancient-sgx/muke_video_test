#coding:utf-8

from django.shortcuts import redirect,reverse
from django.views.generic import View
from app.libs.base_render import render_to_response
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from app.untils.permission import dashboard_auth
from app.model.auth import ClientUser
import mysql.connector

class Login(View):
    TEMPLATE= 'dashboard/auth/login.html'

    def get(self,request):
        if request.user.is_authenticated:
            return redirect(reverse('dashboard_index'))
        to = request.GET.get('to','')

        data={"error":'','to':to}
        return render_to_response(request,self.TEMPLATE,data=data)


    def post(self,request):

        username=request.POST.get('username')
        password=request.POST.get('password')
        to = request.GET.get('to', '')
        data={'error':''}

        exists=User.objects.filter(username=username).exists()
        data['error']='没有该用户'
        if not exists:
            return render_to_response(request,self.TEMPLATE,data=data)
        user=authenticate(username=username,password=password)
        if not user:
            data['error']='密码错误'
            return render_to_response(request,self.TEMPLATE,data=data)
        if not user.is_superuser:#验证是不是超级管理员
            data['error']='你无权限登录'
            return render_to_response(request,self.TEMPLATE,data=data)
        login(request,user)
        if to:
            return redirect(to)
        return redirect(reverse('dashboard_index'))

class Logout(View):

    def get(self,request):
        logout(request)
        return redirect(reverse('dashboard_login'))


class AdminManage(View):
    TEMPLATE='/dashboard/auth/admin.html'
    @dashboard_auth
    def get(self,request):
        users=User.objects.all()
        page = request.GET.get('page',1)
        p=Paginator(users,2)#两个为一页
        total_page = p.num_pages
        if int(page)<=1:
            page=1
        current_page=p.page(int(page)).object_list


        data={'users':current_page,'total':total_page,'page_num':int(page)}
        return render_to_response(request,self.TEMPLATE,data=data)



class UpdateAdminStatus(View):
    def get(self,request):
        status=request.GET.get('status','on')
        _status=True if status == 'on' else False
        request.user.is_superuser=_status
        request.user.save()
        return redirect(reverse('admin_manger'))


class DashboardUser(View):
    TEMPLATE = 'dashboard/auth/user.html'
    @dashboard_auth
    def get(self,request):
        d_users=ClientUser.objects.all()
        data={'users':d_users}
        return render_to_response(request,self.TEMPLATE,data=data)


class Updateuserstatus(View):

    def get(self,request):
        status1 = request.GET.get('status', 'on')
        _status = True if status1 == 'on' else False

        conn = mysql.connector.connect(user='root', password='123456', database='muke_video')
        # 获取游标
        cursor = conn.cursor()
        sql='update app_clientuser set status=%s' %_status
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        return redirect(reverse('dashboard_user'))
