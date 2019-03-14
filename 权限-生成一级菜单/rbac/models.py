from django.db import models


# 权限表
class Permission(models.Model):
    title = models.CharField(max_length=32, verbose_name='标题')
    url = models.CharField(max_length=32, verbose_name='权限')
    is_menu = models.BooleanField(max_length=32,default=False,verbose_name='是否是菜单')
    icon = models.CharField(max_length=32,null=True,blank=True,verbose_name='图标')

    class Meta:
        verbose_name = '权限表'
        verbose_name_plural = '权限表'

    def __str__(self):
        return self.title


# 用户表
class UserInfo(models.Model):
    name = models.CharField(max_length=32, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='密码')
    roles = models.ManyToManyField(to='Role', verbose_name='用户的角色', blank=True)

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = '用户表'

    def __str__(self):
        return self.name


# 角色表
class Role(models.Model):
    name = models.CharField(max_length=32, verbose_name='角色名')
    permissions = models.ManyToManyField(to='Permission', verbose_name='角色拥有的权限', blank=True)

    class Meta:
        verbose_name = '角色表'
        verbose_name_plural = '角色表'

    def __str__(self):
        return self.name
