# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# 第一块区域引用Python内部的模块
from datetime import datetime

# 第二快区域引用第三方的模块
from django.db import models
from django.contrib.auth.models import AbstractUser

# 第三块是引用自己定义的模块区域


# Create your models here.      ---     用户模块


class UserProfiles(AbstractUser):
    """
    如何通过扩展Django默认的用户表,自定义自己的用户表?
    
    需要继承AbstractUser中的默认字段，然后才能扩展自己用户模块中的特有字段
    继承了父类中的字段有:  
        id              主键
        password        密码
        last_login      是否登录
        is_superuser    是否是超级管理员
        username        用户名
        first_name      扩展名
        last_name       扩展名
        email           邮箱
        is_staff        是否是员工
        is_active       当前账号是否激活
        date_joined
        
    注意: 其中username和password是必选的,其他是可选的
    """
    nick_name = models.CharField(verbose_name=u"昵称", max_length=50, default="")
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    # choices一个二维元组组合,多项选择集合  默认是选择框形式显示在后台,默认添加的性别为男生
    gender = models.CharField(
        verbose_name=u"性别",  max_length=5, choices=(('male', u'男'), ('female', u'女')), default='male'
    )
    address = models.CharField(verbose_name=u"地区", max_length=100, default="")
    mobile = models.CharField(verbose_name=u"手机号", max_length=11, null=True, blank=True)
    # 用户上传的头像 地址默认存储:images/年份/月份/日期,  没有上传则默认使用静态文件的一张图片地址
    image = models.ImageField(
        verbose_name=u"头像", upload_to="images/%Y/%m/%d", default=u"images/default.png", max_length=100
    )

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name  # verbose_name的复数形式,如果不指定 值为:verbose_name的值加上一个s

    def __unicode__(self):
        return self.username  # 返回父类中的username字段值


class EmailVerifyRecord(models.Model):
    code = models.CharField(verbose_name=u"验证码", default=20, max_length=20)
    # 最大长度默认是254
    email = models.EmailField(verbose_name=u"邮箱")
    send_type = models.CharField(
        verbose_name=u"验证码类型",
        choices=(('register', u'注册'), ('forget', u'找回密码')),
        max_length=50
    )
    # datetime.now需要去掉()
    # 如果加上括号,此字段就不会按照在对象实例化时的时间来进行复制,而是按照这个模型类编译的时间赋值
    send_time = models.DateTimeField(verbose_name=u"发送时间", default=datetime.now, max_length=10)

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField(verbose_name=u"标题", max_length=100)
    image = models.ImageField(verbose_name=u"轮播图", max_length=200)
    url = models.URLField(verbose_name=u"访问地址", max_length=200)
    # 图片的排列,让最小的值排在最前面
    index = models.IntegerField(verbose_name=u"顺序", default=100)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name
