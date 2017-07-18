# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from users.models import UserProfiles
from courses.models import Course

# Create your models here.      ---     关于用户所有操作的模块


class UserAsk(models.Model):
    name = models.CharField(verbose_name=u"用户姓名", max_length=20)
    mobile = models.CharField(verbose_name=u"手机号", max_length=11)
    course_name = models.CharField(verbose_name=u"课程名", max_length=50)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"用户咨询"
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    user = models.ForeignKey(UserProfiles, verbose_name=u"用户")
    course = models.ForeignKey(Course, verbose_name=u"课程")
    comments = models.CharField(verbose_name=u"评论", max_length=200)
    add_time = models.DateTimeField(verbose_name=u"评论时间", default=datetime.now)

    class Meta:
        verbose_name = u"课程评论"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    """
    用户收藏
    用户需要收藏的有三块: 课程收藏, 讲师收藏, 机构收藏
    通过fav_id和fav_type来指定用户收藏的是哪个,这样就不需要创建多个外键的字段,节省数据库空间
    """
    user = models.ForeignKey(UserProfiles, verbose_name=u"用户")
    fav_id = models.IntegerField(verbose_name=u"数据id", default=0)
    fav_type = models.IntegerField(
        verbose_name=u"收藏类型",
        choices=((1, u'课程'), (2, u'课程机构'), (3, u'讲师')),
        default=1
    )
    add_time = models.DateTimeField(verbose_name=u"收藏时间", default=datetime.now)

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    # user用户,不通过外键来生成,因为网站消息分为2种:
    #   1. 系统发送给所有用户的, 如果通过外键生成,就无法发送给所有用户
    #   2. 定向发送给某个用户的
    # 通过int来生成,在业务逻辑中进行判断,
    # 默认值= 0就是发送给所有用户, 否则保存用户id,就是定向发送给某个用户的
    user = models.IntegerField(verbose_name=u"用户", default=0)
    message = models.CharField(verbose_name=u"消息", max_length=500)
    has_read = models.BooleanField(verbose_name=u"是否已读", default=False)  # 默认未读
    add_time = models.DateTimeField(verbose_name=u"发送时间", default=datetime.now)

    class Meta:
        verbose_name = u"用户消息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.message


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfiles, verbose_name=u"用户")
    course = models.ForeignKey(Course, verbose_name=u"课程")
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"所学课程"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.course.name
