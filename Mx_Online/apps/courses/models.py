# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models

# Create your models here.      ---     课程模块


class Course(models.Model):
    """课程模型类"""
    name = models.CharField(verbose_name=u"课程名", max_length=50)
    desc = models.CharField(verbose_name=u"课程描述", max_length=300)
    detail = models.TextField(verbose_name=u"课程详情")
    degree = models.CharField(
        verbose_name=u"课程难度",
        max_length=2,
        choices=(
            ('primary', u'初级'), ('intermediate', u'中级'), ('advanced', u'高级')
        )
    )
    learn_times = models.IntegerField(verbose_name=u"学习时长(分钟)", default=0)
    students = models.IntegerField(verbose_name=u"学习人数", default=0)
    fav_nums = models.IntegerField(verbose_name=u"收藏人数", default=0)
    image = models.ImageField(verbose_name=u"封面图", upload_to="courses/%Y/%m", max_length=100)
    click_nums = models.IntegerField(verbose_name=u"点击数", default=0)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"课程信息"
        verbose_name_plural = verbose_name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(verbose_name=u"章节名", max_length=100)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"课程章节"
        verbose_name_plural = verbose_name


class Video(models.Model):
    course = models.ForeignKey(Lesson, verbose_name=u"课程章节")
    name = models.CharField(verbose_name=u"视频名", max_length=100)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"章节视频"
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(verbose_name=u"名称", max_length=100)
    download = models.FileField(
        verbose_name=u"资源文件", upload_to="course/resource/%Y/%m", max_length=100
    )
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name
