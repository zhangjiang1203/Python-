# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:张江

from django.conf.urls import url

from . import views

# 添加命名空间
app_name = 'polls'  #关键的是这行

urlpatterns = [

    # url都有四个参数
    # 参数1：描述匹配的字符串或者url
    # 参数2：view指当前处理url请求的视图函数
    # 参数3：kwargs 任意数量的关键字参数可以作为一个字典传递给目标视图
    # 参数4：name对url命名，在模板内部显式的引用它
    # path多了一个patten参数

    # url路由设置
    # url(r'^$',views.index,name='index'),
    # path路由设置
    url('^$', views.index,name='index'),
    # 直接搜索 polls/id
    url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
    # 直接访问 polls/id/results
    url(r'^(?P<question_id>[0-9]+)/results/$',views.results,name='results'),
    # 直接访问 polls/id/vote
    url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
]

# 刚开始创建的时候 urlpattrens = {}  默认的是{}  修改为[]  就可以访问http://127.0.0.1:8000/admin/


