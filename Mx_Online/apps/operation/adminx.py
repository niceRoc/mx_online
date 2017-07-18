# -*- coding: utf-8 -*-
import xadmin

from .models import \
    UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse

__author__ = 'Dunn'
__date__ = '2017/7/18 下午5:07'


class UserAskAdmin(object):
    """用户咨询模型类后台管理器"""

    # 显示列
    list_display = ['name', 'mobile', 'course_name', 'add_time']

    # 搜索
    search_fields = ['name', 'mobile', 'course_name']

    # 过滤器
    list_filter = ['name', 'mobile', 'course_name', 'add_time']


class CourseCommentsAdmin(object):
    """课程评论模型类后台管理器"""

    # 显示列
    list_display = ['user', 'course', 'comments', 'add_time']

    # 搜索
    search_fields = ['user', 'course', 'comments']

    # 过滤器
    list_filter = ['user__username', 'course__name', 'comments', 'add_time']


class UserFavoriteAdmin(object):
    """用户收藏模型类后台管理器"""

    # 显示列
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']

    # 搜索
    search_fields = ['user', 'fav_id', 'fav_type']

    # 过滤器
    list_filter = ['user__username', 'fav_id', 'fav_type', 'add_time']


class UserMessageAdmin(object):
    """用户消息模型类后台管理器"""

    # 显示列
    list_display = ['user', 'message', 'has_read', 'add_time']

    # 搜索
    search_fields = ['user', 'message', 'has_read']

    # 过滤器
    list_filter = ['user', 'message', 'has_read', 'add_time']


class UserCourseAdmin(object):
    """用户所学课程模型类后台管理器"""

    # 显示列
    list_display = ['user', 'course', 'add_time']

    # 搜索
    search_fields = ['user', 'course']

    # 过滤器
    list_filter = ['user__username', 'course__name', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
