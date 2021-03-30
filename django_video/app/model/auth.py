
from django.db import models
import hashlib

def hash_password(password):
    if isinstance(password,str):#isinstance判断password是不是一个str类型
        password=password.encode('utf-8')#变为比特类型
    return hashlib.md5(password).hexdigest().upper()


class ClientUser(models.Model):
    username =models.CharField(max_length=50,null=False,unique=True)#最大长度为50，不能为空，是唯一索引
    password=models.CharField(max_length=255,null=False)#最大长度是255，不能为空
    avader=models.CharField(max_length=500,default='')#头像最大长度500，默认为空
    gender=models.CharField(max_length=10,default='')#最大长度为10，默认为空
    birthday=models.DateTimeField(null=True,blank=True,default=None)#可以为空
    status=models.BooleanField(default=True,db_index=True)#状态默认是True,普通索引
    create_time =models.DateTimeField(auto_now_add=True)#只有第一次创建的时候自己增加

    def __str__(self):
        return 'username:{}'.format(self.username)
    #给密码加密
    @classmethod
    def add(cls,username,password,avatar='',gender='',birthday=None):
        return cls.objects.create(
            username=username,
            password=hash_password(password),
            avader=avatar,
            gender=gender,
            birthday=birthday,
            status=True
        )
    @classmethod
    def get_user(cls,username,password):
        try:
            user=cls.objects.get(
                username=username,
                password=hash_password(password)
            )
            return user
        except:
            return None

    def update_password(self,old_password,new_password):
        hash_old_password=hash_password(old_password)
        if hash_old_password !=self.password:
            return False
        hash_new_password=hash_password(new_password)
        self.password=hash_new_password
        self.save()
        return True

    def update_status(self):

        self.status = not self.status
        self.save()
        return True