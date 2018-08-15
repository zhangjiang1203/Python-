# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:张江
from django.conf.urls import url

from django.urls import path


from . import views

urlpatterns = {

    # url都有四个参数
    # 参数1：描述匹配的字符串或者url
    # 参数2：view指当前处理url请求的视图函数
    # 参数3：kwargs 任意数量的关键字参数可以作为一个字典传递给目标视图
    # 参数4：name对url命名，在模板内部显式的引用它
    # path多了一个patten参数

    # url路由设置
    # url(r'^$',views.index,name='index'),
    # path路由设置
    path('', views.index,name='index'),
}