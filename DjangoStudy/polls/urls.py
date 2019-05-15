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
    # 参数4：name对url命名，在模板内部显式的引用它，反向解析的时候很有用 (视图函数和模板都都可以使用)
    #"""
    #视图函数
    #from django.shortcuts import reverse
    # reverse(name)
    #模板文件中
    #<a href="{% url name 参数 %}">
    #"""
    # path多了一个patten参数


    # url路由设置
    # url(r'^$',views.index,name='index'),
    # path路由设置
    url('^$', views.IndexView.as_view(),name='index'),
    # 直接搜索 polls/id
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
    # 直接访问 polls/id/results
    url(r'^(?P<pk>[0-9]+)/results/$',views.ResultsView.as_view(),name='results'),
    # 直接访问 polls/id/vote
    url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote')



    # 不使用类视图的URL设置方法
    #url('^$', views.index,name='index'),
    # 直接搜索 polls/id
    #url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
    # 直接访问 polls/id/results
    #url(r'^(?P<question_id>[0-9]+)/results/$',views.result,name='results'),
    # 直接访问 polls/id/vote
    #url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),

]

# 刚开始创建的时候 urlpattrens = {}  默认的是{}  修改为[]  就可以访问http://127.0.0.1:8000/admin/


'''
1.url参数  正则表达式 ，对应的路由地址

无名分组对路径进行分组 下面括号内的内容会被分组，当做参数一起传入
url(r'^index/(\d+)',对应的视图也要添加参数)

有名分组
获取到的值赋值给pk和pkk，并将它们以键值对的方式添加到请求中pk=4 或者pkk=5
url(r'^index/(?P<pk>\d+)/(?P<pkk>\d+)',view.index)

'''


