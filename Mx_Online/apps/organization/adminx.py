# -*- coding: utf-8 -*-
import xadmin

from .models import CityDict, CourseOrg, Teacher

__author__ = 'Dunn'
__date__ = '2017/7/18 下午4:56'


class CityDictAdmin(object):
    """城市信息模型类管理器"""

    # 显示列
    list_display = ['name', 'desc', 'add_time']

    # 搜索
    search_fields = ['name', 'desc']

    # 过滤器
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    """机构模型类管理器"""

    # 显示列
    list_display = [
        'name', 'desc', 'click_nums', 'fav_nums', 'images',
        'address', 'city', 'add_time'
    ]

    # 搜索
    search_fields = [
        'name', 'desc', 'click_nums', 'fav_nums', 'images', 'address', 'city'
    ]

    # 过滤器
    list_filter = [
        'name', 'desc', 'click_nums', 'fav_nums', 'images',
        'address', 'city__name', 'add_time'
    ]


class TeacherAdmin(object):
    """讲师模型类管理器"""

    # 显示列
    list_display = [
        'org', 'name', 'work_years', 'work_company', 'work_position',
        'points', 'click_nums', 'fav_nums', 'add_time'
    ]

    # 搜索
    search_fields = [
        'org', 'name', 'work_years', 'work_company', 'work_position',
        'points', 'click_nums', 'fav_nums'
    ]

    # 过滤器
    list_filter = [
        'org__name', 'name', 'work_years', 'work_company', 'work_position',
        'points', 'click_nums', 'fav_nums', 'add_time'
    ]


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
