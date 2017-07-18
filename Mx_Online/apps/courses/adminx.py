# -*- coding: utf-8 -*-
import xadmin

from .models import Course, Lesson, Video, CourseResource

__author__ = 'Dunn'
__date__ = '2017/7/18 下午4:28'


class CourseAdmin(object):
    """
    课程模型类后台管理器
    """
    # 显示列
    list_display = [
        'name', 'desc', 'detail', 'degree', 'learn_times',
        'students', 'fav_nums', 'image', 'click_nums', 'add_time'
    ]

    # 搜索
    search_fields = [
        'name', 'desc', 'detail', 'degree', 'learn_times',
        'students', 'fav_nums', 'image', 'click_nums'
    ]

    # 过滤器
    list_filter = [
        'name', 'desc', 'detail', 'degree', 'learn_times',
        'students', 'fav_nums', 'image', 'click_nums', 'add_time'
    ]


class LessonAdmin(object):
    """
    课程章节模型类后台管理器
    """

    # 显示列
    list_display = ['course', 'name', 'add_time']

    # 搜索
    search_fields = ['course', 'name']

    # 过滤器
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    """章节视频模型类管理器"""

    # 显示列
    list_display = ['lesson', 'name', 'add_time']

    # 搜索
    search_fields = ['lesson', 'name']

    # 过滤器
    list_filter = ['lesson__name', 'name', 'add_time']


class CourseResourceAdmin(object):
    """
    课程资源模型类管理器
    """

    # 显示列
    list_display = ['course', 'name', 'download']

    # 搜索
    search_fields = ['course', 'name', 'download']

    # 过滤器
    list_filter = ['course__name', 'name', 'download']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
