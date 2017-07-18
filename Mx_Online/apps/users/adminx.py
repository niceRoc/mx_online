# -*- coding: utf-8 -*-
import xadmin

from. models import EmailVerifyRecord, Banner

__author__ = 'Dunn'
__date__ = '2017/7/18 下午3:08'


class EmailVerifyRecordAdmin(object):
    """
    邮箱验证码模型类后台管理器
    """

    # 显示列
    list_display = ['code', 'email', 'send_type', 'send_time']

    # 搜索
    search_fields = ['code', 'email', 'send_type']

    # 过滤器
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    """
    轮播图模型类后台管理器
    """

    # 显示列
    list_display = ['title', 'image', 'url', 'index', 'add_time']

    # 搜索
    search_fields = ['title', 'image', 'url', 'index']

    # 过滤器
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
