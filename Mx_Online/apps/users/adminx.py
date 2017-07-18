# -*- coding: utf-8 -*-
import xadmin
from xadmin import views

from. models import EmailVerifyRecord, Banner

__author__ = 'Dunn'
__date__ = '2017/7/18 下午3:08'


@xadmin.sites.register(views.BaseAdminView)
class BaseSetting(object):
    """设置后台的主题样式"""

    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    """全局设置后台显示"""

    site_title = "慕学后台管理系统"
    site_footer = "慕学在线网"
    menu_style = "accordion"


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

# xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
